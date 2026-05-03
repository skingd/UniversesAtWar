"""Equipment alias resolution.

The corpus references the same weapon under many spellings. This module
normalizes a raw reference string from a unit file into a canonical form
that can be looked up in the equipment index.

Observed reference styles (from real data):
    Mech JSON slot:          "AC/20; Inner Sphere"
    Mech JSON rear:          "Medium Laser; Inner Sphere (R)"
    Mech JSON OmniPod:       "ER Large Laser; Clan (OmniPod)"
    Vehicle YAML weapon:     "PPC", "Medium Laser", "LRM 10"
    Vehicle YAML ammo:       "IS Ammo LRM-10"
    Weapon JSON name:        "Inner Sphere AC/20"
    Weapon JSON mtf_ref:     "Autocannon/20" or "AC/20"
    equipment_names key:     "ISAC2", "CLHAG20", "IS LB 2-X AC Ammo"
    equipment_names display: "AC/2", "Ammo LB 2-X AC"
    equipment_avail name:    "IS AC/20"
    ammunition.json name:    "Inner Sphere Ammo Arrow IV"
    ammunition.json wpn_ref: "Arrow IV"
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Iterable



# These tokens are mech crit slot occupants that are NOT weapons/equipment per se;
# they're structural items, actuators, or empty markers. We classify them but do
# not require resolution against the weapon index.
#
# This base set is auto-extended at runtime from
# `reference/equipment_names.json["structural_crits"]` (see `extend_structural_tokens`).
_STRUCTURAL_BASE: set[str] = {
    "empty",
    "shoulder",
    "upper arm actuator", "lower arm actuator", "hand actuator",
    "hip", "upper leg actuator", "lower leg actuator", "foot actuator",
    "life support", "sensors", "cockpit", "command console",
    "engine",  # bare "Engine" used by vehicle/aerospace YAML
    "fusion engine", "ice engine", "xl engine", "xxl engine", "compact engine",
    "light engine", "fission engine", "fuel cell engine",
    "gyro", "xl gyro", "compact gyro", "heavy duty gyro", "heavy-duty gyro",
    "endo steel", "endo-composite",
    "ferro-fibrous", "ferro fibrous", "light ferro-fibrous", "heavy ferro-fibrous",
    "ferro-lamellor",
    "stealth", "stealth armor", "reactive", "reactive armor",
    "reflective", "reflective armor", "hardened", "patchwork",
    "standard structure", "standard armor",
    # "TSM"-class crit fillers — variants reference/equipment_names omits
    "tsm", "triple strength myomer", "industrial triple strength myomer",
    "environmental sealing",
}
STRUCTURAL_TOKENS: set[str] = set(_STRUCTURAL_BASE)


def extend_structural_tokens(equipment_names: dict | None) -> None:
    """Augment STRUCTURAL_TOKENS with the contents of `structural_crits` from
    the reference data so we don't have to keep the hardcoded list in sync."""
    if not equipment_names:
        return
    section = equipment_names.get("structural_crits")
    if not isinstance(section, dict):
        return
    for raw_key, meta in section.items():
        for s in (raw_key, (meta.get("display") if isinstance(meta, dict) else None)):
            if not isinstance(s, str) or not s:
                continue
            STRUCTURAL_TOKENS.add(_normalize_key(s))
            # also register with tech prefixes stripped
            stripped = _TECH_PREFIX_RE.sub("", s).strip()
            if stripped:
                STRUCTURAL_TOKENS.add(_normalize_key(stripped))

