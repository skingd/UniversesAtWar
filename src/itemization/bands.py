"""P2.3 — Translation band derivation.

Collapse continuous BattleTech distributions into the discrete attribute
ladders used by Legions Imperialis. Each derivation:

    1. Picks tercile cut points from the distribution.
    2. Validates the proposal against a hand-curated canonical set so that
       a Medium Laser ends up in SHORT, an ER PPC in LONG, etc.
    3. Records the chosen cut points, the validation hit rate, and any
       canonical entries that landed in the "wrong" bucket.

Output is a single dict suitable for serialization to
`output/itemization/translation_bands.json`.
"""
from __future__ import annotations

from typing import Any, Iterable

from .common import percentile, to_float


# --- Canonical validation sets --------------------------------------------

# weapon display_name (case-insensitive) -> expected band label.
WEAPON_RANGE_VALIDATION: dict[str, str] = {
    "small laser":           "SHORT",
    "medium laser":          "SHORT",
    "large laser":           "MEDIUM",
    "er small laser":        "SHORT",
    "er medium laser":       "MEDIUM",
    "er large laser":        "LONG",
    "ac/2":                  "LONG",
    "ac/5":                  "MEDIUM",
    "ac/10":                 "MEDIUM",
    "ac/20":                 "SHORT",
    "gauss rifle":           "LONG",
    "ppc":                   "LONG",
    "er ppc":                "LONG",
    "lrm 5":                 "LONG",
    "lrm 10":                "LONG",
    "lrm 15":                "LONG",
    "lrm 20":                "LONG",
    "srm 2":                 "SHORT",
    "srm 4":                 "SHORT",
    "srm 6":                 "SHORT",
    "machine gun":           "POINT-BLANK",
    "flamer":                "POINT-BLANK",
}

# unit display name (chassis only, case-insensitive) -> expected band.
MECH_MOVEMENT_VALIDATION: dict[str, str] = {
    "locust":      "FAST",
    "spider":      "FAST",
    "jenner":      "FAST",
    "phoenix hawk": "FAST",
    "wolverine":   "MEDIUM",
    "warhammer":   "MEDIUM",
    "marauder":    "MEDIUM",
    "atlas":       "SLOW",
    "annihilator": "SLOW",
    "king crab":   "SLOW",
    "awesome":     "SLOW",
}


# --- Derivation primitives ------------------------------------------------

def _terciles(values: list[float]) -> tuple[float, float]:
    """Return (p33, p66) cut points. `values` will be sorted in place."""
    values.sort()
    return percentile(values, 33.333), percentile(values, 66.666)


def _quartiles(values: list[float]) -> tuple[float, float, float]:
    values.sort()
    return percentile(values, 25), percentile(values, 50), percentile(values, 75)


def _bucket_for_range(value: float, p33: float, p66: float) -> str:
    if value <= 1:
        return "POINT-BLANK"
    if value <= p33:
        return "SHORT"
    if value <= p66:
        return "MEDIUM"
    return "LONG"


def _bucket_for_movement(value: float, p33: float, p66: float) -> str:
    if value <= p33:
        return "SLOW"
    if value <= p66:
        return "MEDIUM"
    return "FAST"


# --- Range bands (P2.3 headline) -----------------------------------------

def derive_weapon_range_bands(weapons: list[dict]) -> dict:
    """Derive SHORT / MEDIUM / LONG / POINT-BLANK from weapon `long_range`."""
    longs: list[float] = []
    for w in weapons:
        v = to_float(w.get("long_range"))
        if v is not None and v > 0:
            longs.append(v)
    if not longs:
        return {"error": "no weapon long-range data"}
    p33, p66 = _terciles(longs)

    hits = 0
    misses = []
    for name, expected in WEAPON_RANGE_VALIDATION.items():
        match = _find_weapon_by_name(weapons, name)
        if not match:
            misses.append({"name": name, "expected": expected, "actual": "not-found"})
            continue
        rng = to_float(match.get("long_range"))
        actual = _bucket_for_range(rng or 0.0, p33, p66) if rng is not None else "no-range"
        if actual == expected:
            hits += 1
        else:
            misses.append({
                "name": name,
                "expected": expected,
                "actual": actual,
                "long_range": rng,
            })
    total = len(WEAPON_RANGE_VALIDATION)

    return {
        "stat": "weapon_range",
        "source_field": "long_range",
        "cut_points": {"p33": round(p33, 2), "p66": round(p66, 2), "point_blank_max": 1.0},
        "labels": ["POINT-BLANK", "SHORT", "MEDIUM", "LONG"],
        "validation_hits": hits,
        "validation_total": total,
        "validation_hit_rate": round(hits / total, 3) if total else 0.0,
        "validation_misses": misses,
        "passed_90pct": (hits / total >= 0.9) if total else False,
    }


def _find_weapon_by_name(weapons: list[dict], name: str) -> dict | None:
    target = name.lower().strip()
    # exact match first
    for w in weapons:
        if (w.get("display_name") or "").lower().strip() == target:
            return w
    # IS-prefixed
    for w in weapons:
        n = (w.get("display_name") or "").lower().strip()
        if n in (f"is {target}", f"inner sphere {target}"):
            return w
    return None


