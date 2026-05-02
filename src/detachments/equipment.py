"""Partition raw unit equipment refs into weapons vs. equipment, and
synthesize the special-rules list for the detachment record.

Per the design doc:
* Drop ammo references entirely (they're upgrades, not standing rules).
* Drop bare structural / armor materials (Ferro-Fibrous, Endo Steel …)
  that are mechanical components, not gameplay rules.
* Pass the remaining named items through as-is, deduplicated.
"""
from __future__ import annotations

from typing import Iterable, Optional

from src.datacheck.alias_resolver import (
    AliasIndex,
    is_structural,
    parse_reference,
)
from src.detachments.weapons import WeaponIndex


# Substrings (case-insensitive) that mark a ref as a structural/armor item
# we never want surfaced in special_rules.
_DROP_SUBSTRINGS: tuple[str, ...] = (
    "ferro-fibrous",
    "ferro fibrous",
    "ferrofibrous",
    "endo steel",
    "endo-steel",
    "endosteel",
    "endo composite",
    "endo-composite",
    "ferro-lamellor",
    "stealth armor",
    "reactive armor",
    "reflective armor",
    "hardened armor",
    "patchwork armor",
)


def _is_drop_equipment(name: str) -> bool:
    n = name.lower()
    if "ammo" in n or "ammunition" in n:
        return True
    return any(token in n for token in _DROP_SUBSTRINGS)


def partition_refs(
    raw_refs: Iterable[str],
    weapon_index: WeaponIndex,
    alias_index: Optional[AliasIndex] = None,
) -> tuple[list[str], list[str]]:
    """Return ``(weapon_refs, equipment_refs)``.

    ``weapon_refs`` retains the **raw** strings that resolved to a weapon
    profile (preserving order and per-installation duplication so the
    assembler can emit one row per gun).

    ``equipment_refs`` contains the raw strings that did NOT resolve as
    weapons and are not ammo/structural — i.e. things like CASE, TAG,
    A-Pod, Heat Sink, etc. Order preserved; duplicates kept (assembler
    dedups for special_rules).
    """
    weapon_refs: list[str] = []
    equipment_refs: list[str] = []
    for ref in raw_refs:
        if not isinstance(ref, str) or not ref.strip():
            continue
        prof, kind = weapon_index.resolve(ref, alias_index=alias_index)
        if prof is not None:
            weapon_refs.append(ref)
            continue
        if kind == "ammo":
            continue
        # Either structural or unmapped weapon — but unmapped weapons should
        # still appear in weapon_refs so the assembler can emit them with
        # `unmapped: true`. Use parse_reference + is_structural to split.
        parsed = parse_reference(ref)
        if is_structural(parsed):
            continue
        if parsed.is_ammo:
            continue
        # Heuristic: if the ref's normalized name contains "laser", "ppc",
        # "cannon", "missile", "gauss", "rifle", "mortar", "machine gun",
        # "ac/", "lrm", "srm", "atm", "lb ", "uac", "mml", treat as a
        # weapon (unmapped). Otherwise classify as equipment.
        nk = parsed.normalized_key
        if _looks_like_weapon(nk):
            weapon_refs.append(ref)
        else:
            equipment_refs.append(ref)
    return weapon_refs, equipment_refs


_WEAPON_HINT_TOKENS: tuple[str, ...] = (
    "laser", "ppc", "autocannon", "ac/", "ac ", "gauss", "rifle",
    "missile", "lrm", "srm", "mml", "atm", "mrm", "rl ", "rl-",
    "rocket launcher", "mortar", "machine gun", "machinegun", "mg",
    "uac", "lb ", "lb-", "hag", "arrow iv", "thunderbolt", "narc",
    "tag", "flamer", "plasma", "snub", "snub-nose", "bombard",
)


def _looks_like_weapon(normalized: str) -> bool:
    if not normalized:
        return False
    return any(tok in normalized for tok in _WEAPON_HINT_TOKENS)


def special_rules_from_equipment(equipment_refs: Iterable[str]) -> list[str]:
    """Dedup + clean equipment refs into the ``special_rules`` list.

    Strips tech suffixes/prefixes via parse_reference, then preserves
    first-seen order. Drops items whose normalized form is empty or that
    match one of the structural / ammo drop rules (defense in depth — the
    caller should already have filtered these via :func:`partition_refs`).
    """
    out: list[str] = []
    seen: set[str] = set()
    for ref in equipment_refs:
        if not isinstance(ref, str):
            continue
        parsed = parse_reference(ref)
        name = parsed.name.strip()
        if not name:
            continue
        if _is_drop_equipment(name):
            continue
        key = name.casefold()
        if key in seen:
            continue
        seen.add(key)
        out.append(name)
    return out
