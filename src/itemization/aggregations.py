"""Part 2 — Capability aggregation.

Computes distribution blocks (`min/max/mean/median/std/percentiles/histogram`)
for every numeric capability that drives the BattleTech → Legions Imperialis
translation, sliced by tech base / era bucket / unit tier.

Two entry points:
    * ``aggregate_units(unit_indices, raw_unit_files)``
    * ``aggregate_weapons(weapons_catalogue)``

`raw_unit_files` is optional. When present it should be a mapping
``{unit_type: [(parsed_dict, source_path), ...]}`` of the original unit JSON /
YAML blobs (the same shape `datacheck.cli` builds), which lets us pull richer
numeric stats than the canonical index records carry. When absent we fall
back to whatever stats are already on the index records (tonnage, era,
tech_base) — useful for environments where the source corpus isn't available.
"""
from __future__ import annotations

import math
from collections import defaultdict
from typing import Any, Iterable

from src.datacheck.stats import (
    extract_armor_total as _extract_armor_total,
    extract_engine_rating as _extract_engine_rating,
    extract_heat_sink_count as _extract_heat_sink_count,
    extract_jump_mp as _extract_jump_mp,
    extract_run_mp as _extract_run_mp,
)

from .common import categorical_counts, summarize, to_float, to_int


# --- Era buckets -----------------------------------------------------------

ERA_BUCKETS: list[tuple[str, int, int]] = [
    ("age-of-war",       2005, 2570),  # 2005 = Terran Alliance founding era safety floor
    ("star-league",      2571, 2780),
    ("succession-wars",  2781, 3049),
    ("clan-invasion",    3050, 3061),
    ("civil-war",        3062, 3067),
    ("jihad",            3068, 3080),
    ("dark-age",         3081, 3150),
    ("ilclan",           3151, 3300),
]


def era_bucket(year: Any) -> str:
    y = to_int(year)
    if y is None:
        return "unknown"
    for label, lo, hi in ERA_BUCKETS:
        if lo <= y <= hi:
            return label
    return "unknown"


# --- Mech tier classification ---------------------------------------------

def mech_tier(tonnage: Any) -> str:
    t = to_float(tonnage)
    if t is None:
        return "unknown"
    if t <= 35:
        return "light"
    if t <= 55:
        return "medium"
    if t <= 75:
        return "heavy"
    if t <= 100:
        return "assault"
    return "superheavy"


def vehicle_tier(tonnage: Any) -> str:
    t = to_float(tonnage)
    if t is None:
        return "unknown"
    if t <= 30:
        return "light"
    if t <= 60:
        return "medium"
    if t <= 100:
        return "heavy"
    return "assault"


def aerospace_tier(tonnage: Any) -> str:
    t = to_float(tonnage)
    if t is None:
        return "unknown"
    if t <= 35:
        return "light"
    if t <= 70:
        return "medium"
    if t <= 100:
        return "heavy"
    return "superheavy"


_TIER_FOR = {
    "mech": mech_tier,
    "vehicle": vehicle_tier,
    "aerospace": aerospace_tier,
}


# --- Field extraction from raw unit blobs ---------------------------------
#
# The actual extractors live in `src.datacheck.stats` so the index builder
# can persist them. The `_extract_*` aliases above keep this module's
# internal call sites stable.

def _equipment_ref_count(unit_record: dict) -> int:
    return len(unit_record.get("raw_equipment_refs") or [])


# --- Top-level aggregations -----------------------------------------------

def aggregate_units(
    unit_indices: dict[str, list[dict]],
    raw_unit_files: dict[str, list[tuple[Any, str]]] | None = None,
) -> dict:
    """Produce P2.1 distribution blocks for every unit type."""
    raw_unit_files = raw_unit_files or {}
    out: dict[str, dict] = {}
    for ut, units in unit_indices.items():
        builder = _UNIT_BUILDERS.get(ut, _aggregate_generic)
        out[ut] = builder(units, raw_unit_files.get(ut, []))
    return out


