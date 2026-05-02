"""Pure-functional aggregation of per-unit base stats into min/max/median
ranges, overall and broken down by tonnage tier.

Inputs are the index records produced by `src.datacheck.index_builder`. No
file I/O happens here.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Iterable

from src.itemization.aggregations import aerospace_tier, mech_tier, vehicle_tier
from src.itemization.common import summarize

# Per-unit-type configuration:
#   movement_field: name of the movement value on the index record
#   armor_field:    name of the armor total field (None when n/a)
#   tier_fn:        tonnage->tier classifier (None for infantry)
#   tier_label:     human label for tier sections
UNIT_TYPE_CONFIG: dict[str, dict] = {
    "mech": {
        "movement_field": "walk_mp",
        "movement_label": "walk_mp",
        "armor_field": "armor_total",
        "tier_fn": mech_tier,
        "tier_label": "tonnage_tier",
    },
    "vehicle": {
        "movement_field": "cruise_mp",
        "movement_label": "cruise_mp",
        "armor_field": "armor_total",
        "tier_fn": vehicle_tier,
        "tier_label": "tonnage_tier",
    },
    "aerospace": {
        "movement_field": "safe_thrust",
        "movement_label": "safe_thrust",
        "armor_field": "armor_total",
        "tier_fn": aerospace_tier,
        "tier_label": "tonnage_tier",
    },
    "infantry": {
        "movement_field": "movement_points",
        "movement_label": "movement_points",
        "armor_field": None,
        "tier_fn": None,         # infantry tiers by motion mode instead
        "tier_label": "motion_mode",
    },
}


def _summarize_block(records: Iterable[dict], movement_field: str, armor_field: str | None) -> dict:
    """Build `{n, movement, armor}` summary for a record set."""
    records = list(records)
    block: dict = {
        "n": len(records),
        "movement": summarize(r.get(movement_field) for r in records),
    }
    if armor_field:
        block["armor"] = summarize(r.get(armor_field) for r in records)
    return block


def _tier_for(record: dict, cfg: dict) -> str:
    if cfg["tier_fn"] is not None:
        return cfg["tier_fn"](record.get("tonnage"))
    # Infantry: bucket by motion mode (Foot, Tracked, Wheeled, Hover, Jump, ...).
    mode = record.get("movement_mode")
    return mode if isinstance(mode, str) and mode else "unknown"


def compute_unit_type(records: Iterable[dict], unit_type: str) -> dict:
    """Distill one unit type's index into overall + per-tier ranges."""
    if unit_type not in UNIT_TYPE_CONFIG:
        raise ValueError(f"unknown unit_type: {unit_type}")
    cfg = UNIT_TYPE_CONFIG[unit_type]
    records = list(records)

    overall = _summarize_block(records, cfg["movement_field"], cfg["armor_field"])

    by_tier: dict[str, list[dict]] = defaultdict(list)
    for rec in records:
        by_tier[_tier_for(rec, cfg)].append(rec)

    tiers = {
        tier: _summarize_block(recs, cfg["movement_field"], cfg["armor_field"])
        for tier, recs in by_tier.items()
    }

    return {
        "unit_type": unit_type,
        "movement_field": cfg["movement_label"],
        "tier_label": cfg["tier_label"],
        "overall": overall,
        "by_tier": tiers,
    }


def compute_all(indices_by_type: dict[str, list[dict]]) -> dict:
    """Run `compute_unit_type` for every supported unit type that has an
    index. Missing unit types are silently skipped."""
    out: dict[str, dict] = {}
    for ut in UNIT_TYPE_CONFIG:
        recs = indices_by_type.get(ut)
        if recs is None:
            continue
        out[ut] = compute_unit_type(recs, ut)
    return out


def required_field_counts(records: Iterable[dict], unit_type: str) -> dict[str, int]:
    """How many records have non-None values for each required field.

    Used by --strict to detect a stale index that pre-dates the Phase 1
    extension of `build_unit_index`.
    """
    cfg = UNIT_TYPE_CONFIG[unit_type]
    counts = {cfg["movement_field"]: 0}
    if cfg["armor_field"]:
        counts[cfg["armor_field"]] = 0
    for r in records:
        for field in counts:
            if r.get(field) is not None:
                counts[field] += 1
    return counts
