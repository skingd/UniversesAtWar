"""Phase A2/A3/A5 — canonical index builders.

Produces:
    data/index/equipment_index.json
    data/index/equipment_aliases.json
    data/index/reference_index.json
    data/index/{mech,vehicle,aerospace,infantry}_index.json
"""
from __future__ import annotations

import os
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, Iterable

from .alias_resolver import (
    AliasIndex,
    build_alias_index,
    is_structural,
    parse_reference,
)
from .common import (
    Issue,
    UNIT_TYPES,
    file_slug,
    parse_json_file,
    parse_yaml_file,
    slugify,
    write_json,
)
from .inventory import iter_reference_files, iter_unit_files, iter_weapon_files
from .stats import (
    extract_armor_total,
    extract_cruise_mp,
    extract_infantry_movement,
    extract_jump_mp,
    extract_safe_thrust,
    extract_walk_mp,
)


# Ammunition is not modelled by the Universes At War rules translation; ammo
# entries are dropped from the equipment index, alias map, and per-unit
# equipment refs at build time.
_AMMO_RX = re.compile(r"\bammo\b|\bammunition\b", re.IGNORECASE)


def _is_ammo_text(s: str | None) -> bool:
    return bool(s and _AMMO_RX.search(s))


# I/O is the bottleneck (thousands of small JSON/YAML files, often on
# OneDrive). Parsing happens in a thread pool; per-file results are returned
# in the original input order so downstream dedup logic stays deterministic.
_DEFAULT_WORKERS = min(32, (os.cpu_count() or 4) * 4)


def _parse_files_threaded(
    paths: Iterable[Path],
    parser_for: Callable[[Path], Callable[[Path], tuple[Any, Any]]],
    *,
    max_workers: int = _DEFAULT_WORKERS,
) -> list[tuple[Path, Any, Any]]:
    """Parse ``paths`` in parallel. Returns ``[(path, data, err), ...]`` in
    the same order as ``paths``."""
    paths = list(paths)
    if not paths:
        return []

    def _one(p: Path) -> tuple[Path, Any, Any]:
        data, err = parser_for(p)(p)
        return p, data, err

    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        return list(ex.map(_one, paths))


# --- Equipment index -------------------------------------------------------

def build_equipment_index(data_dir: Path) -> tuple[list[dict], list[Issue]]:
    """Walk weaponsandequipment/ and build canonical equipment records."""
    issues: list[Issue] = []
    records: list[dict] = []
    seen_canonical: dict[str, str] = {}
    seen_numeric: dict[str, str] = {}

    cat_path_pairs = list(iter_weapon_files(data_dir))
    parsed = _parse_files_threaded(
        (p for _cat, p in cat_path_pairs),
        lambda _p: parse_json_file,
    )
    for (cat, _p), (p, data, _err) in zip(cat_path_pairs, parsed):
        if data is None:
            continue  # already reported by inventory phase

        if cat == "ammunition":
            # Ammunition is intentionally excluded from the equipment index.
            continue

        if not isinstance(data, dict):
            issues.append(Issue("error", "schema", str(p), f"weapon JSON not an object ({cat})"))
            continue

        rec = _record_from_weapon_or_equipment(data, p, cat)
        _register(rec, records, seen_canonical, seen_numeric, issues)

    return records, issues


def _record_from_weapon_or_equipment(data: dict, path: Path, category: str) -> dict:
    name = data.get("name") or data.get("mtf_reference") or path.stem
    cid = file_slug(path.name)
    return {
        "canonical_id": cid,
        "numeric_id": str(data.get("id", "")) or None,
        "display_name": name,
        "mtf_reference": data.get("mtf_reference"),
        "category": category,
        "tech_base": data.get("tech_base"),
        "tech_rating": data.get("tech_rating"),
        "rarity": data.get("rarity"),
        "weight_tons": data.get("weight_tons"),
        "damage": data.get("damage"),
        "heat": data.get("heat"),
        "range": data.get("range"),
        "aerospace_range": data.get("aerospace_range"),
        "ammo_per_ton": data.get("ammo_per_ton"),
        "space": data.get("space"),
        "cost": data.get("cost"),
        "source": data.get("source"),
        "page_ref": data.get("page_ref"),
        "equipment_type": data.get("equipment_type"),
        "source_path": str(path),
    }


