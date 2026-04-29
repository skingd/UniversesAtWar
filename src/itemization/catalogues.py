"""Part 1 — Itemization catalogues.

Builds four catalogues from `data/index/equipment_index.json` and the unit
indices:
    * P1.1 Weapons
    * P1.2 Ammunition
    * P1.3 Equipment
    * P1.4 Upgrades  (a curated view of P1.3 entries that materially alter
                      a chassis and likely need a dedicated LI special rule)

Plus P1.5 coverage verification: every equipment record must land in exactly
one catalogue, and every unit equipment reference must resolve to a catalogue
entry (uncatalogued references are blocking; orphan catalogue entries are
informational).
"""
from __future__ import annotations

import re
from collections import defaultdict
from typing import Any, Iterable

from .common import to_float, to_int


# --- Weapon subcategory classification -------------------------------------

# Order matters — first match wins. The patterns are checked against the
# weapon's display_name (case-insensitive).
_WEAPON_SUBCATEGORY_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("gauss",         re.compile(r"\bgauss\b|magshot", re.I)),
    ("autocannon",    re.compile(r"\b(ac|lac|hac|hag|lb[- ]?\d+[- ]?x|ultra ac|rotary ac)\b|autocannon", re.I)),
    ("machine-gun",   re.compile(r"\bmachine gun\b|\bmg array\b|\bmg\b", re.I)),
    ("rifle",         re.compile(r"\brifle\b", re.I)),
    ("ppc",           re.compile(r"\bppc\b|particle cannon|plasma rifle|plasma cannon", re.I)),
    ("pulse-laser",   re.compile(r"pulse laser|x[- ]pulse", re.I)),
    ("er-laser",      re.compile(r"\ber\s+(small|medium|large|micro)?\s*laser|er laser", re.I)),
    ("heavy-laser",   re.compile(r"heavy laser|binary laser|bombast laser|chemical laser", re.I)),
    ("laser",         re.compile(r"\blaser\b", re.I)),
    ("flamer",        re.compile(r"\bflamer\b", re.I)),
    ("tser",          re.compile(r"taser", re.I)),
    ("streak",        re.compile(r"streak", re.I)),
    ("atm",           re.compile(r"\batm\b|\biatm\b", re.I)),
    ("lrm",           re.compile(r"\blrm\b|\bilrm\b|\bextended lrm\b|enhanced lrm", re.I)),
    ("srm",           re.compile(r"\bsrm\b|\bisrm\b", re.I)),
    ("mrm",           re.compile(r"\bmrm\b|\bmml\b", re.I)),
    ("mrl",           re.compile(r"\bmrl\b|rocket launcher|\bthunderbolt\b", re.I)),
    ("artillery",     re.compile(r"arrow iv|long tom|sniper|thumper|cruise missile|bombast", re.I)),
    ("narc",          re.compile(r"\bnarc\b", re.I)),
    ("tag",           re.compile(r"\btag\b", re.I)),
    ("ams",           re.compile(r"anti[- ]?missile|\bams\b|laser ams", re.I)),
    ("bomb",          re.compile(r"\bbomb\b|cluster bomb|inferno bomb", re.I)),
    ("melee",         re.compile(r"hatchet|sword|claw|talon|spike|fist|mace|lance|flail|whip|chainsaw|vibroblade|retractable blade", re.I)),
]


def classify_weapon_subcategory(display_name: str | None) -> str:
    if not display_name:
        return "unknown"
    for label, pat in _WEAPON_SUBCATEGORY_PATTERNS:
        if pat.search(display_name):
            return label
    return "other"


# --- Upgrade classification (P1.4) -----------------------------------------

