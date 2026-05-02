"""Shared numeric coercion + base-stat extractors for unit blobs.

Originally lived in `src/itemization/aggregations.py`; promoted here so the
data-check index builder and the base-ranges report can both use them
without the reverse dependency on the itemization package.
"""
from __future__ import annotations

import math
import re
from typing import Any

_NUM_RE = re.compile(r"-?\d+(?:\.\d+)?")


# --- Numeric coercion ------------------------------------------------------

def to_float(value: Any) -> float | None:
    """Best-effort numeric coercion. Returns None for missing / non-numeric."""
    if value is None:
        return None
    if isinstance(value, bool):  # bools are ints in Python; reject
        return None
    if isinstance(value, (int, float)):
        if isinstance(value, float) and math.isnan(value):
            return None
        return float(value)
    if isinstance(value, str):
        s = value.strip()
        if not s or s.upper() in ("NA", "N/A", "VARIABLE", "SPECIAL", "-"):
            return None
        try:
            return float(s)
        except ValueError:
            m = _NUM_RE.search(s)
            return float(m.group(0)) if m else None
    return None


def to_int(value: Any) -> int | None:
    f = to_float(value)
    return int(f) if f is not None else None


# --- Base-stat extractors --------------------------------------------------
#
# These pull the canonical base values out of a parsed unit blob (the dict
# loaded from a Data Files/ JSON or YAML file). They intentionally return
# `None` when the field is missing or non-numeric so the caller can decide
# whether that's a hard error or a soft skip.

def extract_armor_total(parsed: dict) -> float | None:
    """Sum every numeric value under the 'Armor Points' / 'Armor' block."""
    ap = parsed.get("Armor Points")
    if ap is None:
        ap = parsed.get("Armor")
    if ap is None:
        return None
    if isinstance(ap, (int, float)):
        return float(ap)
    if isinstance(ap, dict):
        total = 0.0
        any_numeric = False
        for v in ap.values():
            f = to_float(v)
            if f is not None:
                total += f
                any_numeric = True
        return total if any_numeric else None
    if isinstance(ap, list):
        total = 0.0
        any_numeric = False
        for item in ap:
            if isinstance(item, dict):
                for v in item.values():
                    f = to_float(v)
                    if f is not None:
                        total += f
                        any_numeric = True
            else:
                f = to_float(item)
                if f is not None:
                    total += f
                    any_numeric = True
        return total if any_numeric else None
    return to_float(ap)


def extract_walk_mp(parsed: dict) -> int | None:
    """Mech Walk MP."""
    return to_int(parsed.get("Walk MP") or parsed.get("Walk Mp") or parsed.get("walk_mp"))


def extract_jump_mp(parsed: dict) -> int | None:
    """Mech Jump MP. Returns 0 when the field is explicitly 0; None when absent."""
    for key in ("Jump MP", "Jump Mp", "jump_mp"):
        if key in parsed:
            return to_int(parsed.get(key))
    return None


def extract_run_mp(parsed: dict) -> int | None:
    """Run MP — explicit value, else ⌈walk × 1.5⌉."""
    explicit = to_int(parsed.get("Run MP"))
    if explicit is not None:
        return explicit
    walk = to_float(parsed.get("Walk MP"))
    if walk is None:
        return None
    return int(math.ceil(walk * 1.5))


def extract_cruise_mp(parsed: dict) -> int | None:
    """Vehicle Cruise MP."""
    return to_int(parsed.get("Cruise MP") or parsed.get("Cruise Mp") or parsed.get("cruise_mp"))


def extract_safe_thrust(parsed: dict) -> int | None:
    """Aerospace Safe Thrust."""
    return to_int(parsed.get("Safe Thrust") or parsed.get("safe_thrust"))


def extract_engine_rating(parsed: dict) -> float | None:
    eng = parsed.get("Engine") or parsed.get("engine")
    if isinstance(eng, dict):
        return to_float(eng.get("rating") or eng.get("Rating"))
    return to_float(eng)


def extract_heat_sink_count(parsed: dict) -> int | None:
    hs = parsed.get("Heat Sinks") or parsed.get("HeatSinks")
    if isinstance(hs, dict):
        return to_int(hs.get("count") or hs.get("Count") or hs.get("number"))
    return to_int(hs)


# Conventional infantry MP is not stored explicitly in BattleTech unit
# files; it is a rules lookup keyed off ``Motion Type`` (Total Warfare
# p.215, table "Infantry Ground Movement"). Values below are walking MP
# only — jump MP is a separate concern handled at translation time.
_INFANTRY_MP_BY_MOTION: dict[str, int] = {
    "foot":            1,
    "leg":             1,   # alias for foot in some source files
    "beast":           1,
    "jump":            1,   # 1 walk MP, jump rated separately
    "motorized":       3,
    "motorized scuba": 3,
    "tracked":         2,
    "wheeled":         3,
    "hover":           5,
    "vtol":            6,
    "vtol (microlite)": 7,
    "microlite":       7,
    "submarine":       2,
    "underwater":      2,
}


def extract_infantry_movement(parsed: dict) -> tuple[int | None, str | None]:
    """Infantry base movement points + motion type.

    Movement is taken from an explicit field when present; otherwise it is
    derived from ``Motion Type`` via the canonical rules lookup. Returns
    ``(None, None)`` only when neither piece of information is available.
    """
    mp = to_int(
        parsed.get("Movement Points")
        or parsed.get("Ground MP")
        or parsed.get("Walk MP")
    )
    mt = parsed.get("Motion Type") or parsed.get("MotionType")
    if not isinstance(mt, str) or not mt:
        mt = None
    if mp is None and mt is not None:
        key = mt.strip().lower()
        mp = _INFANTRY_MP_BY_MOTION.get(key)
        if mp is None and ":" in key:
            # Compound types like "Beast:Camel" — fall back to the prefix.
            mp = _INFANTRY_MP_BY_MOTION.get(key.split(":", 1)[0].strip())
    return mp, mt
