"""CLI entry point: python -m src.itemization"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .aggregations import aggregate_units, aggregate_weapons
from .bands import derive_translation_bands
from .catalogues import build_catalogues
from .common import read_json
from .reporter import write_all


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="uaw-itemize",
        description="Build itemization catalogues + capability aggregations "
                    "from canonical indices produced by uaw-datacheck.",
    )
    parser.add_argument("--index-dir", type=Path, default=Path("data/index"),
        help="Directory containing the canonical index JSON files (default: data/index)")
    parser.add_argument("--output-dir", type=Path, default=Path("output/itemization"),
        help="Where to write itemization reports (default: output/itemization)")
    parser.add_argument("--data-dir", type=Path, default=None,
        help="Optional path to the BattleTech 'Data Files' root. When given, "
             "raw unit files are re-scanned to enrich Part-2 aggregations with "
             "stats not present on the canonical index records (Walk MP, Armor "
             "Points, etc.).")
    parser.add_argument("--strict", action="store_true",
        help="Exit non-zero if Part-1 coverage is blocking or if any Part-2.3 "
             "validation hit-rate is below 90%%.")

    args = parser.parse_args(argv)
    index_dir: Path = args.index_dir
    if not index_dir.exists():
        print(f"ERROR: --index-dir does not exist: {index_dir}", file=sys.stderr)
        return 2

    print(f"[itemize] index-dir:  {index_dir}")
    print(f"[itemize] output-dir: {args.output_dir}")
    print(f"[itemize] data-dir:   {args.data_dir or '(not provided — partial Part-2 stats)'}")

    # Load indices
    equipment_records = read_json(index_dir / "equipment_index.json")
    unit_indices = {}
    for ut in ("mech", "vehicle", "aerospace", "infantry"):
        p = index_dir / f"{ut}_index.json"
        if p.exists():
            unit_indices[ut] = read_json(p)
        else:
            unit_indices[ut] = []

    # Build alias index for usage cross-reference + coverage
    alias_index = _try_build_alias_index(index_dir, equipment_records)

    # Optionally re-scan raw unit files for richer Part-2.1 stats
    raw_unit_files = _maybe_load_raw_unit_files(args.data_dir) if args.data_dir else {}

    print("[itemize] Part 1: building catalogues ...")
    catalogues = build_catalogues(equipment_records, unit_indices, alias_index=alias_index)
    cov = catalogues["coverage"]
    print(f"  weapons={len(catalogues['weapons'])} "
          f"ammo={len(catalogues['ammunition'])} "
          f"equipment={len(catalogues['equipment'])} "
          f"upgrades={len(catalogues['upgrades'])}")
    print(f"  coverage: by_catalogue={cov.get('by_catalogue')} "
          f"uncatalogued={cov.get('uncatalogued_count')} "
          f"orphans={cov.get('orphan_count')} "
          f"blocking={cov.get('blocking')}")

    print("[itemize] Part 2.1: aggregating unit capabilities ...")
    unit_aggregations = aggregate_units(unit_indices, raw_unit_files)

    print("[itemize] Part 2.2: aggregating weapon capabilities ...")
    weapon_aggregations = aggregate_weapons(catalogues["weapons"])

    print("[itemize] Part 2.3: deriving translation bands ...")
    bands = derive_translation_bands(catalogues["weapons"], unit_aggregations, weapon_aggregations)
    rng = bands.get("weapon_range") or {}
    if "validation_hit_rate" in rng:
        print(f"  weapon_range validation: {rng['validation_hits']}/{rng['validation_total']} "
              f"= {rng['validation_hit_rate']*100:.0f}%")

    print("[itemize] writing reports ...")
    write_all(args.output_dir, catalogues, unit_aggregations, weapon_aggregations, bands)
    print(f"[itemize] report: {args.output_dir / 'REPORT.md'}")

    if args.strict:
        if cov.get("blocking"):
            print("[itemize] STRICT FAIL: coverage is blocking", file=sys.stderr)
            return 1
        if rng.get("passed_90pct") is False:
            print("[itemize] STRICT FAIL: weapon-range validation below 90%", file=sys.stderr)
            return 1
    return 0


def _try_build_alias_index(index_dir: Path, equipment_records: list[dict]):
    """Build an AliasIndex if the datacheck reference data is available."""
    try:
        from src.datacheck.alias_resolver import build_alias_index
    except ImportError:
        return None
    reference_path = index_dir / "reference_index.json"
    reference = read_json(reference_path) if reference_path.exists() else {}
    return build_alias_index(
        equipment_records,
        equipment_names=reference.get("equipment_names"),
        ammunition=None,
    )


def _maybe_load_raw_unit_files(data_dir: Path) -> dict:
    """Re-read every unit file as raw dicts for hygiene-grade stats."""
    if not data_dir.exists():
        print(f"[itemize] WARN: --data-dir not found, skipping raw scan: {data_dir}", file=sys.stderr)
        return {}
    try:
        from src.datacheck.common import UNIT_TYPES, parse_json_file, parse_yaml_file
        from src.datacheck.inventory import iter_unit_files
    except ImportError:
        return {}
    out: dict = {}
    for ut in UNIT_TYPES:
        items = []
        for p in iter_unit_files(data_dir, ut):
            parser = parse_json_file if p.suffix == ".json" else parse_yaml_file
            data, _err = parser(p)
            items.append((data, str(p)))
        out[ut] = items
    return out


if __name__ == "__main__":
    raise SystemExit(main())
