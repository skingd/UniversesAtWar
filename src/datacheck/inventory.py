"""Phase A1 — file inventory.

Walks the BattleTech Data Files tree and records every relevant file with its
parse status. Output is consumed by later phases.
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterator

from .common import (
    Issue,
    SUBDIR,
    UNIT_FILE_EXT,
    UNIT_TYPES,
    WEAPON_CATEGORIES,
    parse_json_file,
    parse_yaml_file,
)


def iter_unit_files(data_dir: Path, unit_type: str) -> Iterator[Path]:
    """Yield all unit files for a given unit type, recursively."""
    root = data_dir / SUBDIR[unit_type]
    if not root.exists():
        return
    ext = UNIT_FILE_EXT[unit_type]
    for p in root.rglob(f"*{ext}"):
        # skip the auto-generated reports in mechs/
        if p.name in ("conversion_report.json", "verification_report.json"):
            continue
        yield p


def iter_weapon_files(data_dir: Path) -> Iterator[tuple[str, Path]]:
    """Yield (category, path) for every weapon/equipment JSON."""
    root = data_dir / "weaponsandequipment"
    if not root.exists():
        return
    # ammunition.json sits at the top level of weaponsandequipment/
    ammo = root / "ammunition.json"
    if ammo.exists():
        yield "ammunition", ammo
    for cat in WEAPON_CATEGORIES:
        sub = root / cat
        if not sub.exists():
            continue
        for p in sub.glob("*.json"):
            yield cat, p


def iter_reference_files(data_dir: Path) -> Iterator[Path]:
    root = data_dir / "reference"
    if not root.exists():
        return
    for p in root.glob("*.json"):
        yield p


def build_inventory(data_dir: Path) -> tuple[dict, list[Issue]]:
    """Build the master inventory and surface parse errors as issues."""
    issues: list[Issue] = []
    inv: dict = {
        "data_dir": str(data_dir),
        "units": {},
        "weapons": {},
        "reference": {},
        "totals": {},
    }

    # --- units
    total_units = 0
    parse_failures = 0
    for ut in UNIT_TYPES:
        records = []
        for p in iter_unit_files(data_dir, ut):
            parser = parse_json_file if p.suffix == ".json" else parse_yaml_file
            data, err = parser(p)
            entry = {
                "path": str(p),
                "size": p.stat().st_size,
                "parsed": data is not None,
                "warning": err if data is not None else None,
                "error": err if data is None else None,
            }
            records.append(entry)
            total_units += 1
            if data is None:
                parse_failures += 1
                issues.append(Issue("error", "parse", str(p), f"failed to parse {ut}: {err}"))
            elif err:
                issues.append(Issue("warning", "encoding", str(p), err))
        inv["units"][ut] = {
            "count": len(records),
            "files": records,
        }

    # --- weapons / equipment
    weapon_buckets: dict[str, list[dict]] = {}
    for cat, p in iter_weapon_files(data_dir):
        data, err = parse_json_file(p)
        entry = {
            "path": str(p),
            "size": p.stat().st_size,
            "parsed": data is not None,
            "warning": err if data is not None else None,
            "error": err if data is None else None,
        }
        weapon_buckets.setdefault(cat, []).append(entry)
        if data is None:
            parse_failures += 1
            issues.append(Issue("error", "parse", str(p), f"failed to parse weapon ({cat}): {err}"))
        elif err:
            issues.append(Issue("warning", "encoding", str(p), err))
    for cat, recs in weapon_buckets.items():
        inv["weapons"][cat] = {"count": len(recs), "files": recs}

    # --- reference
    ref_records = []
    for p in iter_reference_files(data_dir):
        data, err = parse_json_file(p)
        ref_records.append({
            "path": str(p),
            "name": p.name,
            "parsed": data is not None,
            "warning": err if data is not None else None,
            "error": err if data is None else None,
        })
        if data is None:
            issues.append(Issue("error", "parse", str(p), f"failed to parse reference: {err}"))
    inv["reference"] = {"count": len(ref_records), "files": ref_records}

    inv["totals"] = {
        "units": total_units,
        "weapons": sum(len(r) for r in weapon_buckets.values()),
        "reference": len(ref_records),
        "parse_failures": parse_failures,
    }

    return inv, issues
