"""Translation tables from `design/units-translation.md`.

Pure data + lookup helpers. No I/O.
"""
from __future__ import annotations

from typing import Optional

from src.datacheck.stats import to_float, to_int

# --- Armor save -----------------------------------------------------------

# (max_armor, save). Inclusive upper bound; final entry uses inf.
_MECH_ARMOR: list[tuple[float, str]] = [
    (99,  "5+"),
    (299, "4+"),
    (400, "3+"),
    (float("inf"), "2+"),
]
_VEH_AERO_ARMOR: list[tuple[float, str]] = [
    (20,  "5+"),
    (80,  "4+"),
    (250, "3+"),
    (300, "2+"),
    (float("inf"), "1+"),
]


def armor_save(armor_total, unit_type: str) -> Optional[str]:
    """Return e.g. ``"3+"`` for the unit's armor total, or ``None`` if the
    armor value is missing/unparseable."""
    a = to_float(armor_total)
    if a is None:
        return None
    table = _MECH_ARMOR if unit_type == "mech" else _VEH_AERO_ARMOR
    for cap, save in table:
        if a <= cap:
            return save
    return None  # unreachable; final inf catches all


# --- Movement -------------------------------------------------------------

# Sparse maps lifted verbatim from design/units-translation.md. Note both
# the mech and aerospace tables skip speed `13`; the resolver below falls
# back to the next-lower entry and the caller logs a warning.

_MECH_MOVEMENT: dict[int, str] = {
    2: "4\"",  3: "5\"",  4: "6\"",  5: "7\"",  6: "8\"",
    7: "9\"",  8: "10\"", 9: "11\"", 10: "12\"", 11: "13\"",
    12: "14\"", 14: "15\"", 15: "16\"", 16: "17\"",
}
_AEROSPACE_MOVEMENT: dict[int, str] = {
    2: "18\"", 3: "19\"", 4: "20\"", 5: "21\"", 6: "22\"",
    7: "23\"", 8: "24\"", 9: "25\"", 10: "26\"", 11: "27\"",
    12: "28\"", 14: "29\"", 15: "30\"",
}
_VEHICLE_MOVEMENT: dict[int, str] = {
    2: "4\"",  3: "5\"",  4: "6\"",  5: "7\"",  6: "8\"",
    7: "9\"",  8: "10\"", 9: "11\"", 10: "12\"", 11: "13\"",
    12: "14\"", 14: "15\"", 15: "16\"", 16: "17\"", 17: "18\"",
    18: "19\"",
}

_MOVEMENT_TABLES: dict[str, dict[int, str]] = {
    "mech":      _MECH_MOVEMENT,
    "vehicle":   _VEHICLE_MOVEMENT,
    "aerospace": _AEROSPACE_MOVEMENT,
}


def movement_inches(speed, unit_type: str) -> tuple[Optional[str], bool]:
    """Look up movement for a base speed.

    Returns ``(movement, exact)``. ``exact`` is False when the speed had to
    be rounded down to the nearest defined entry (e.g. mech speed 13 →
    speed 12's row); the caller should record the gap in coverage.
    Returns ``(None, False)`` when speed is missing or below the lowest row.
    """
    s = to_int(speed)
    if s is None:
        return None, False
    table = _MOVEMENT_TABLES.get(unit_type)
    if table is None:
        return None, False
    if s in table:
        return table[s], True
    # Speed above max — clamp to max row.
    max_key = max(table)
    if s > max_key:
        return table[max_key], False
    # Gap (e.g. 13 in mech): fall back to next-lower defined key.
    lower = max((k for k in table if k < s), default=None)
    if lower is None:
        return None, False
    return table[lower], False


# --- Tonnage tier ladders -------------------------------------------------
#
# (max_tons, label). Inclusive upper bound; final entry uses inf.
_MECH_TIERS: list[tuple[float, str]] = [
    (35, "light"), (55, "medium"), (75, "heavy"), (100, "assault"),
    (float("inf"), "superheavy"),
]
_VEHICLE_TIERS: list[tuple[float, str]] = [
    (30, "light"), (60, "medium"), (100, "heavy"),
    (float("inf"), "assault"),
]
_AEROSPACE_TIERS: list[tuple[float, str]] = [
    (35, "light"), (70, "medium"), (100, "heavy"),
    (float("inf"), "superheavy"),
]

_TIER_TABLES: dict[str, list[tuple[float, str]]] = {
    "mech":      _MECH_TIERS,
    "vehicle":   _VEHICLE_TIERS,
    "aerospace": _AEROSPACE_TIERS,
}


