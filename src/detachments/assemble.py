"""Assemble per-unit detachment records.

Stitches together translation tables, the weapon catalogue, and equipment
passthrough into the final schema documented in ``plans/units.prompt.md``.

Per the design spec, weapon and ammo profiles are **not** hardcoded into
the detachment JSON. Each weapon entry is a **link** (a name that the
document generator joins to ``data/WeaponRules.csv`` at render time) plus
a ``traits_added`` list capturing per-mount-location dynamic traits like
``Arc(Front)`` for vehicle/aerospace hull mounts.

The hardcoded ``weapons_bulleted`` field carries the human-readable
bullet list (e.g. ``"Two Inner Sphere LRM 20"``). It is hardcoded because
this prose is stable text — only the per-profile rule data is volatile.
"""
from __future__ import annotations

from collections import Counter
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


# --- Arc(Front) derivation -------------------------------------------------

def _is_turret_location(location: Optional[str]) -> bool:
    if not location:
        return False
    return "turret" in location.lower()


def _is_bomb(name: str) -> bool:
    """Bombs are exempt from Arc(Front). Detect by name token."""
    return "bomb" in (name or "").lower()


def _arc_front_traits(
    unit_type: str,
    location: Optional[str],
    weapon_name: str,
) -> list[str]:
    """Return ``["Arc(Front)"]`` if this mount auto-gains Arc(Front), else ``[]``.

    Per ``design/units-translation.md``: vehicle hull mounts (anything not
    a turret) and aerospace fighter weapons all gain Arc(Front), with
    bombs and turret-mounted weapons exempt.
    """
    if unit_type not in ("vehicle", "aerospace"):
        return []
    if _is_turret_location(location):
        return []
    if _is_bomb(weapon_name):
        return []
    return ["Arc(Front)"]


# --- Weapon link entry -----------------------------------------------------

def _weapon_link(
    raw_ref: str,
    profile: Optional[WeaponProfile],
    location: Optional[str],
    unit_type: str,
) -> dict:
    """Build a *link-only* weapon entry. Profile data is **not** embedded."""
    name = profile.name if profile is not None else raw_ref
    return {
        "name": name,
        "raw_ref": raw_ref,
        "mount_location": location,
        "traits_added": _arc_front_traits(unit_type, location, name),
        "unmapped": profile is None,
    }


# --- Bulleted list ---------------------------------------------------------

_NUMBER_WORDS: dict[int, str] = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
    11: "Eleven", 12: "Twelve",
}


def _count_word(n: int) -> str:
    return _NUMBER_WORDS.get(n, str(n))


def _pluralize(name: str) -> str:
    """Append ``s`` only when the name ends in a letter — keeps tokens like
    ``LRM 20`` unchanged while pluralizing ``Medium Laser`` → ``Medium Lasers``.
    """
    if not name:
        return name
    return name + "s" if name[-1].isalpha() else name


def _bullet_list(weapon_links: list[dict]) -> list[str]:
    """Aggregate weapon links by name (first-occurrence order) and produce
    a list of strings like ``"Two Inner Sphere LRM 20"``.

    Singletons render as bare names per the design example, which only
    shows count words for multiples.
    """
    counts: dict[str, int] = {}
    order: list[str] = []
    for w in weapon_links:
        name = w["name"]
        if name not in counts:
            counts[name] = 0
            order.append(name)
        counts[name] += 1

    out: list[str] = []
    for name in order:
        n = counts[name]
        if n == 1:
            out.append(name)
        else:
            out.append(f"{_count_word(n)} {_pluralize(name)}")
    return out


# --- Upgrade options -------------------------------------------------------

def _detachment_size_options(base: int, max_size: int) -> list[dict]:
    if max_size <= base:
        return []
    return [{"size": n, "points": None} for n in range(base + 1, max_size + 1)]


def _special_ammo_links(
    weapon_names: Iterable[str],
    ammo_index: dict[str, list[AmmoOption]],
) -> list[dict]:
    """Link-only union of ammo options for the unique weapon names present.

    Each entry is just ``{ammo_name, weapon_name, points}`` — the renderer
    joins to ``AmmunitionRules.csv`` for full profile data at document time.
    """
    out: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for wname in weapon_names:
        for opt in ammo_index.get(wname, []):
            key = (opt.weapon_name, opt.name)
            if key in seen:
                continue
            seen.add(key)
            out.append({
                "ammo_name": opt.name,
                "weapon_name": opt.weapon_name,
                "points": opt.points,
            })
    return out


# --- Mount iteration -------------------------------------------------------

def _iter_mounts(record: dict) -> list[tuple[str, Optional[str]]]:
    """Yield ``(ref, location)`` pairs for every weapon/equipment install.

    Prefer the structured ``raw_equipment_mounts`` field (vehicle/aerospace)
    when present; otherwise fall back to ``raw_equipment_refs`` with
    ``location=None`` (mechs, infantry).
    """
    mounts = record.get("raw_equipment_mounts")
    if isinstance(mounts, list) and mounts:
        out: list[tuple[str, Optional[str]]] = []
        for m in mounts:
            if isinstance(m, dict):
                ref = m.get("ref")
                if isinstance(ref, str) and ref:
                    out.append((ref, m.get("location")))
        return out
    refs = record.get("raw_equipment_refs") or []
    return [(r, None) for r in refs if isinstance(r, str) and r]


# --- Build -----------------------------------------------------------------

def build_detachment(
    record: dict,
    weapon_index: WeaponIndex,
    ammo_index: dict[str, list[AmmoOption]],
    alias_index: Optional[AliasIndex],
    coverage: Coverage,
) -> Optional[dict]:
    """Build a single detachment dict from an index record."""
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
        base_max = (1, 1)
    base, max_size = base_max

    # Walk mounts (preserves location for vehicle/aerospace) and partition.
    mounts = _iter_mounts(record)
    raw_refs = [ref for ref, _loc in mounts]
    weapon_refs, equipment_refs = partition_refs(raw_refs, weapon_index, alias_index)

    # Re-walk mounts in order, consuming each weapon ref occurrence to
    # preserve duplicate counts and keep mount locations aligned.
    weapon_links: list[dict] = []
    seen_weapon_names: list[str] = []
    seen_set: set[str] = set()
    remaining = Counter(weapon_refs)
    for ref, loc in mounts:
        if remaining.get(ref, 0) <= 0:
            continue
        remaining[ref] -= 1
        prof, _kind = weapon_index.resolve(ref, alias_index=alias_index)
        link = _weapon_link(ref, prof, loc, unit_type)
        weapon_links.append(link)
        if link["unmapped"]:
            coverage.unmapped_weapons[link["name"]] = (
                coverage.unmapped_weapons.get(link["name"], 0) + 1
            )
        if link["name"] not in seen_set:
            seen_set.add(link["name"])
            seen_weapon_names.append(link["name"])

    bulleted = _bullet_list(weapon_links)
    special_rules = special_rules_from_equipment(equipment_refs)
    special_ammo = _special_ammo_links(seen_weapon_names, ammo_index)
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
        "weapons_bulleted": bulleted,
        "weapons": weapon_links,
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