def _register(
    rec: dict,
    out: list[dict],
    seen_canonical: dict[str, str],
    seen_numeric: dict[str, str],
    issues: list[Issue],
) -> None:
    cid = rec["canonical_id"]
    # disambiguate canonical_id collisions (e.g. two ammo entries with identical names)
    if cid in seen_canonical:
        # append numeric_id to make unique; if no numeric_id, append a counter
        suffix = rec.get("numeric_id") or str(sum(1 for r in out if r["canonical_id"].startswith(cid)))
        new_cid = f"{cid}-{suffix}"
        issues.append(Issue(
            "warning", "duplicate-canonical-id", rec["source_path"],
            f"canonical id collision; reassigned",
            {"original": cid, "renamed_to": new_cid, "previous": seen_canonical[cid]},
        ))
        rec["canonical_id"] = new_cid
        cid = new_cid
    seen_canonical[cid] = rec["source_path"]

    nid = rec.get("numeric_id")
    if nid:
        if nid in seen_numeric:
            issues.append(Issue(
                "warning", "duplicate-numeric-id", rec["source_path"],
                f"numeric id {nid} also present at {seen_numeric[nid]}",
                {"numeric_id": nid, "previous": seen_numeric[nid]},
            ))
        else:
            seen_numeric[nid] = rec["source_path"]

    out.append(rec)


# --- Reference index -------------------------------------------------------

def build_reference_index(data_dir: Path) -> dict:
    out: dict = {}
    parsed = _parse_files_threaded(
        iter_reference_files(data_dir),
        lambda _p: parse_json_file,
    )
    for p, data, _err in parsed:
        if data is None:
            continue
        out[p.stem] = data
    return out


# --- Unit indices ----------------------------------------------------------

def build_unit_index(
    data_dir: Path,
    unit_type: str,
) -> tuple[list[dict], list[Issue]]:
    """Build a canonical index of all units of one type."""
    issues: list[Issue] = []
    records: list[dict] = []
    seen_keys: dict[str, str] = {}

    parsed = _parse_files_threaded(
        iter_unit_files(data_dir, unit_type),
        lambda p: parse_json_file if p.suffix == ".json" else parse_yaml_file,
    )
    for p, data, _err in parsed:
        if data is None or not isinstance(data, dict):
            continue

        chassis = data.get("chassis") or ""
        model = data.get("model") or ""
        mul_id = data.get("mul id")

        canonical_id = f"{slugify(chassis)}-{slugify(str(model))}" if chassis or model else file_slug(p.name)
        key = str(mul_id) if mul_id is not None else canonical_id

        if key in seen_keys:
            issues.append(Issue(
                "warning", "duplicate-unit-key", str(p),
                f"unit key {key} already used by {seen_keys[key]}",
                {"key": key, "previous": seen_keys[key]},
            ))
        else:
            seen_keys[key] = str(p)

        rec = {
            "canonical_id": canonical_id,
            "key": key,
            "mul_id": mul_id,
            "chassis": chassis,
            "model": model,
            "unit_type": unit_type,
            "tech_base": data.get("TechBase") or _split_tech_field(data.get("Tech Base / Rules Level")),
            "rules_level": data.get("Rules Level") or _split_rules_level(data.get("Tech Base / Rules Level")),
            "era": data.get("Era") or data.get("Year"),
            "tonnage": data.get("Mass") or data.get("Tonnage"),
            "role": data.get("Role"),
            "source": data.get("Source"),
            "manufacturers": data.get("Manufacturers") or _split_manufacturer(data.get("Manufacturer")),
            "raw_equipment_refs": _extract_equipment_refs(data, unit_type),
            "raw_equipment_mounts": _extract_equipment_mounts(data, unit_type),
            "raw_quirks": data.get("Quirks") or [],
            "source_path": str(p),
        }
        rec.update(_extract_base_stats(data, unit_type))
        records.append(rec)

    return records, issues