# Modifier suffixes appearing in parentheses — extracted into flags.
_MODIFIER_RE = re.compile(r"\(([^)]+)\)")
# Tech tag separator used by mech JSONs: "; Inner Sphere" / "; Clan"
_TECH_SUFFIX_RE = re.compile(r";\s*(Inner Sphere|Clan|Mixed)\s*$", re.IGNORECASE)
# Common prefixes used in equipment_availability and equipment_names keys
_TECH_PREFIX_RE = re.compile(r"^(IS|CL|Clan|Inner Sphere|ISC|CLER|ISER|ER)\s+", re.IGNORECASE)
# CamelCase suffix tags appearing on equipment_names keys: ":OMNI", ":Prototype"
_COLON_TAG_RE = re.compile(r":[A-Za-z0-9_]+$")
# Casual synonyms commonly used by vehicle/aerospace YAML that don't appear in
# any reference list. Mapping is *applied during normalization* so they share an
# alias key with their canonical equivalent.
_NAME_SYNONYMS: dict[str, str] = {
    "particle cannon": "ppc",
    "light auto cannon/5": "lac/5",
    "light auto cannon/2": "lac/2",
    "light autocannon/5": "lac/5",
    "light autocannon/2": "lac/2",
    "auto cannon/2": "ac/2",
    "auto cannon/5": "ac/5",
    "auto cannon/10": "ac/10",
    "auto cannon/20": "ac/20",
    "autocannon/2": "ac/2",
    "autocannon/5": "ac/5",
    "autocannon/10": "ac/10",
    "autocannon/20": "ac/20",
    "rl 10": "rocket launcher 10",
    "rl 15": "rocket launcher 15",
    "rl 20": "rocket launcher 20",
}


@dataclass
class ParsedRef:
    """A reference string parsed into normalized parts."""
    raw: str
    name: str               # weapon/equipment name with tech & modifier stripped
    tech_base: str | None   # "Inner Sphere" | "Clan" | None
    is_rear: bool = False
    is_omnipod: bool = False
    is_ammo: bool = False
    other_modifiers: list[str] = field(default_factory=list)

    @property
    def normalized_key(self) -> str:
        """A casefolded, whitespace-normalized lookup key."""
        return _normalize_key(self.name)


def _normalize_key(s: str) -> str:
    """Casefold and collapse whitespace/separators for fuzzy lookup."""
    if not s:
        return ""
    # unify hyphens between digits to space ("LRM-10" -> "LRM 10")
    s = re.sub(r"(?<=[A-Za-z])-(?=\d)", " ", s)
    s = re.sub(r"(?<=\d)-(?=[A-Za-z])", " ", s)
    # collapse whitespace
    s = re.sub(r"\s+", " ", s).strip()
    folded = s.casefold()
    return _NAME_SYNONYMS.get(folded, folded)


def parse_reference(raw: str) -> ParsedRef:
    """Parse a single equipment reference string into structured form."""
    if not isinstance(raw, str):
        raw = str(raw)
    s = raw.strip()

    # strip colon-tagged suffixes used by some equipment_names keys: ":OMNI"
    colon_tags: list[str] = []
    while True:
        m = _COLON_TAG_RE.search(s)
        if not m:
            break
        colon_tags.append(m.group(0)[1:])
        s = s[: m.start()].strip()

    # extract modifiers like (R), (OmniPod). Other parenthesized text —
    # e.g. "(Master)", "(Slave)", "(TK Assault)" — is part of the name.
    modifiers: list[str] = []
    _KNOWN_MODS = {"r", "omnipod", "clan", "is", "inner sphere"}
    def _consume(match: re.Match[str]) -> str:
        token = match.group(1).strip()
        if token.lower() in _KNOWN_MODS:
            modifiers.append(token)
            return ""
        return match.group(0)
    s = _MODIFIER_RE.sub(_consume, s).strip()

    is_rear = any(m.lower() == "r" for m in modifiers)
    is_omnipod = any(m.lower() == "omnipod" for m in modifiers) or any(
        t.lower() == "omni" for t in colon_tags
    )
    other = [m for m in modifiers if m.lower() not in ("r", "omnipod")] + colon_tags

    # tech suffix: "AC/20; Inner Sphere"
    tech_base: str | None = None
    m = _TECH_SUFFIX_RE.search(s)
    if m:
        tech_base = _canonical_tech(m.group(1))
        s = s[: m.start()].strip()
    else:
        # tech prefix: "IS AC/20", "Clan Ammo Arrow IV"
        pm = _TECH_PREFIX_RE.match(s)
        if pm:
            tech_base = _canonical_tech(pm.group(1))
            s = s[pm.end():].strip()

    # If the body is now CamelCase glued like "ISMediumLaser" or "CLHAG20", split it.
    if " " not in s and re.search(r"[A-Z][a-z]", s):
        s = _split_camel(s)
        # the split may surface a tech prefix the regex above missed
        pm2 = _TECH_PREFIX_RE.match(s)
        if pm2 and tech_base is None:
            tech_base = _canonical_tech(pm2.group(1))
            s = s[pm2.end():].strip()

    is_ammo = bool(re.match(r"(?i)\bammo\b", s)) or " ammo " in f" {s.lower()} "

    return ParsedRef(
        raw=raw,
        name=s,
        tech_base=tech_base,
        is_rear=is_rear,
        is_omnipod=is_omnipod,
        is_ammo=is_ammo,
        other_modifiers=other,
    )