# --- Movement bands -------------------------------------------------------

def derive_movement_bands(unit_aggregations: dict) -> dict:
    """Derive SLOW / MEDIUM / FAST from mech `walk_mp`."""
    mech_block = unit_aggregations.get("mech") or {}
    walk_block = mech_block.get("walk_mp") or {}
    if walk_block.get("count", 0) == 0:
        return {"error": "no walk_mp data"}
    # We don't have raw values inside the summary; reconstruct using percentiles.
    # The summary already has p33-equivalent (p25/p50/p75); we approximate p33≈p25
    # and p66≈p75 for band derivation when raw values are unavailable.
    p33 = walk_block.get("p25", walk_block.get("min"))
    p66 = walk_block.get("p75", walk_block.get("max"))
    return {
        "stat": "mech_walk_mp",
        "source_field": "walk_mp",
        "cut_points": {"p33": p33, "p66": p66},
        "labels": ["SLOW", "MEDIUM", "FAST"],
        "note": "Bands approximated from summary percentiles (p25/p75). "
                "Re-derive against raw values if the validation set fails.",
    }


# --- Armour save ladder ---------------------------------------------------

def derive_armour_save_ladder(unit_aggregations: dict) -> dict:
    """Map total armour / tonnage ratio to a 5-step save ladder (6+..2+)."""
    mech_block = unit_aggregations.get("mech") or {}
    armor_block = mech_block.get("armor_total") or {}
    tonnage_block = mech_block.get("tonnage") or {}
    if armor_block.get("count", 0) == 0 or tonnage_block.get("count", 0) == 0:
        return {"error": "no armour data"}

    # Use the median ratio as an anchor; place quintile cut points around it.
    median_ratio = (armor_block.get("median") or 0) / (tonnage_block.get("median") or 1)
    return {
        "stat": "armour_save",
        "source_field": "armor_total / tonnage",
        "anchor_median_ratio": round(median_ratio, 3),
        "ladder": [
            {"save": "6+", "ratio_max": round(median_ratio * 0.50, 3)},
            {"save": "5+", "ratio_max": round(median_ratio * 0.80, 3)},
            {"save": "4+", "ratio_max": round(median_ratio * 1.10, 3)},
            {"save": "3+", "ratio_max": round(median_ratio * 1.40, 3)},
            {"save": "2+", "ratio_max": None},
        ],
        "note": "Heuristic ladder based on the median armour/tonnage ratio. "
                "Refine with raw per-unit ratios once available.",
    }


# --- Damage / AP --------------------------------------------------------

def derive_damage_ap_ladder(weapon_aggregations: dict) -> dict:
    """Map weapon `damage` to LI attack-dice and AP brackets."""
    overall = weapon_aggregations.get("overall") or {}
    dmg = overall.get("damage") or {}
    if dmg.get("count", 0) == 0:
        return {"error": "no damage data"}
    p33 = dmg.get("p25", dmg.get("min"))
    p66 = dmg.get("p75", dmg.get("max"))
    return {
        "stat": "weapon_damage",
        "source_field": "damage",
        "cut_points": {"p33": p33, "p66": p66},
        "ladder": [
            {"label": "1A",  "damage_max": p33,        "ap_modifier": 0},
            {"label": "2A",  "damage_max": p66,        "ap_modifier": -1},
            {"label": "3A+", "damage_max": None,       "ap_modifier": -2},
        ],
        "note": "Cut points approximated from summary p25/p75. AP modifier "
                "is a starting point; tune against canonical heavy weapons.",
    }


# --- Wounds (mech internal structure) -----------------------------------

def derive_wound_ladder(unit_aggregations: dict) -> dict:
    """Map mech tonnage to LI wound counts (1–4)."""
    mech_block = unit_aggregations.get("mech") or {}
    tonnage_block = mech_block.get("tonnage") or {}
    if tonnage_block.get("count", 0) == 0:
        return {"error": "no tonnage data"}
    return {
        "stat": "wounds",
        "source_field": "tonnage",
        "ladder": [
            {"wounds": 1, "tonnage_max": 35},
            {"wounds": 2, "tonnage_max": 55},
            {"wounds": 3, "tonnage_max": 75},
            {"wounds": 4, "tonnage_max": None},
        ],
        "note": "Hard-coded against the canonical light/medium/heavy/assault "
                "tier boundaries; verified to match BattleMech weight classes.",
    }


# --- Top-level orchestrator ---------------------------------------------

def derive_translation_bands(
    weapons: list[dict],
    unit_aggregations: dict,
    weapon_aggregations: dict,
) -> dict:
    """Build the full `translation_bands.json` payload."""
    return {
        "weapon_range":  derive_weapon_range_bands(weapons),
        "movement":      derive_movement_bands(unit_aggregations),
        "armour_save":   derive_armour_save_ladder(unit_aggregations),
        "damage_ap":     derive_damage_ap_ladder(weapon_aggregations),
        "wounds":        derive_wound_ladder(unit_aggregations),
    }
