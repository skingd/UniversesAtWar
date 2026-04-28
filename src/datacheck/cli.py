"""CLI entry point: python -m src.datacheck"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .common import UNIT_TYPES, parse_json_file, parse_yaml_file
from .cross_reference import (
    resolve_ammo_links,
    resolve_eras,
    resolve_quirks,
    resolve_unit_equipment,
)
from .hygiene import (
    check_duplicates,
    check_ranges,
    check_required_fields,
    detect_orphans_via_indices,
)
from .index_builder import build_all_indices
from .inventory import build_inventory, iter_unit_files
from .reporter import write_reports


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="uaw-datacheck",
        description="Validate BattleTech source data and build canonical indices.")
    parser.add_argument("--data-dir", required=True, type=Path,
        help="Path to the BattleTech 'Data Files' root directory.")
    parser.add_argument("--output-dir", type=Path,
        default=Path("output/data-check"),
        help="Where to write reports (default: output/data-check)")
    parser.add_argument("--index-dir", type=Path,
        default=Path("data/index"),
        help="Where to write canonical indices (default: data/index)")
    parser.add_argument("--strict", action="store_true",
        help="Treat warnings as failures.")
    parser.add_argument("--fuzzy-threshold", type=int, default=85,
        help="Min fuzzy-match score for unresolved-equipment suggestions (default: 85)")
    parser.add_argument("--fail-threshold", type=float, default=1.0,
        help="Max allowed unresolved-equipment percentage before FAIL (default: 1.0)")
    parser.add_argument("--gate-types", default="mech,vehicle,aerospace",
        help="Comma-separated unit types whose unresolved-pct counts toward the "
             "FAIL gate (default: mech,vehicle,aerospace). Infantry is excluded "
             "by default because the source data has no infantry-weapon catalog.")

    args = parser.parse_args(argv)
    data_dir: Path = args.data_dir
    if not data_dir.exists():
        print(f"ERROR: data-dir does not exist: {data_dir}", file=sys.stderr)
        return 2

    print(f"[datacheck] data-dir: {data_dir}")
    print(f"[datacheck] index-dir: {args.index_dir}")
    print(f"[datacheck] output-dir: {args.output_dir}")

    all_issues = []

    # Phase A1: inventory
    print("[datacheck] Phase A1: building inventory ...")
    inventory, inv_issues = build_inventory(data_dir)
    all_issues.extend(inv_issues)
    print(f"  scanned {inventory['totals']['units']} unit files, "
          f"{inventory['totals']['weapons']} weapons, "
          f"{inventory['totals']['parse_failures']} parse failure(s)")

    # Phase A2/A3/A4/A5: build indices
    print("[datacheck] Phase A2-A5: building canonical indices ...")
    index_summary, alias_index, idx_issues = build_all_indices(data_dir, args.index_dir)
    all_issues.extend(idx_issues)
    print(f"  equipment={index_summary['equipment_count']} "
          f"(synthesized={index_summary.get('synthesized_count', 0)}) "
          f"aliases={index_summary['alias_count']}")
    for ut, n in index_summary["units"].items():
        print(f"  {ut}: {n}")

    # load the unit indices we just wrote
    unit_indices = {}
    for ut in UNIT_TYPES:
        path = args.index_dir / f"{ut}_index.json"
        if path.exists():
            unit_indices[ut] = json.loads(path.read_text(encoding="utf-8"))
    equipment_records = json.loads((args.index_dir / "equipment_index.json").read_text(encoding="utf-8"))
    reference = json.loads((args.index_dir / "reference_index.json").read_text(encoding="utf-8"))

    # Phase B: cross-reference
    print("[datacheck] Phase B: cross-reference resolution ...")
    resolution_report, res_issues = resolve_unit_equipment(
        unit_indices, alias_index, fuzzy_threshold=args.fuzzy_threshold
    )
    all_issues.extend(res_issues)
    print(f"  resolved {resolution_report['resolution_rate']}% "
          f"({resolution_report['totals']['unresolved']} unresolved)")

    quirk_report, q_issues = resolve_quirks(unit_indices, reference)
    all_issues.extend(q_issues)
    era_report, e_issues = resolve_eras(unit_indices, reference)
    all_issues.extend(e_issues)
    ammo_report, a_issues = resolve_ammo_links(equipment_records)
    all_issues.extend(a_issues)

    # Phase C: hygiene
    print("[datacheck] Phase C: hygiene checks ...")
    raw_unit_files = _load_raw_unit_files(data_dir)
    field_report, f_issues = check_required_fields(raw_unit_files, equipment_records)
    all_issues.extend(f_issues)
    range_report, r_issues = check_ranges(raw_unit_files)
    all_issues.extend(r_issues)
    dup_report, d_issues = check_duplicates(unit_indices, equipment_records)
    all_issues.extend(d_issues)
    orphan_report, _ = detect_orphans_via_indices(equipment_records, unit_indices, alias_index)
    print(f"  orphan equipment: {orphan_report['orphan_count']}")

    # Phase D: report
    print("[datacheck] Phase D: writing reports ...")
    gate_types = tuple(t.strip() for t in args.gate_types.split(",") if t.strip())
    passed, msg = write_reports(
        args.output_dir,
        inventory,
        index_summary,
        resolution_report,
        quirk_report,
        era_report,
        ammo_report,
        field_report,
        range_report,
        dup_report,
        orphan_report,
        all_issues,
        fail_threshold_pct=args.fail_threshold,
        gate_types=gate_types,
        strict=args.strict,
    )
    print(f"[datacheck] {msg}")
    print(f"[datacheck] report: {args.output_dir / 'REPORT.md'}")
    return 0 if passed else 1


def _load_raw_unit_files(data_dir: Path) -> dict[str, list[tuple[object, str]]]:
    """Re-read every unit file (as raw dicts) for hygiene checks that need the
    original field names rather than the normalized index records."""
    out: dict[str, list[tuple[object, str]]] = {}
    for ut in UNIT_TYPES:
        items: list[tuple[object, str]] = []
        for p in iter_unit_files(data_dir, ut):
            parser = parse_json_file if p.suffix == ".json" else parse_yaml_file
            data, _err = parser(p)
            items.append((data, str(p)))
        out[ut] = items
    return out


if __name__ == "__main__":
    raise SystemExit(main())