# Each tuple: (upgrade_label, regex against display_name, affects_stat,
# binary_or_scaled). `affects_stat` ∈ {"move", "armour-save", "range-band",
# "wounds", "heat", "special-rule-only"}; `binary_or_scaled` ∈ {"binary",
# "scaled"}.
_UPGRADE_PATTERNS: list[tuple[str, re.Pattern[str], str, str]] = [
    # Engines
    ("engine-xl",            re.compile(r"\bxl\s*engine\b|\bxl\s*fusion\b|\bextra[- ]light engine\b", re.I), "wounds", "binary"),
    ("engine-light",         re.compile(r"\blight\s+(fusion\s+)?engine\b", re.I), "wounds", "binary"),
    ("engine-xxl",           re.compile(r"\bxxl\s*engine\b", re.I), "wounds", "binary"),
    ("engine-compact",       re.compile(r"\bcompact\s+(fusion\s+)?engine\b", re.I), "wounds", "binary"),
    ("engine-fuel-cell",     re.compile(r"fuel[- ]cell engine", re.I), "special-rule-only", "binary"),
    ("engine-fission",       re.compile(r"fission engine", re.I), "special-rule-only", "binary"),
    ("engine-ice",           re.compile(r"\bice engine\b|internal combustion", re.I), "special-rule-only", "binary"),
    ("engine-primitive",     re.compile(r"primitive engine|primitive fusion", re.I), "special-rule-only", "binary"),
    # Internal structure
    ("structure-endo-steel", re.compile(r"endo[- ]steel", re.I), "wounds", "binary"),
    ("structure-endo-composite", re.compile(r"endo[- ]composite", re.I), "wounds", "binary"),
    ("structure-composite",  re.compile(r"\bcomposite structure\b|^composite$", re.I), "wounds", "binary"),
    ("structure-reinforced", re.compile(r"reinforced structure|reinforced internal", re.I), "wounds", "binary"),
    ("structure-industrial", re.compile(r"industrial structure", re.I), "wounds", "binary"),
    # Armour types
    ("armor-ferro-fibrous",  re.compile(r"ferro[- ]fibrous", re.I), "armour-save", "binary"),
    ("armor-ferro-lamellor", re.compile(r"ferro[- ]lamellor", re.I), "armour-save", "binary"),
    ("armor-hardened",       re.compile(r"hardened armou?r", re.I), "armour-save", "binary"),
    ("armor-reactive",       re.compile(r"reactive armou?r", re.I), "armour-save", "binary"),
    ("armor-reflective",     re.compile(r"reflective armou?r", re.I), "armour-save", "binary"),
    ("armor-stealth",        re.compile(r"stealth armou?r|stealth system", re.I), "special-rule-only", "binary"),
    ("armor-ferro-aluminum", re.compile(r"ferro[- ]aluminum|ferro[- ]aluminium", re.I), "armour-save", "binary"),
    # Gyros / cockpits
    ("gyro-xl",              re.compile(r"\bxl gyro\b", re.I), "special-rule-only", "binary"),
    ("gyro-heavy-duty",      re.compile(r"heavy[- ]duty gyro", re.I), "wounds", "binary"),
    ("gyro-compact",         re.compile(r"compact gyro", re.I), "special-rule-only", "binary"),
    ("cockpit-small",        re.compile(r"small cockpit", re.I), "special-rule-only", "binary"),
    ("cockpit-command",      re.compile(r"command cockpit|command console", re.I), "special-rule-only", "binary"),
    ("cockpit-torso",        re.compile(r"torso[- ]mounted cockpit", re.I), "special-rule-only", "binary"),
    ("cockpit-primitive",    re.compile(r"primitive cockpit", re.I), "special-rule-only", "binary"),
    ("cockpit-industrial",   re.compile(r"industrial cockpit", re.I), "special-rule-only", "binary"),
    ("cockpit-interface",    re.compile(r"interface cockpit", re.I), "special-rule-only", "binary"),
    # Movement upgrades
    ("masc",                 re.compile(r"\bmasc\b", re.I), "move", "binary"),
    ("supercharger",         re.compile(r"supercharger", re.I), "move", "binary"),
    ("tsm",                  re.compile(r"triple[- ]strength myomer|\btsm\b", re.I), "move", "binary"),
    ("partial-wing",         re.compile(r"partial wing", re.I), "move", "binary"),
    ("jump-booster",         re.compile(r"jump booster|mechanical jump booster", re.I), "move", "binary"),
    ("umu",                  re.compile(r"\bumu\b|underwater maneuvering", re.I), "move", "binary"),
    # Signature / EW
    ("null-signature",       re.compile(r"null[- ]signature", re.I), "special-rule-only", "binary"),
    ("void-signature",       re.compile(r"void[- ]signature", re.I), "special-rule-only", "binary"),
    ("chameleon-lps",        re.compile(r"chameleon( light)?( polarization)?", re.I), "special-rule-only", "binary"),
    ("mimetic-armor",        re.compile(r"mimetic", re.I), "special-rule-only", "binary"),
    ("ecm",                  re.compile(r"\becm\b|guardian ecm|angel ecm", re.I), "special-rule-only", "binary"),
    # Command / coordination
    ("c3",                   re.compile(r"\bc3\b", re.I), "special-rule-only", "binary"),
    ("artemis",              re.compile(r"artemis( iv| v)?( fcs)?", re.I), "range-band", "binary"),
    ("apollo",               re.compile(r"apollo( fcs)?", re.I), "range-band", "binary"),
    ("narc-launcher",        re.compile(r"\bnarc\b launcher|improved narc", re.I), "range-band", "binary"),
    ("tag-system",           re.compile(r"^tag$|^light tag$", re.I), "special-rule-only", "binary"),
    ("active-probe",         re.compile(r"active probe|bloodhound|watchdog", re.I), "special-rule-only", "binary"),
    ("targeting-computer",   re.compile(r"targeting computer", re.I), "range-band", "binary"),
    # Heat
    ("heat-sink-double",     re.compile(r"double heat sink", re.I), "heat", "scaled"),
    ("heat-sink-laser",      re.compile(r"laser heat sink", re.I), "heat", "scaled"),
    ("heat-sink-compact",    re.compile(r"compact heat sink", re.I), "heat", "scaled"),
    ("heat-sink-risc",       re.compile(r"risc heat sink", re.I), "heat", "scaled"),
    ("coolant-pod",          re.compile(r"coolant pod", re.I), "heat", "scaled"),
    # Defensive / specialty
    ("case",                 re.compile(r"\bcase\b( ii)?", re.I), "special-rule-only", "binary"),
    ("aes",                  re.compile(r"\baes\b|actuator enhancement", re.I), "special-rule-only", "binary"),
    ("battlemech-shield",    re.compile(r"battlemech shield|mech shield", re.I), "armour-save", "binary"),
    ("claws-talons",         re.compile(r"^claws?$|^talons?$|^spikes?$", re.I), "special-rule-only", "binary"),
]


