"""CLI: ``python -m src.detachments``.

Reads pre-built indices from ``data/index`` plus ``data/WeaponRules.csv`` /
``data/AmmunitionRules.csv``, and emits per-type ``detachments_<type>.json``
files plus a coverage report.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from src.datacheck.alias_resolver import build_alias_index
from src.detachments.assemble import Coverage, build_all
from src.detachments.weapons import (
    build_weapon_index,
    load_ammunition_rules,
    load_weapon_rules,
)


_INDEX_FILES: dict[str, str] = {
    "mech":      "mech_index.json",
    "vehicle":   "vehicle_index.json",
    "aerospace": "aerospace_index.json",
}


def _load_json(path: Path) -> object:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _coverage_markdown(per_type: dict[str, Coverage]) -> str:
    lines: list[str] = ["# Detachments Build Coverage", ""]
    for unit_type, cov in per_type.items():
        lines.append(f"## {unit_type}")
        lines.append("")
        lines.append(f"- Total records: **{cov.total_records}**")
        lines.append(f"- Emitted: **{cov.emitted}**")
        lines.append(f"- Skipped — unknown tech_base: {cov.skipped_unknown_tech_base}")
        lines.append(f"- Skipped — missing tonnage: {cov.skipped_missing_tonnage}")
        lines.append(f"- Skipped — missing armor: {cov.skipped_missing_armor}")
        lines.append(f"- Skipped — missing movement: {cov.skipped_missing_movement}")
        lines.append(f"- Speed gap fall-backs: {len(cov.missing_speed)}")
        if cov.missing_speed:
            sample = cov.missing_speed[:5]
            lines.append("  - Examples:")
            for s in sample:
                lines.append(
                    f"    - {s['unit']} (speed={s['speed']} → {s['fallback_movement']})"
                )
        lines.append(f"- Distinct unmapped weapon names: {len(cov.unmapped_weapons)}")
        if cov.unmapped_weapons:
            top = sorted(cov.unmapped_weapons.items(), key=lambda kv: -kv[1])[:25]
            lines.append("")
            lines.append("| Weapon | Installations |")
            lines.append("| --- | ---: |")
            for name, count in top:
                lines.append(f"| {name} | {count} |")
        lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="uaw-detachments",
        description="Build per-type detachment JSON profiles from indices + rule CSVs.",
    )
    parser.add_argument("--index-dir", type=Path, default=Path("data/index"),
        help="Directory holding *_index.json files (default: data/index).")
    parser.add_argument("--weapon-rules", type=Path,
        default=Path("data/WeaponRules.csv"),
        help="Path to WeaponRules.csv (default: data/WeaponRules.csv).")
    parser.add_argument("--ammo-rules", type=Path,
        default=Path("data/AmmunitionRules.csv"),
        help="Path to AmmunitionRules.csv (default: data/AmmunitionRules.csv).")
    parser.add_argument("--output-dir", type=Path,
        default=Path("output/detachments"),
        help="Where to write detachments_<type>.json + coverage (default: output/detachments).")
    parser.add_argument("--types", nargs="+", default=["mech", "vehicle", "aerospace"],
        choices=["mech", "vehicle", "aerospace"],
        help="Which unit types to build.")
    args = parser.parse_args(argv)

    if not args.index_dir.exists():
        print(f"ERROR: index-dir does not exist: {args.index_dir}", file=sys.stderr)
        return 2
    if not args.weapon_rules.exists():
        print(f"ERROR: weapon-rules not found: {args.weapon_rules}", file=sys.stderr)
        return 2
    if not args.ammo_rules.exists():
        print(f"ERROR: ammo-rules not found: {args.ammo_rules}", file=sys.stderr)
        return 2

    args.output_dir.mkdir(parents=True, exist_ok=True)

    print(f"[detachments] loading WeaponRules: {args.weapon_rules}")
    profiles = load_weapon_rules(args.weapon_rules)
    print(f"[detachments]   {len(profiles)} weapon profiles")

    print(f"[detachments] loading AmmunitionRules: {args.ammo_rules}")
    ammo_index = load_ammunition_rules(args.ammo_rules)
    print(f"[detachments]   {sum(len(v) for v in ammo_index.values())} ammo options "
          f"across {len(ammo_index)} weapons")

    eq_path = args.index_dir / "equipment_index.json"
    equipment_records: list[dict] = []
    alias_index = None
    if eq_path.exists():
        print(f"[detachments] loading equipment_index: {eq_path}")
        equipment_records = _load_json(eq_path)  # type: ignore[assignment]
        try:
            alias_index = build_alias_index(equipment_records)
            print(f"[detachments]   alias index ready ({len(alias_index.exact)} keys)")
        except Exception as ex:
            print(f"[detachments]   WARNING: alias index build failed: {ex}",
                  file=sys.stderr)
            alias_index = None
    else:
        print(f"[detachments]   (no equipment_index.json — name-only resolution)")

    weapon_index = build_weapon_index(profiles, equipment_records=equipment_records)
    print(f"[detachments]   weapon index: {len(weapon_index.by_name_key)} by-name, "
          f"{len(weapon_index.by_canonical_id)} by-canonical-id")

    coverage_per_type: dict[str, Coverage] = {}
    for unit_type in args.types:
        idx_path = args.index_dir / _INDEX_FILES[unit_type]
        if not idx_path.exists():
            print(f"[detachments] SKIP {unit_type}: {idx_path} not found")
            continue
        print(f"[detachments] building {unit_type} from {idx_path}")
        records = _load_json(idx_path)
        if not isinstance(records, list):
            print(f"[detachments]   WARNING: {idx_path} is not a JSON array; skipping",
                  file=sys.stderr)
            continue
        detachments, cov = build_all(
            records, unit_type, weapon_index, ammo_index, alias_index,
        )
        out_file = args.output_dir / f"detachments_{unit_type}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(detachments, f, indent=2, ensure_ascii=False)
        print(f"[detachments]   wrote {len(detachments)} → {out_file}")
        print(f"[detachments]   coverage: {cov.emitted}/{cov.total_records} emitted, "
              f"{len(cov.unmapped_weapons)} unmapped weapon names, "
              f"{len(cov.missing_speed)} speed gaps")
        coverage_per_type[unit_type] = cov

    cov_json = args.output_dir / "coverage.json"
    with open(cov_json, "w", encoding="utf-8") as f:
        json.dump({k: v.to_dict() for k, v in coverage_per_type.items()},
                  f, indent=2, ensure_ascii=False)
    cov_md = args.output_dir / "coverage.md"
    cov_md.write_text(_coverage_markdown(coverage_per_type), encoding="utf-8")
    print(f"[detachments] wrote coverage report: {cov_json}, {cov_md}")
    return 0