def _canonical_tech(s: str) -> str:
    s = s.strip().lower()
    if s in ("is", "inner sphere", "iser", "isc"):
        return "Inner Sphere"
    if s in ("cl", "clan", "cler"):
        return "Clan"
    if s == "er":
        # ambiguous prefix — "ER " on its own usually means "Extended Range" weapon
        # variant, NOT a tech tag. Caller treats None as unknown.
        return ""  # sentinel: was ER but consumed, leave tech unset
    return s.title()


def _split_camel(s: str) -> str:
    """Split CamelCase / acronym-glued strings into spaced words.

    "ISMediumLaser" -> "IS Medium Laser"
    "CLHAG20"       -> "CL HAG20"   (digits stay glued to preceding word)
    "ISLBXAC20"     -> "IS LBXAC 20"
    """
    # Insert a space between a lowercase/digit and an uppercase letter
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", s)
    # Insert a space between an uppercase run and an uppercase+lowercase word
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", s)
    # Insert a space between letters and digits (only when transitioning)
    s = re.sub(r"(?<=[A-Za-z])(?=\d)", " ", s)
    return s


def is_structural(parsed: ParsedRef) -> bool:
    """True if the reference is a structural slot occupant, not a weapon."""
    key = parsed.normalized_key
    if not key:
        return True
    if key in STRUCTURAL_TOKENS:
        return True
    # variants like "double heat sink" should be classified as equipment;
    # plain "heat sink" is structural.
    if key == "heat sink":
        return True
    return False


# --- Lookup index ----------------------------------------------------------

@dataclass
class AliasIndex:
    """Maps normalized lookup keys -> canonical equipment ID."""
    # key (normalized) -> canonical_id
    exact: dict[str, str]
    # for fuzzy: list of (normalized_key, canonical_id) for rapidfuzz scoring
    candidates: list[tuple[str, str]]

    def lookup(self, parsed: ParsedRef) -> tuple[str | None, str]:
        """Return (canonical_id, match_kind) where match_kind in
        {"exact", "tech-disambiguated", "structural", "miss"}."""
        if is_structural(parsed):
            return None, "structural"
        key = parsed.normalized_key
        if not key:
            return None, "miss"
        # Try exact match with tech-prefix preference if known
        if parsed.tech_base:
            tech_prefix = "is" if parsed.tech_base == "Inner Sphere" else "clan"
            tagged = f"{tech_prefix} {key}"
            if tagged in self.exact:
                return self.exact[tagged], "tech-disambiguated"
        if key in self.exact:
            return self.exact[key], "exact"
        return None, "miss"

    def fuzzy_suggest(self, parsed: ParsedRef, *, score_cutoff: int = 85) -> list[tuple[str, str, int]]:
        """Return up to 3 fuzzy matches (canonical_id, candidate_key, score)."""
        from rapidfuzz import process, fuzz  # lazy import — not needed on render path
        if is_structural(parsed):
            return []
        key = parsed.normalized_key
        if not key:
            return []
        keys_only = [k for k, _ in self.candidates]
        results = process.extract(
            key, keys_only, scorer=fuzz.WRatio, limit=3, score_cutoff=score_cutoff
        )
        out: list[tuple[str, str, int]] = []
        # rebuild back to canonical_id (first-wins so it matches `exact` dict)
        idx_map: dict[str, str] = {}
        for k, cid in self.candidates:
            idx_map.setdefault(k, cid)
        for matched_key, score, _ in results:
            out.append((idx_map[matched_key], matched_key, int(score)))
        return out