def classify_upgrade(display_name: str | None) -> tuple[str, str, str] | None:
    """Return (upgrade_label, affects_stat, binary_or_scaled) or None if the
    item is not a recognised chassis-altering upgrade."""
    if not display_name:
        return None
    for label, pat, affects, mode in _UPGRADE_PATTERNS:
        if pat.search(display_name):
            return label, affects, mode
    return None


# --- Equipment categorisation for P1.3 -------------------------------------

# Coarse functional buckets used in the equipment.md grouping. Falls back to
# the source `equipment_type` when present, otherwise inferred from name.
_EQUIPMENT_TYPE_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("heat",        re.compile(r"heat sink|coolant", re.I)),
    ("mobility",    re.compile(r"jump jet|jump booster|masc|supercharger|myomer|partial wing|umu|propulsion", re.I)),
    ("electronics", re.compile(r"\becm\b|active probe|bloodhound|watchdog|c3|tag|narc|targeting computer|sensor|comms|communications|interface", re.I)),
    ("defence",     re.compile(r"\bcase\b|stealth|chameleon|mimetic|null[- ]sig|void[- ]sig|reactive|reflective|shield|hardened", re.I)),
    ("fcs",         re.compile(r"artemis|apollo|fire control", re.I)),
    ("structural",  re.compile(r"engine|gyro|cockpit|endo|composite|ferro|armor|armour|structure|reinforced", re.I)),
    ("utility",     re.compile(r"cargo|lift hoist|searchlight|mine|smoke|rsd|remote sensor|trailer|fluid|salvage|spotlight|environmental sealing", re.I)),
]


def classify_equipment_type(rec: dict) -> str:
    explicit = rec.get("equipment_type")
    if isinstance(explicit, str) and explicit:
        return explicit
    name = rec.get("display_name") or ""
    for label, pat in _EQUIPMENT_TYPE_PATTERNS:
        if pat.search(name):
            return label
    return "other"


# --- Catalogue construction ------------------------------------------------

WEAPON_CATEGORIES = ("ballistic", "energy", "missile", "physical", "infantry")


