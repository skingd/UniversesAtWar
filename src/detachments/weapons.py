"""Weapon profile catalogue (`data/WeaponRules.csv`) and ammunition options
(`data/AmmunitionRules.csv`), plus name resolution for unit equipment refs.

The CSVs are the authoritative source for game profile data: the unit
files only carry weapon **names**; everything else (range, dice, AP …)
comes from these tables.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable, Optional

from src.datacheck.alias_resolver import (
    AliasIndex,
    ParsedRef,
    _normalize_key,
    parse_reference,
)


@dataclass(frozen=True)
class WeaponProfile:
    name: str
    range: str
    heat: int
    dice: int
    to_hit: str
    ap: int
    type: str
    traits: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        d = asdict(self)
        return d


@dataclass(frozen=True)
class AmmoOption:
    name: str           # ammo variant name e.g. "ER", "Inferno"
    weapon_name: str    # parent weapon
    range: str
    heat: int
    dice: int
    to_hit: str
    ap: int
    type: str
    traits: list[str]
    points: Optional[int]

    def to_dict(self) -> dict:
        return asdict(self)


# ---------------------------------------------------------------------------
# CSV loaders
# ---------------------------------------------------------------------------

def _split_traits(raw: str) -> list[str]:
    if not raw:
        return []
    parts = [p.strip() for p in raw.split(",")]
    return [p for p in parts if p]


def _to_int(raw: str, default: int = 0) -> int:
    raw = (raw or "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        try:
            return int(float(raw))
        except ValueError:
            return default


def _to_optional_int(raw: str) -> Optional[int]:
    raw = (raw or "").strip()
    if not raw:
        return None
    try:
        return int(raw)
    except ValueError:
        try:
            return int(float(raw))
        except ValueError:
            return None


def load_weapon_rules(path: Path) -> list[WeaponProfile]:
    """Load `data/WeaponRules.csv`. Skips rows with an empty Weapon Name."""
    profiles: list[WeaponProfile] = []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = (row.get("Weapon Name") or "").strip()
            if not name:
                continue
            profiles.append(WeaponProfile(
                name=name,
                range=(row.get("Range") or "").strip(),
                heat=_to_int(row.get("Heat", "")),
                dice=_to_int(row.get("Dice", "")),
                to_hit=(row.get("To-Hit") or "").strip(),
                ap=_to_int(row.get("AP", "")),
                type=(row.get("Type") or "").strip(),
                traits=_split_traits(row.get("Traits", "") or ""),
            ))
    return profiles


def load_ammunition_rules(path: Path) -> dict[str, list[AmmoOption]]:
    """Load `data/AmmunitionRules.csv` keyed by parent weapon name."""
    out: dict[str, list[AmmoOption]] = {}
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            wpn = (row.get("Weapon Name") or "").strip()
            ammo_name = (row.get("Ammo Name") or "").strip()
            if not wpn or not ammo_name:
                continue
            opt = AmmoOption(
                name=ammo_name,
                weapon_name=wpn,
                range=(row.get("Range") or "").strip(),
                heat=_to_int(row.get("Heat", "")),
                dice=_to_int(row.get("Dice", "")),
                to_hit=(row.get("To-Hit") or "").strip(),
                ap=_to_int(row.get("AP", "")),
                type=(row.get("Type") or "").strip(),
                traits=_split_traits(row.get("Traits", "") or ""),
                points=_to_optional_int(row.get("Points", "")),
            )
            out.setdefault(wpn, []).append(opt)
    return out


# ---------------------------------------------------------------------------
# Resolution
# ---------------------------------------------------------------------------

@dataclass
class WeaponIndex:
    """Indexes WeaponProfile entries for resolution from raw unit refs."""
    by_name_key: dict[str, WeaponProfile]
    by_canonical_id: dict[str, WeaponProfile]

    def resolve(
        self,
        raw_ref: str,
        alias_index: Optional[AliasIndex] = None,
    ) -> tuple[Optional[WeaponProfile], str]:
        """Return (profile, kind) where kind ∈ {"canonical","name","ammo","miss"}."""
        parsed: ParsedRef = parse_reference(raw_ref)
        if parsed.is_ammo:
            return None, "ammo"

        # 0. Try the raw ref itself (colon-tags stripped, normalized) directly
        #    in the alias index.  Handles MTF CamelCase refs like "ISNarcBeacon"
        #    or "CLNarcBeacon:OMNI" that are registered from mtf_reference fields
        #    in equipment records but whose camel-split form loses information.
        if alias_index is not None:
            raw_clean = _normalize_key(raw_ref.split(":")[0])
            if raw_clean:
                cid = alias_index.exact.get(raw_clean)
                if cid and cid in self.by_canonical_id:
                    return self.by_canonical_id[cid], "canonical"

        # 1. Canonical id route via alias index.
        if alias_index is not None:
            cid, _kind = alias_index.lookup(parsed)
            if cid and cid in self.by_canonical_id:
                return self.by_canonical_id[cid], "canonical"

        # 2. Direct normalized-name route.
        key = parsed.normalized_key
        if key and key in self.by_name_key:
            return self.by_name_key[key], "name"

        # 3. parse_reference strips IS/Clan tech tags from the name; many
        #    CSV rows still carry that prefix ("Inner Sphere Gauss Rifle").
        #    Re-attach the parsed tech_base and try again.
        if key and parsed.tech_base:
            tagged = _normalize_key(f"{parsed.tech_base} {parsed.name}")
            if tagged and tagged in self.by_name_key:
                return self.by_name_key[tagged], "name"

        # 4. Try with a tech-stripped normalized form for cases where the
        #    raw ref carried a prefix the parser didn't strip.
        if key:
            for prefix in ("inner sphere ", "clan ", "is "):
                if key.startswith(prefix):
                    sub = key[len(prefix):]
                    if sub in self.by_name_key:
                        return self.by_name_key[sub], "name"

        # 5. Narc / iNarc keyword fallback.
        #    Bare "Narc" refs and MTF abbreviations like "ISImprovedNarc" don't
        #    match any exact key.  Ammo pods (key contains "pods") are excluded.
        if key and "narc" in key and "pods" not in key:
            tech_lower = "clan" if parsed.tech_base == "Clan" else "inner sphere"
            if "inarc" in key or "improved narc" in key:
                probe = f"{tech_lower} inarc launcher"
            else:
                probe = f"{tech_lower} narc missile beacon"
            if probe in self.by_name_key:
                return self.by_name_key[probe], "name"
            # Tech fallback: try the other tech variant if preferred not present.
            alt = "clan" if tech_lower == "inner sphere" else "inner sphere"
            alt_probe = f"{alt} narc missile beacon"
            if alt_probe in self.by_name_key:
                return self.by_name_key[alt_probe], "name"

        return None, "miss"


def build_weapon_index(
    profiles: Iterable[WeaponProfile],
    equipment_records: Optional[Iterable[dict]] = None,
) -> WeaponIndex:
    """Build a `WeaponIndex` from CSV profiles.

    If `equipment_records` is supplied, also map each profile to a canonical
    equipment id whenever the profile's name matches one of the record's
    name-like fields. This lets the alias resolver's tech-disambiguation
    propagate into weapon resolution.
    """
    by_name_key: dict[str, WeaponProfile] = {}
    for prof in profiles:
        nk = _normalize_key(prof.name)
        if nk:
            by_name_key.setdefault(nk, prof)

    by_canonical_id: dict[str, WeaponProfile] = {}
    if equipment_records is not None:
        # Build display-key -> canonical_id map first.
        name_to_cid: dict[str, str] = {}
        for rec in equipment_records:
            cid = rec.get("canonical_id")
            if not cid:
                continue
            for fname in ("display_name", "mtf_reference", "name"):
                val = rec.get(fname)
                if isinstance(val, str) and val:
                    nk = _normalize_key(val)
                    if nk:
                        name_to_cid.setdefault(nk, cid)
        for nk, prof in by_name_key.items():
            cid = name_to_cid.get(nk)
            if cid:
                by_canonical_id.setdefault(cid, prof)

    return WeaponIndex(by_name_key=by_name_key, by_canonical_id=by_canonical_id)
