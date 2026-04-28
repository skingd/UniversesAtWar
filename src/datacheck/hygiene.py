"""Phase C — data hygiene checks (required fields, ranges, duplicates, orphans)."""
from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

from .common import Issue


REQUIRED_FIELDS = {
    "mech": ["chassis", "model", "Mass", "Walk MP", "Armor Points", "Equipment", "TechBase", "Era"],
    "vehicle": ["chassis", "Unit Type", "Motion Type", "Tonnage", "Cruise MP", "Armor Points"],
    "aerospace": ["chassis", "Aerospace Class", "Safe Thrust", "Structural Integrity", "Armor Points", "Fuel"],
    "infantry": ["chassis", "Unit Type", "Motion Type", "Platoon", "Primary Weapon"],
}

WEAPON_REQUIRED = ["id", "name", "tech_base", "damage", "range"]
AMMO_REQUIRED = ["id", "name", "tech_base", "weapon_ref", "weight_tons"]
EQUIPMENT_REQUIRED = ["id", "name", "tech_base", "weight_tons"]


def check_required_fields(
    raw_unit_files: dict[str, list[tuple[Any, str]]],  # {unit_type: [(parsed, path), ...]}
    equipment_records: list[dict],
) -> tuple[dict, list[Issue]]:
    """Verify required fields are present and non-empty."""
    issues: list[Issue] = []
    summary: dict[str, dict[str, int]] = {}

    for ut, items in raw_unit_files.items():
        missing = 0
        required = REQUIRED_FIELDS[ut]
        for parsed, path in items:
            if not isinstance(parsed, dict):
                continue
            for field in required:
                v = parsed.get(field)
                if v is None or v == "" or v == [] or v == {}:
                    missing += 1
                    issues.append(Issue(
                        "error", "missing-field", path,
                        f"missing required field {field!r} for {ut}",
                        {"field": field, "unit_type": ut},
                    ))
        summary[ut] = {"missing_field_count": missing, "files_checked": len(items)}

    # weapon/equipment required-field checks
    eq_missing = 0
    for rec in equipment_records:
        cat = rec.get("category")
        if cat == "ammunition":
            required = AMMO_REQUIRED
        elif cat == "equipment":
            required = EQUIPMENT_REQUIRED
        elif cat in ("ballistic", "energy", "missile", "physical", "infantry"):
            required = WEAPON_REQUIRED
        else:
            continue
        for f in required:
            # rec uses normalized field names; map back where needed
            target = {"id": "numeric_id", "name": "display_name"}.get(f, f)
            v = rec.get(target)
            if v is None or v == "":
                eq_missing += 1
                issues.append(Issue(
                    "error", "missing-field", rec["source_path"],
                    f"missing required field {f!r} for equipment ({cat})",
                    {"field": f, "category": cat, "canonical_id": rec["canonical_id"]},
                ))
    summary["equipment"] = {"missing_field_count": eq_missing, "records_checked": len(equipment_records)}
    return summary, issues


def check_ranges(raw_unit_files: dict[str, list[tuple[Any, str]]]) -> tuple[dict, list[Issue]]:
    """Validate numeric fields fall within plausible ranges."""
    issues: list[Issue] = []
    violations = 0

    bounds = {
        "Mass": (10, 200),       # mechs and large support vehicles
        "Walk MP": (0, 25),
        "Jump MP": (0, 12),
        "Cruise MP": (0, 30),
        "Tonnage": (0.1, 200),
        "Safe Thrust": (1, 30),
        "Structural Integrity": (1, 100),
        "Fuel": (0, 5000),
    }

    for ut, items in raw_unit_files.items():
        for parsed, path in items:
            if not isinstance(parsed, dict):
                continue
            for field, (lo, hi) in bounds.items():
                v = parsed.get(field)
                if v is None:
                    continue
                try:
                    n = float(v)
                except (TypeError, ValueError):
                    issues.append(Issue(
                        "warning", "non-numeric", path,
                        f"field {field!r} expected numeric, got {v!r}",
                        {"field": field, "value": v, "unit_type": ut},
                    ))
                    violations += 1
                    continue
                if not (lo <= n <= hi):
                    issues.append(Issue(
                        "warning", "out-of-range", path,
                        f"{field}={n} outside expected [{lo}, {hi}]",
                        {"field": field, "value": n, "min": lo, "max": hi, "unit_type": ut},
                    ))
                    violations += 1
    return {"violations": violations}, issues