def build_alias_index(
    equipment_records: Iterable[dict],
    equipment_names: dict | None = None,
    ammunition: list[dict] | None = None,
) -> AliasIndex:
    """Construct an AliasIndex from the parsed equipment + reference data.

    `equipment_records` is the canonical equipment index list (each entry must have
    `canonical_id`, `display_name`, optional `mtf_reference`, `tech_base`).
    `equipment_names` is the parsed contents of `reference/equipment_names.json`.
    `ammunition` is the parsed list from `weaponsandequipment/ammunition.json`.
    """
    # populate STRUCTURAL_TOKENS from the reference data first so registrations
    # of structural items are silently skipped (they don't need aliases).
    extend_structural_tokens(equipment_names)

    exact: dict[str, str] = {}
    candidates: list[tuple[str, str]] = []

    def _register(key: str, cid: str) -> None:
        nk = _normalize_key(key)
        if not nk:
            return
        # Don't overwrite an existing mapping (first-wins keeps deterministic behavior)
        exact.setdefault(nk, cid)
        candidates.append((nk, cid))

    for rec in equipment_records:
        cid = rec["canonical_id"]
        for field_name in ("display_name", "mtf_reference", "name"):
            val = rec.get(field_name)
            if isinstance(val, str) and val:
                _register(val, cid)
                # also register a tech-tagged variant for disambiguation
                tb = rec.get("tech_base")
                if tb in ("Inner Sphere", "Clan"):
                    prefix = "is" if tb == "Inner Sphere" else "clan"
                    _register(f"{prefix} {val}", cid)

    # equipment_names.json: keys -> display, with tech metadata
    if equipment_names:
        # keys -> canonical_id via display lookup. Build the lookup from every
        # name-like field on each equipment record so we don't miss matches
        # against records whose `display_name` is a longer tech-tagged form
        # (e.g. record display_name="Inner Sphere Medium Laser" but the
        # equipment_names display="Medium Laser").
        display_to_cid: dict[str, str] = {}
        for rec in equipment_records:
            for fname in ("display_name", "mtf_reference", "name"):
                v = rec.get(fname)
                if isinstance(v, str) and v:
                    display_to_cid.setdefault(_normalize_key(v), rec["canonical_id"])

        for section_name, mapping in equipment_names.items():
            # `structural_crits` was already absorbed into STRUCTURAL_TOKENS;
            # don't pollute the alias index with it.
            if section_name == "structural_crits":
                continue
            if not isinstance(mapping, dict):
                continue
            for raw_key, meta in mapping.items():
                if not isinstance(meta, dict):
                    continue
                disp = meta.get("display") or ""
                tech = meta.get("tech")
                cid = display_to_cid.get(_normalize_key(disp))
                if cid is None:
                    # No matching equipment record; still index the key so we know
                    # about it for resolution reporting (synthesize a placeholder id).
                    cid = f"unknown:{_normalize_key(disp) or _normalize_key(raw_key)}"
                # Register the raw key (e.g. "ISMediumLaser") AND its CamelCase-
                # split form (e.g. "is medium laser") so unit references that go
                # through `parse_reference` (which splits CamelCase) still match.
                _register(raw_key, cid)
                split_form = _split_camel(raw_key)
                if split_form != raw_key:
                    _register(split_form, cid)
                    # also tech-prefixed-stripped form
                    stripped = _TECH_PREFIX_RE.sub("", split_form).strip()
                    if stripped:
                        _register(stripped, cid)
                _register(disp, cid)
                if tech in ("Inner Sphere", "Clan") and disp:
                    prefix = "is" if tech == "Inner Sphere" else "clan"
                    _register(f"{prefix} {disp}", cid)

    # ammunition.json: name + weapon_ref give us extra aliases for ammo entries
    if ammunition:
        for entry in ammunition:
            if not isinstance(entry, dict):
                continue
            name = entry.get("name", "")
            wref = entry.get("weapon_ref", "")
            # try to find a matching equipment record by id first, then by name
            cid = None
            eid = entry.get("id")
            if eid:
                for rec in equipment_records:
                    if rec.get("numeric_id") == eid:
                        cid = rec["canonical_id"]
                        break
            if cid is None and name:
                # Fall back to a synthetic ammo id so it at least resolves
                cid = f"ammo:{_normalize_key(name)}"
            if cid:
                _register(name, cid)
                if wref:
                    _register(f"ammo {wref}", cid)
                    _register(f"is ammo {wref}", cid)
                    _register(f"clan ammo {wref}", cid)

    return AliasIndex(exact=exact, candidates=candidates)