def build_catalogues(
    equipment_records: list[dict],
    unit_indices: dict[str, list[dict]],
    *,
    alias_index: Any | None = None,
) -> dict:
    """Build all four Part-1 catalogues plus the coverage report.

    Parameters
    ----------
    equipment_records
        Contents of `data/index/equipment_index.json`.
    unit_indices
        `{unit_type: [unit_record, ...]}` from the four unit indices.
    alias_index
        Optional `datacheck.alias_resolver.AliasIndex` used to compute
        per-equipment usage counts. When `None`, usage counts are zero and
        coverage uncatalogued/orphan reports are skipped.
    """
    # 1) Compute usage_count + mounting_unit_types per canonical_id.
    usage = _compute_usage(unit_indices, alias_index)

    weapons: list[dict] = []
    ammo: list[dict] = []
    equipment: list[dict] = []
    upgrades: list[dict] = []
    classification_seen: dict[str, str] = {}  # canonical_id -> catalogue

    for rec in equipment_records:
        cat = rec.get("category")
        cid = rec["canonical_id"]
        u = usage.get(cid, {"count": 0, "unit_types": set()})
        common_meta = {
            "canonical_id": cid,
            "display_name": rec.get("display_name"),
            "tech_base": rec.get("tech_base"),
            "tech_rating": rec.get("tech_rating"),
            "rarity": rec.get("rarity"),
            "source": rec.get("source"),
            "page_ref": rec.get("page_ref"),
            "tonnage": to_float(rec.get("weight_tons")),
            "usage_count": u["count"],
            "mounting_unit_types": sorted(u["unit_types"]),
        }
        if cat in WEAPON_CATEGORIES:
            entry = _weapon_entry(rec, common_meta)
            weapons.append(entry)
            classification_seen[cid] = "weapons"
        elif cat == "ammunition":
            entry = _ammo_entry(rec, common_meta)
            ammo.append(entry)
            classification_seen[cid] = "ammunition"
        elif cat == "equipment":
            entry = _equipment_entry(rec, common_meta)
            equipment.append(entry)
            classification_seen[cid] = "equipment"
            up = classify_upgrade(rec.get("display_name"))
            if up:
                label, affects, mode = up
                upgrades.append({
                    **common_meta,
                    "category": entry["category"],
                    "upgrade_label": label,
                    "affects_stat": affects,
                    "binary_or_scaled": mode,
                    "crit_slots": entry.get("crit_slots"),
                })
        elif cat == "unit-derived":
            # Synthesized records from the data-check harvest. We classify
            # them by name so they show up in the right catalogue rather
            # than being silently dropped.
            up = classify_upgrade(rec.get("display_name"))
            if up:
                entry = _equipment_entry(rec, common_meta)
                equipment.append(entry)
                classification_seen[cid] = "equipment"
                label, affects, mode = up
                upgrades.append({
                    **common_meta,
                    "category": entry["category"],
                    "upgrade_label": label,
                    "affects_stat": affects,
                    "binary_or_scaled": mode,
                    "crit_slots": entry.get("crit_slots"),
                })
            elif _looks_like_weapon(rec.get("display_name")):
                weapons.append(_weapon_entry(rec, common_meta))
                classification_seen[cid] = "weapons"
            elif _looks_like_ammo(rec.get("display_name")):
                ammo.append(_ammo_entry(rec, common_meta))
                classification_seen[cid] = "ammunition"
            else:
                equipment.append(_equipment_entry(rec, common_meta))
                classification_seen[cid] = "equipment"
        else:
            # Unknown source category — drop into equipment so it is still
            # visible, and flag it via coverage report.
            equipment.append(_equipment_entry(rec, common_meta))
            classification_seen[cid] = "equipment"

    weapons.sort(key=lambda e: (e["category"], e["subcategory"], e.get("tech_base") or "", e.get("tonnage") or 0))
    ammo.sort(key=lambda e: (e.get("weapon_ref") or "", e.get("display_name") or ""))
    equipment.sort(key=lambda e: (e["category"], e.get("display_name") or ""))
    upgrades.sort(key=lambda e: (e["upgrade_label"], e.get("display_name") or ""))

    coverage = _coverage(
        equipment_records,
        classification_seen,
        unit_indices,
        alias_index,
    )

    return {
        "weapons": weapons,
        "ammunition": ammo,
        "equipment": equipment,
        "upgrades": upgrades,
        "coverage": coverage,
    }


# --- Per-catalogue entry builders -----------------------------------------

def _weapon_entry(rec: dict, common: dict) -> dict:
    rng = rec.get("range") or {}
    space = rec.get("space") or {}
    subcat = classify_weapon_subcategory(rec.get("display_name"))
    return {
        **common,
        "category": rec.get("category"),
        "subcategory": subcat,
        "damage": rec.get("damage"),
        "heat": to_float(rec.get("heat")),
        "min_range":   to_float(rng.get("minimum")) if isinstance(rng, dict) else None,
        "short_range": to_float(rng.get("short")) if isinstance(rng, dict) else None,
        "medium_range": to_float(rng.get("medium")) if isinstance(rng, dict) else None,
        "long_range":  to_float(rng.get("long")) if isinstance(rng, dict) else None,
        "extreme_range": to_float(rng.get("extreme")) if isinstance(rng, dict) else None,
        "crit_slots":  to_int(space.get("battlemech")) if isinstance(space, dict) else None,
        "ammo_per_ton": to_int(rec.get("ammo_per_ton")),
        "cost":        to_float(rec.get("cost")),
    }