def tier(tonnage, unit_type: str) -> Optional[str]:
    t = to_float(tonnage)
    if t is None:
        return None
    table = _TIER_TABLES.get(unit_type)
    if table is None:
        return None
    for cap, label in table:
        if t <= cap:
            return label
    return None


# --- Wounds ---------------------------------------------------------------

_WOUNDS: dict[str, dict[str, int]] = {
    "mech":      {"light": 2, "medium": 4, "heavy": 6, "assault": 8, "superheavy": 8},
    "vehicle":   {"light": 1, "medium": 2, "heavy": 3, "assault": 4},
    "aerospace": {"light": 1, "medium": 2, "heavy": 3, "superheavy": 4},
}


def wounds(tonnage, unit_type: str) -> Optional[int]:
    t = tier(tonnage, unit_type)
    if t is None:
        return None
    return _WOUNDS.get(unit_type, {}).get(t)


# --- Scale ---------------------------------------------------------------

_SCALE: dict[str, dict[str, int]] = {
    "mech":      {"light": 2, "medium": 3, "heavy": 3, "assault": 4, "superheavy": 4},
    "vehicle":   {"light": 1, "medium": 2, "heavy": 2, "assault": 3},
    "aerospace": {"light": 2, "medium": 2, "heavy": 2, "superheavy": 2},
}


def scale(tonnage, unit_type: str) -> Optional[int]:
    t = tier(tonnage, unit_type)
    if t is None:
        return None
    return _SCALE.get(unit_type, {}).get(t)


# --- Detachment size ------------------------------------------------------

# Mechs: always 1 per detachment regardless of tier / tech base.
# Vehicles / aerospace: per-tier (base, max), keyed by tech base.

_DETACHMENT_SIZE_VEHICLE: dict[str, dict[str, tuple[int, int]]] = {
    "Inner Sphere": {
        "light":   (4, 12),
        "medium":  (4, 12),
        "heavy":   (4, 12),
        "assault": (1, 4),
    },
    "Clan": {
        "light":   (5, 15),
        "medium":  (5, 15),
        "heavy":   (5, 15),
        "assault": (1, 5),
    },
}

_DETACHMENT_SIZE_AEROSPACE: dict[str, dict[str, tuple[int, int]]] = {
    "Inner Sphere": {
        "light":      (1, 4),
        "medium":     (1, 4),
        "heavy":      (1, 4),
        "superheavy": (1, 1),
    },
    "Clan": {
        "light":      (1, 5),
        "medium":     (1, 5),
        "heavy":      (1, 5),
        "superheavy": (1, 1),
    },
}


def detachment_size(tonnage, unit_type: str, tech_base: str) -> Optional[tuple[int, int]]:
    if unit_type == "mech":
        return (1, 1)
    t = tier(tonnage, unit_type)
    if t is None:
        return None
    if unit_type == "vehicle":
        return _DETACHMENT_SIZE_VEHICLE.get(tech_base, {}).get(t)
    if unit_type == "aerospace":
        return _DETACHMENT_SIZE_AEROSPACE.get(tech_base, {}).get(t)
    return None


# --- Detachment label -----------------------------------------------------
#
# IS labels are taken verbatim from design/units-translation.md ("Vehicle
# Lance", "Aerospace Lance"). Clan equivalents follow BattleTech canon
# ("Star" instead of "Lance"). Mechs are always "BattleMech".

def detachment_label(unit_type: str, tech_base: str) -> str:
    if unit_type == "mech":
        return "BattleMech"
    suffix = "Star" if tech_base == "Clan" else "Lance"
    if unit_type == "vehicle":
        return f"Vehicle {suffix}"
    if unit_type == "aerospace":
        return f"Aerospace {suffix}"
    return unit_type


# --- Unit-type label ------------------------------------------------------

_UNIT_TYPE_LABEL = {
    "mech":      "BattleMech",
    "vehicle":   "Vehicle",
    "aerospace": "Aerospace",
    "infantry":  "Infantry",
}


def unit_type_label(unit_type: str) -> str:
    return _UNIT_TYPE_LABEL.get(unit_type, unit_type)


# --- Movement field per unit type -----------------------------------------

_BASE_SPEED_FIELD: dict[str, str] = {
    "mech":      "walk_mp",
    "vehicle":   "cruise_mp",
    "aerospace": "safe_thrust",
}


def base_speed_field(unit_type: str) -> Optional[str]:
    return _BASE_SPEED_FIELD.get(unit_type)