def _extract_base_stats(data: dict, unit_type: str) -> dict[str, Any]:
    """Per-unit-type base movement + armor stats (used by `uaw-base-ranges`).

    Returns a dict of fields to merge into the unit record. All values may be
    `None` when the source file omits them.
    """
    if unit_type == "mech":
        return {
            "walk_mp":     extract_walk_mp(data),
            "jump_mp":     extract_jump_mp(data),
            "armor_total": extract_armor_total(data),
        }
    if unit_type == "vehicle":
        return {
            "cruise_mp":   extract_cruise_mp(data),
            "armor_total": extract_armor_total(data),
        }
    if unit_type == "aerospace":
        return {
            "safe_thrust": extract_safe_thrust(data),
            "armor_total": extract_armor_total(data),
        }
    if unit_type == "infantry":
        mp, mode = extract_infantry_movement(data)
        return {
            "movement_points": mp,
            "movement_mode":   mode,
        }
    return {}


def _split_tech_field(combined: Any) -> str | None:
    """Vehicles/aerospace use 'Tech Base / Rules Level: IS Level 1' format."""
    if not isinstance(combined, str):
        return None
    parts = combined.split()
    if not parts:
        return None
    if parts[0].lower() == "is":
        return "Inner Sphere"
    if parts[0].lower() == "clan":
        return "Clan"
    if parts[0].lower() == "mixed":
        return "Mixed"
    return parts[0]


def _split_rules_level(combined: Any) -> int | None:
    if not isinstance(combined, str):
        return None
    import re as _re
    m = _re.search(r"level\s*(\d+)", combined, _re.IGNORECASE)
    return int(m.group(1)) if m else None


def _split_manufacturer(value: Any) -> list[str]:
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        return [m.strip() for m in value.split(",") if m.strip()]
    return []


def _extract_equipment_refs(data: dict, unit_type: str) -> list[str]:
    """Return a flat list of every weapon/equipment reference string in the unit.

    Mech `Equipment` is `[{LocationName: [slot_strings...]}, ...]`.
    Vehicle/Aerospace `Equipment` is `[{LocationName: [item_strings...]}, ...]` (similar shape).
    Infantry units have no Equipment block; their weapon is `Primary Weapon` (a string).
    """
    refs: list[str] = []

    if unit_type == "infantry":
        pw = data.get("Primary Weapon")
        if isinstance(pw, str) and pw and not _is_ammo_text(pw):
            refs.append(pw)
        sw = data.get("Secondary Weapon")
        if isinstance(sw, str) and sw and not _is_ammo_text(sw):
            refs.append(sw)
        return refs

    eq = data.get("Equipment")
    if not isinstance(eq, list):
        return refs
    for loc in eq:
        if not isinstance(loc, dict):
            continue
        for _location_name, slot_list in loc.items():
            if not isinstance(slot_list, list):
                continue
            for slot in slot_list:
                if isinstance(slot, str) and slot and not _is_ammo_text(slot):
                    refs.append(slot)
    return refs


def _extract_equipment_mounts(data: dict, unit_type: str) -> list[dict]:
    """Like :func:`_extract_equipment_refs` but preserves mount-location info.

    Only emitted for vehicle / aerospace records (mechs don't need it for
    Arc(Front) trait derivation). Each entry is ``{"ref": str, "location": str}``.
    Returns an empty list for mechs and infantry.
    """
    if unit_type not in ("vehicle", "aerospace"):
        return []
    eq = data.get("Equipment")
    if not isinstance(eq, list):
        return []
    out: list[dict] = []
    for loc in eq:
        if not isinstance(loc, dict):
            continue
        for location_name, slot_list in loc.items():
            if not isinstance(slot_list, list):
                continue
            for slot in slot_list:
                if isinstance(slot, str) and slot and not _is_ammo_text(slot):
                    out.append({"ref": slot, "location": location_name})
    return out


# --- Top-level orchestrator ------------------------------------------------