def _aggregate_generic(units: list[dict], raw: list) -> dict:
    """Fallback: aggregate only the fields present on every index record."""
    return {
        "count": len(units),
        "tonnage": summarize((u.get("tonnage") for u in units), bin_width=5),
        "era": summarize((u.get("era") for u in units), bin_width=50),
        "weapon_ref_count": summarize((_equipment_ref_count(u) for u in units), bin_width=2),
        "tech_base": categorical_counts(u.get("tech_base") for u in units),
        "era_bucket": categorical_counts(era_bucket(u.get("era")) for u in units),
    }


def _aggregate_mechs(units: list[dict], raw: list) -> dict:
    """P2.1 — BattleMechs."""
    by_path = {p: parsed for parsed, p in raw if isinstance(parsed, dict)}
    walk_mp: list[float] = []
    run_mp: list[float] = []
    jump_mp: list[float] = []
    armor_total: list[float] = []
    engine_rating: list[float] = []
    heat_sinks: list[float] = []
    weapon_count = [_equipment_ref_count(u) for u in units]
    quirk_count = [len(u.get("raw_quirks") or []) for u in units]
    by_tier: dict[str, list[float]] = defaultdict(list)

    for u in units:
        parsed = by_path.get(u.get("source_path"))
        tier = mech_tier(u.get("tonnage"))
        by_tier[tier].append(to_float(u.get("tonnage")) or 0.0)
        if not parsed:
            continue
        if (w := to_float(parsed.get("Walk MP"))) is not None:
            walk_mp.append(w)
        if (r := _extract_run_mp(parsed)) is not None:
            run_mp.append(float(r))
        if (j := _extract_jump_mp(parsed)) is not None:
            jump_mp.append(float(j))
        if (a := _extract_armor_total(parsed)) is not None:
            armor_total.append(a)
        if (e := _extract_engine_rating(parsed)) is not None:
            engine_rating.append(e)
        if (h := _extract_heat_sink_count(parsed)) is not None:
            heat_sinks.append(float(h))

    return {
        "count": len(units),
        "tonnage":        summarize((u.get("tonnage") for u in units), bin_width=5),
        "walk_mp":        summarize(walk_mp, bin_width=1),
        "run_mp":         summarize(run_mp, bin_width=1),
        "jump_mp":        summarize(jump_mp, bin_width=1),
        "armor_total":    summarize(armor_total, bin_width=25),
        "engine_rating":  summarize(engine_rating, bin_width=50),
        "heat_sinks":     summarize(heat_sinks, bin_width=2),
        "weapon_ref_count": summarize(weapon_count, bin_width=5),
        "quirk_count":    summarize(quirk_count, bin_width=1),
        "tier":           categorical_counts(mech_tier(u.get("tonnage")) for u in units),
        "tech_base":      categorical_counts(u.get("tech_base") for u in units),
        "era_bucket":     categorical_counts(era_bucket(u.get("era")) for u in units),
        "role":           categorical_counts(u.get("role") for u in units),
        "by_tier_tonnage": {tier: summarize(vals) for tier, vals in by_tier.items()},
    }


def _aggregate_vehicles(units: list[dict], raw: list) -> dict:
    by_path = {p: parsed for parsed, p in raw if isinstance(parsed, dict)}
    cruise: list[float] = []
    flank: list[float] = []
    armor_total: list[float] = []
    crew: list[float] = []
    motion_types: list[str] = []
    weapon_count = [_equipment_ref_count(u) for u in units]

    for u in units:
        parsed = by_path.get(u.get("source_path"))
        if not parsed:
            continue
        if (c := to_float(parsed.get("Cruise MP"))) is not None:
            cruise.append(c)
            flank.append(float(math.ceil(c * 1.5)))
        if (a := _extract_armor_total(parsed)) is not None:
            armor_total.append(a)
        crew_field = parsed.get("Crew")
        if isinstance(crew_field, dict):
            cr = to_float(crew_field.get("size") or crew_field.get("Size"))
        else:
            cr = to_float(crew_field)
        if cr is not None:
            crew.append(cr)
        mt = parsed.get("Motion Type")
        if isinstance(mt, str) and mt:
            motion_types.append(mt)

    return {
        "count": len(units),
        "tonnage":     summarize((u.get("tonnage") for u in units), bin_width=10),
        "cruise_mp":   summarize(cruise, bin_width=1),
        "flank_mp":    summarize(flank, bin_width=1),
        "armor_total": summarize(armor_total, bin_width=25),
        "crew_size":   summarize(crew, bin_width=1),
        "weapon_ref_count": summarize(weapon_count, bin_width=2),
        "motion_type": categorical_counts(motion_types),
        "tier":        categorical_counts(vehicle_tier(u.get("tonnage")) for u in units),
        "tech_base":   categorical_counts(u.get("tech_base") for u in units),
        "era_bucket":  categorical_counts(era_bucket(u.get("era")) for u in units),
    }


