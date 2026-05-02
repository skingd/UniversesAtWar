"""Assemble per-unit detachment records.

Stitches together translation tables, weapon catalogue, and equipment
passthrough into the final schema documented in ``plans/units.prompt.md``.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Optional

from src.datacheck.alias_resolver import AliasIndex
from src.detachments import tables
from src.detachments.equipment import (
    partition_refs,
    special_rules_from_equipment,
)
from src.detachments.weapons import (
    AmmoOption,
    WeaponIndex,
    WeaponProfile,
)


_VALID_TECH_BASES: frozenset[str] = frozenset({"Inner Sphere", "Clan"})


@dataclass
class Coverage:
    """Aggregated stats for a build run."""
    unit_type: str
    total_records: int = 0
    emitted: int = 0
    skipped_unknown_tech_base: int = 0
    skipped_missing_armor: int = 0
    skipped_missing_movement: int = 0
    skipped_missing_tonnage: int = 0
    missing_speed: list[dict] = field(default_factory=list)
    unmapped_weapons: dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "unit_type": self.unit_type,
            "total_records": self.total_records,
            "emitted": self.emitted,
            "skipped_unknown_tech_base": self.skipped_unknown_tech_base,
            "skipped_missing_armor": self.skipped_missing_armor,
            "skipped_missing_movement": self.skipped_missing_movement,
            "skipped_missing_tonnage": self.skipped_missing_tonnage,
            "missing_speed_count": len(self.missing_speed),
            "missing_speed_samples": self.missing_speed[:25],
            "unmapped_weapons_count": len(self.unmapped_weapons),
            "unmapped_weapons_top": sorted(
                self.unmapped_weapons.items(), key=lambda kv: -kv[1],
            )[:50],
        }


def _display_name(record: dict) -> str:
    chassis = str(record.get("chassis") or "").strip()
    model = str(record.get("model") or "").strip()
    if chassis and model:
        return f"{chassis} {model}"
    return chassis or model or record.get("canonical_id") or ""


def _weapon_entry(
    raw_ref: str,
    profile: Optional[WeaponProfile],
) -> dict:
    if profile is not None:
        return {
            "name": profile.name,
            "range": profile.range,
            "dice": profile.dice,
            "to_hit": profile.to_hit,
            "ap": profile.ap,
            "heat": profile.heat,
            "type": profile.type,
            "traits": list(profile.traits),
            "unmapped": False,
            "raw_ref": raw_ref,
        }
    return {
        "name": raw_ref,
        "range": None,
        "dice": None,
        "to_hit": None,
        "ap": None,
        "heat": None,
        "type": None,
        "traits": [],
        "unmapped": True,
        "raw_ref": raw_ref,
    }


def _detachment_size_options(base: int, max_size: int) -> list[dict]:
    """Generate placeholder upgrade entries for every size above the base."""
    if max_size <= base:
        return []
    return [{"size": n, "points": None} for n in range(base + 1, max_size + 1)]


def _special_ammo_options(
    weapon_names: Iterable[str],
    ammo_index: dict[str, list[AmmoOption]],
) -> list[dict]:
    """Union of ammo options for the unique weapon names present, deduped."""
    out: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for wname in weapon_names:
        for opt in ammo_index.get(wname, []):
            key = (opt.weapon_name, opt.name)
            if key in seen:
                continue
            seen.add(key)
            out.append(opt.to_dict())
    return out


def build_detachment(
    record: dict,
    weapon_index: WeaponIndex,
    ammo_index: dict[str, list[AmmoOption]],
    alias_index: Optional[AliasIndex],
    coverage: Coverage,
) -> Optional[dict]:
    """Build a single detachment dict from an index record.

    Returns ``None`` (and increments the appropriate coverage counter) if
    the record lacks a usable tech_base, tonnage, armor, or movement.
    """
    unit_type = record.get("unit_type") or coverage.unit_type
    tech_base = record.get("tech_base")
    if tech_base not in _VALID_TECH_BASES:
        coverage.skipped_unknown_tech_base += 1
        return None

    tonnage = record.get("tonnage")
    if tonnage is None:
        coverage.skipped_missing_tonnage += 1
        return None

    save = tables.armor_save(record.get("armor_total"), unit_type)
    if save is None:
        coverage.skipped_missing_armor += 1
        return None

    speed_field = tables.base_speed_field(unit_type)
    raw_speed = record.get(speed_field) if speed_field else None
    movement, exact = tables.movement_inches(raw_speed, unit_type)
    if movement is None:
        coverage.skipped_missing_movement += 1
        return None
    if not exact:
        coverage.missing_speed.append({
            "unit": _display_name(record),
            "unit_type": unit_type,
            "speed": raw_speed,
            "fallback_movement": movement,
        })

    base_max = tables.detachment_size(tonnage, unit_type, tech_base)
    if base_max is None:
        # Tier resolved but no entry — treat as missing config; do NOT skip
        # entirely (mechs always succeed). Use (1,1) as a safe default.
        base_max = (1, 1)
    base, max_size = base_max

    raw_refs = record.get("raw_equipment_refs") or []
    weapon_refs, equipment_refs = partition_refs(raw_refs, weapon_index, alias_index)

    weapons: list[dict] = []
    weapons_seen_names: list[str] = []
    seen_weapon_names: set[str] = set()
    for ref in weapon_refs:
        prof, kind = weapon_index.resolve(ref, alias_index=alias_index)
        entry = _weapon_entry(ref, prof)
        weapons.append(entry)
        wname = entry["name"]
        if entry["unmapped"]:
            coverage.unmapped_weapons[wname] = coverage.unmapped_weapons.get(wname, 0) + 1
        if wname not in seen_weapon_names:
            seen_weapon_names.add(wname)
            weapons_seen_names.append(wname)

    special_rules = special_rules_from_equipment(equipment_refs)
    special_ammo = _special_ammo_options(weapons_seen_names, ammo_index)
    size_upgrades = _detachment_size_options(base, max_size)

    coverage.emitted += 1
    return {
        "id": record.get("canonical_id") or record.get("key"),
        "name": _display_name(record),
        "detachment": tables.detachment_label(unit_type, tech_base),
        "unit_type": tables.unit_type_label(unit_type),
        "scale": tables.scale(tonnage, unit_type),
        "tier": tables.tier(tonnage, unit_type),
        "tech_base": tech_base,
        "tonnage": tonnage,
        "armor_save": save,
        "movement": movement,
        "wounds": tables.wounds(tonnage, unit_type),
        "detachment_size": {"base": base, "max": max_size},
        "points": None,
        "weapons": weapons,
        "upgrade_options": {
            "special_ammo": special_ammo,
            "detachment_size": size_upgrades,
        },
        "special_rules": special_rules,
        "source_path": record.get("source_path"),
    }


def build_all(
    records: Iterable[dict],
    unit_type: str,
    weapon_index: WeaponIndex,
    ammo_index: dict[str, list[AmmoOption]],
    alias_index: Optional[AliasIndex] = None,
) -> tuple[list[dict], Coverage]:
    coverage = Coverage(unit_type=unit_type)
    out: list[dict] = []
    for rec in records:
        coverage.total_records += 1
        det = build_detachment(rec, weapon_index, ammo_index, alias_index, coverage)
        if det is not None:
            out.append(det)
    return out, coverage