def build_all_indices(
    data_dir: Path,
    index_dir: Path,
) -> tuple[dict, AliasIndex, list[Issue]]:
    """Build every index file. Returns (summary, alias_index, issues)."""
    issues: list[Issue] = []

    equipment_records, eq_issues = build_equipment_index(data_dir)
    issues.extend(eq_issues)
    write_json(index_dir / "equipment_index.json", equipment_records)

    reference = build_reference_index(data_dir)
    write_json(index_dir / "reference_index.json", reference)

    alias_index = build_alias_index(
        equipment_records,
        equipment_names=reference.get("equipment_names"),
        ammunition=None,  # ammo intentionally excluded from itemization
    )
    write_json(index_dir / "equipment_aliases.json", alias_index.exact)

    unit_summary: dict[str, int] = {}
    unit_records_by_type: dict[str, list[dict]] = {}
    for ut in UNIT_TYPES:
        records, ut_issues = build_unit_index(data_dir, ut)
        issues.extend(ut_issues)
        write_json(index_dir / f"{ut}_index.json", records)
        unit_summary[ut] = len(records)
        unit_records_by_type[ut] = records

    # --- A6: harvest unit-only equipment -----------------------------------
    # Some referenced equipment has no canonical record in weaponsandequipment/.
    # We synthesize one per unique (normalized name, tech_base) pair so that
    # every reference resolves and the gap is visible in a dedicated report.
    synthesized, alias_index = _harvest_unit_only_equipment(
        unit_records_by_type,
        equipment_records,
        alias_index,
        reference.get("equipment_names"),
        None,  # ammo intentionally excluded from itemization
    )
    if synthesized:
        equipment_records.extend(synthesized)
        write_json(index_dir / "equipment_index.json", equipment_records)
        write_json(index_dir / "equipment_aliases.json", alias_index.exact)
        write_json(index_dir / "equipment_synthesized.json", synthesized)

    summary = {
        "equipment_count": len(equipment_records),
        "synthesized_count": len(synthesized),
        "alias_count": len(alias_index.exact),
        "reference_files": list(reference.keys()),
        "units": unit_summary,
    }
    return summary, alias_index, issues


def _harvest_unit_only_equipment(
    unit_records_by_type: dict[str, list[dict]],
    equipment_records: list[dict],
    alias_index: AliasIndex,
    equipment_names: dict | None,
    ammunition: list[dict] | None,
) -> tuple[list[dict], AliasIndex]:
    """Walk every unit's raw_equipment_refs; for each reference that doesn't
    already resolve and isn't structural, synthesize a canonical equipment
    record. Returns (synthesized_records, augmented_alias_index)."""
    from collections import defaultdict

    # group by (normalized_name, tech_base) so we get one record per concept
    discoveries: dict[tuple[str, str | None], dict] = {}
    for ut, records in unit_records_by_type.items():
        for unit in records:
            for raw in unit.get("raw_equipment_refs", []) or []:
                if _is_ammo_text(raw):
                    continue
                parsed = parse_reference(raw)
                if is_structural(parsed):
                    continue
                cid, kind = alias_index.lookup(parsed)
                if cid is not None:
                    continue
                if _is_ammo_text(parsed.normalized_key) or _is_ammo_text(parsed.name):
                    continue
                key = (parsed.normalized_key, parsed.tech_base)
                d = discoveries.get(key)
                if d is None:
                    discoveries[key] = {
                        "name": parsed.name,
                        "tech_base": parsed.tech_base,
                        "raw_examples": [raw],
                        "ref_count": 1,
                        "first_unit_path": unit.get("source_path"),
                        "unit_types": {ut},
                    }
                else:
                    d["ref_count"] += 1
                    d["unit_types"].add(ut)
                    if len(d["raw_examples"]) < 5 and raw not in d["raw_examples"]:
                        d["raw_examples"].append(raw)

    if not discoveries:
        return [], alias_index

    synthesized: list[dict] = []
    for (norm_key, tech), d in sorted(discoveries.items(), key=lambda kv: (kv[0][0], kv[0][1] or "")):
        tech_slug = "is" if d["tech_base"] == "Inner Sphere" else (
            "clan" if d["tech_base"] == "Clan" else "unk"
        )
        cid = f"unit-derived-{tech_slug}-{slugify(norm_key)}"
        synthesized.append({
            "canonical_id": cid,
            "numeric_id": None,
            "display_name": d["name"],
            "mtf_reference": d["name"],
            "category": "unit-derived",
            "tech_base": d["tech_base"],
            "source": "harvested-from-unit-references",
            "ref_count": d["ref_count"],
            "unit_types": sorted(d["unit_types"]),
            "raw_examples": d["raw_examples"],
            "first_unit_path": d["first_unit_path"],
        })

    augmented = build_alias_index(
        equipment_records + synthesized,
        equipment_names=equipment_names,
        ammunition=ammunition,
    )
    return synthesized, augmented