def _ammo_entry(rec: dict, common: dict) -> dict:
    name = (rec.get("display_name") or "").lower()
    munition_flags = []
    for flag in ("inferno", "precision", "armor-piercing", "armor piercing", "tandem",
                 "smoke", "flare", "mine clearance", "swarm", "narc", "artemis",
                 "tracer", "incendiary", "fragmentation", "cluster", "homing"):
        if flag in name:
            munition_flags.append(flag.replace(" ", "-"))
    return {
        **common,
        "category": "ammunition",
        "weapon_ref": rec.get("weapon_ref"),
        "shots_per_ton": to_int(rec.get("ammo_per_ton")),
        "munition_flags": munition_flags,
        "is_special_munition": bool(munition_flags),
    }


def _equipment_entry(rec: dict, common: dict) -> dict:
    space = rec.get("space") or {}
    return {
        **common,
        "category": classify_equipment_type(rec),
        "raw_category": rec.get("category"),
        "crit_slots": to_int(space.get("battlemech")) if isinstance(space, dict) else None,
        "mechanical_effect": rec.get("display_name"),
    }


def _looks_like_weapon(name: str | None) -> bool:
    if not name:
        return False
    return classify_weapon_subcategory(name) not in ("unknown", "other")


def _looks_like_ammo(name: str | None) -> bool:
    if not name:
        return False
    return bool(re.search(r"\bammo\b|\bammunition\b", name, re.I))


# --- Usage cross-reference -------------------------------------------------

def _compute_usage(
    unit_indices: dict[str, list[dict]],
    alias_index: Any | None,
) -> dict[str, dict]:
    """Return `{canonical_id: {"count": int, "unit_types": set[str]}}`."""
    out: dict[str, dict] = defaultdict(lambda: {"count": 0, "unit_types": set()})
    if alias_index is None:
        return out
    # Local import to avoid a hard dep when the resolver isn't available.
    from src.datacheck.alias_resolver import parse_reference  # noqa: WPS433

    for ut, records in unit_indices.items():
        for unit in records:
            for raw in unit.get("raw_equipment_refs") or []:
                parsed = parse_reference(raw)
                cid, _kind = alias_index.lookup(parsed)
                if cid:
                    out[cid]["count"] += 1
                    out[cid]["unit_types"].add(ut)
    return out


# --- P1.5 Coverage verification -------------------------------------------

def _coverage(
    equipment_records: list[dict],
    classification_seen: dict[str, str],
    unit_indices: dict[str, list[dict]],
    alias_index: Any | None,
) -> dict:
    """Cross-check that every record is classified and every unit ref resolves."""
    by_catalogue: dict[str, int] = defaultdict(int)
    for cat in classification_seen.values():
        by_catalogue[cat] += 1

    missing_classification = [
        rec["canonical_id"] for rec in equipment_records
        if rec["canonical_id"] not in classification_seen
    ]

    orphans: list[dict] = []
    uncatalogued: list[dict] = []

    if alias_index is not None:
        from src.datacheck.alias_resolver import parse_reference  # noqa: WPS433

        seen_cids: set[str] = set()
        # uncatalogued = unit ref resolves to a canonical_id that we did not classify
        # (should be impossible given how we iterate equipment_records, but check).
        for ut, records in unit_indices.items():
            for unit in records:
                for raw in unit.get("raw_equipment_refs") or []:
                    parsed = parse_reference(raw)
                    cid, _kind = alias_index.lookup(parsed)
                    if cid:
                        # `unknown:*` prefixes are sentinels emitted by the
                        # data-check alias harvest for references that have no
                        # canonical record. They are tracked as a separate
                        # data-check finding and are NOT itemization failures.
                        if cid.startswith("unknown:"):
                            continue
                        seen_cids.add(cid)
                        if cid not in classification_seen:
                            uncatalogued.append({
                                "raw": raw,
                                "canonical_id": cid,
                                "unit_type": ut,
                                "unit_path": unit.get("source_path"),
                            })
        for rec in equipment_records:
            if rec["canonical_id"] not in seen_cids:
                orphans.append({
                    "canonical_id": rec["canonical_id"],
                    "display_name": rec.get("display_name"),
                    "category": rec.get("category"),
                })

    return {
        "by_catalogue": dict(by_catalogue),
        "missing_classification": missing_classification,
        "uncatalogued_count": len(uncatalogued),
        "uncatalogued": uncatalogued[:200],  # cap for report sanity
        "orphan_count": len(orphans),
        "orphans": orphans,
        "blocking": bool(missing_classification or uncatalogued),
    }