def check_duplicates(unit_indices: dict[str, list[dict]], equipment_records: list[dict]) -> tuple[dict, list[Issue]]:
    issues: list[Issue] = []
    summary: dict[str, int] = {}

    for ut, records in unit_indices.items():
        keys = Counter()
        path_for: dict[str, list[str]] = defaultdict(list)
        for r in records:
            keys[r["key"]] += 1
            path_for[r["key"]].append(r["source_path"])
        dup_count = 0
        for k, n in keys.items():
            if n > 1:
                dup_count += 1
                issues.append(Issue(
                    "warning", "duplicate-unit", path_for[k][0],
                    f"unit key {k!r} appears {n} times",
                    {"key": k, "paths": path_for[k]},
                ))
        summary[f"{ut}_duplicate_keys"] = dup_count

    # equipment numeric_id duplicates
    nid_counter = Counter()
    nid_paths: dict[str, list[str]] = defaultdict(list)
    for rec in equipment_records:
        nid = rec.get("numeric_id")
        if nid:
            nid_counter[nid] += 1
            nid_paths[nid].append(rec["source_path"])
    eq_dups = 0
    for nid, n in nid_counter.items():
        if n > 1:
            eq_dups += 1
            issues.append(Issue(
                "warning", "duplicate-equipment-id", nid_paths[nid][0],
                f"equipment numeric id {nid!r} appears {n} times",
                {"numeric_id": nid, "paths": nid_paths[nid]},
            ))
    summary["equipment_duplicate_numeric_ids"] = eq_dups
    return summary, issues


def detect_orphan_equipment(
    equipment_records: list[dict],
    resolution_per_unit: list[dict],
) -> tuple[dict, list[Issue]]:
    """Equipment never referenced by any unit (informational)."""
    used: set[str] = set()
    # We can't tell exactly which canonical_id was matched without re-running
    # resolution; instead we approximate by collecting normalized raw refs that
    # successfully resolved -- but for orphan detection we compare canonical_ids
    # directly. Here we flag equipment whose numeric_id never appears as a hit.
    # Simpler approximation: compare display_name normalized form against any
    # successfully-resolved unit ref.
    referenced_names: set[str] = set()
    for u in resolution_per_unit:
        for unr in u.get("unresolved", []):
            # ignore unresolved
            pass
    # Without preserving matched canonical_ids upstream, we treat orphan detection
    # as "equipment with no unit referencing its display_name in its raw refs".
    # This is informational only.
    raw_strings: list[str] = []
    for u in resolution_per_unit:
        # we don't have raw refs here; orphan check requires the unit indices
        pass
    # Return placeholder summary. The orphan detection is enriched in the
    # reporter where raw refs are accessible.
    return {"orphan_count": 0, "computed": False}, []


def detect_orphans_via_indices(
    equipment_records: list[dict],
    unit_indices: dict[str, list[dict]],
    alias_index,  # AliasIndex
) -> tuple[dict, list[Issue]]:
    """Orphan = equipment whose canonical_id is never matched by any unit ref."""
    from .alias_resolver import parse_reference
    used: set[str] = set()
    for records in unit_indices.values():
        for unit in records:
            for raw in unit.get("raw_equipment_refs") or []:
                parsed = parse_reference(raw)
                cid, _kind = alias_index.lookup(parsed)
                if cid:
                    used.add(cid)

    orphans = [
        {
            "canonical_id": rec["canonical_id"],
            "display_name": rec["display_name"],
            "category": rec["category"],
            "tech_base": rec.get("tech_base"),
        }
        for rec in equipment_records
        if rec["canonical_id"] not in used
    ]
    return {"orphan_count": len(orphans), "orphans": orphans}, []