def _aggregate_aerospace(units: list[dict], raw: list) -> dict:
    by_path = {p: parsed for parsed, p in raw if isinstance(parsed, dict)}
    safe: list[float] = []
    max_t: list[float] = []
    si: list[float] = []
    armor_total: list[float] = []
    fuel: list[float] = []
    weapon_count = [_equipment_ref_count(u) for u in units]

    for u in units:
        parsed = by_path.get(u.get("source_path"))
        if not parsed:
            continue
        if (s := to_float(parsed.get("Safe Thrust"))) is not None:
            safe.append(s)
        if (m := to_float(parsed.get("Max Thrust"))) is not None:
            max_t.append(m)
        elif s is not None:
            max_t.append(float(math.ceil(s * 1.5)))
        if (i := to_float(parsed.get("Structural Integrity"))) is not None:
            si.append(i)
        if (a := _extract_armor_total(parsed)) is not None:
            armor_total.append(a)
        if (f := to_float(parsed.get("Fuel"))) is not None:
            fuel.append(f)

    return {
        "count": len(units),
        "tonnage":     summarize((u.get("tonnage") for u in units), bin_width=25),
        "safe_thrust": summarize(safe, bin_width=1),
        "max_thrust":  summarize(max_t, bin_width=1),
        "structural_integrity": summarize(si, bin_width=2),
        "armor_total": summarize(armor_total, bin_width=25),
        "fuel":        summarize(fuel, bin_width=50),
        "weapon_ref_count": summarize(weapon_count, bin_width=2),
        "tier":        categorical_counts(aerospace_tier(u.get("tonnage")) for u in units),
        "tech_base":   categorical_counts(u.get("tech_base") for u in units),
        "era_bucket":  categorical_counts(era_bucket(u.get("era")) for u in units),
    }


def _aggregate_infantry(units: list[dict], raw: list) -> dict:
    by_path = {p: parsed for parsed, p in raw if isinstance(parsed, dict)}
    platoon_size: list[float] = []
    motion_types: list[str] = []
    anti_mech = 0

    for u in units:
        parsed = by_path.get(u.get("source_path"))
        if not parsed:
            continue
        platoon = parsed.get("Platoon")
        if isinstance(platoon, dict):
            if (sz := to_float(platoon.get("size") or platoon.get("Size"))) is not None:
                platoon_size.append(sz)
        elif isinstance(platoon, (int, float)):
            platoon_size.append(float(platoon))
        mt = parsed.get("Motion Type")
        if isinstance(mt, str) and mt:
            motion_types.append(mt)
        if parsed.get("Anti-Mech") in (True, "Yes", "yes", "true", "True"):
            anti_mech += 1

    return {
        "count": len(units),
        "platoon_size": summarize(platoon_size, bin_width=4),
        "motion_type":  categorical_counts(motion_types),
        "tech_base":    categorical_counts(u.get("tech_base") for u in units),
        "era_bucket":   categorical_counts(era_bucket(u.get("era")) for u in units),
        "anti_mech_count": anti_mech,
    }


_UNIT_BUILDERS = {
    "mech":      _aggregate_mechs,
    "vehicle":   _aggregate_vehicles,
    "aerospace": _aggregate_aerospace,
    "infantry":  _aggregate_infantry,
}


# --- Weapons aggregation (P2.2) -------------------------------------------

def aggregate_weapons(weapons: list[dict]) -> dict:
    """Compute distribution blocks for every numeric weapon capability."""
    fields = {
        "damage":        ("damage", 1.0),
        "heat":          ("heat", 1.0),
        "min_range":     ("min_range", 1.0),
        "short_range":   ("short_range", 2.0),
        "medium_range":  ("medium_range", 3.0),
        "long_range":    ("long_range", 5.0),
        "extreme_range": ("extreme_range", 5.0),
        "tonnage":       ("tonnage", 1.0),
        "crit_slots":    ("crit_slots", 1.0),
        "ammo_per_ton":  ("ammo_per_ton", 5.0),
    }

    overall: dict[str, dict] = {}
    for label, (field, bin_w) in fields.items():
        overall[label] = summarize((w.get(field) for w in weapons), bin_width=bin_w)

    # derived
    derived = {
        "damage_per_heat": [],
        "damage_per_ton": [],
        "damage_per_crit": [],
        "range_total": [],
    }
    for w in weapons:
        d = to_float(w.get("damage"))
        h = to_float(w.get("heat"))
        t = to_float(w.get("tonnage"))
        c = to_float(w.get("crit_slots"))
        s = to_float(w.get("short_range")) or 0.0
        m = to_float(w.get("medium_range")) or 0.0
        l = to_float(w.get("long_range")) or 0.0
        if d is not None and h is not None and h > 0:
            derived["damage_per_heat"].append(d / h)
        if d is not None and t is not None and t > 0:
            derived["damage_per_ton"].append(d / t)
        if d is not None and c is not None and c > 0:
            derived["damage_per_crit"].append(d / c)
        if (s + m + l) > 0:
            derived["range_total"].append(s + m + l)

    overall_derived = {k: summarize(v) for k, v in derived.items()}

    by_category: dict[str, dict] = defaultdict(dict)
    for w in weapons:
        cat = w.get("category") or "unknown"
        by_category[cat].setdefault("_weapons", []).append(w)
    by_category_out: dict[str, dict] = {}
    for cat, payload in by_category.items():
        wlist = payload["_weapons"]
        by_category_out[cat] = {
            "count": len(wlist),
            "damage":     summarize((w.get("damage") for w in wlist), bin_width=1),
            "heat":       summarize((w.get("heat") for w in wlist), bin_width=1),
            "long_range": summarize((w.get("long_range") for w in wlist), bin_width=5),
            "tonnage":    summarize((w.get("tonnage") for w in wlist), bin_width=1),
        }

    by_subcategory: dict[str, list[dict]] = defaultdict(list)
    for w in weapons:
        by_subcategory[w.get("subcategory") or "unknown"].append(w)
    by_subcategory_out: dict[str, dict] = {}
    for sub, wlist in by_subcategory.items():
        by_subcategory_out[sub] = {
            "count": len(wlist),
            "damage":     summarize((w.get("damage") for w in wlist), bin_width=1),
            "long_range": summarize((w.get("long_range") for w in wlist), bin_width=5),
            "tonnage":    summarize((w.get("tonnage") for w in wlist), bin_width=1),
            "heat":       summarize((w.get("heat") for w in wlist), bin_width=1),
        }

    by_tech_base = categorical_counts(w.get("tech_base") for w in weapons)
    by_category_count = categorical_counts(w.get("category") for w in weapons)
    by_subcategory_count = categorical_counts(w.get("subcategory") for w in weapons)

    return {
        "count": len(weapons),
        "overall": overall,
        "derived": overall_derived,
        "by_category": by_category_out,
        "by_subcategory": by_subcategory_out,
        "tech_base_counts": by_tech_base,
        "category_counts": by_category_count,
        "subcategory_counts": by_subcategory_count,
    }
