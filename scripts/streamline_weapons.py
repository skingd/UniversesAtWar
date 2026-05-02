"""Generate deduplicated WeaponRules.csv per plans/streamline-weapons.prompt.md.

- Reads data/weapons.csv (distilled source).
- Applies range-band translation (min + long range) to compute the new range.
- Classifies each weapon by Type (Missile / Ballistic / Energy / Support).
- Marks weapons with multi-ammo support via the "Special Ammo" trait, derived
  from data/AmmunitionRules.csv plus a small canonical multi-ammo list.
- Retains Clan / Inner Sphere separation; condenses (turret)/(split) variants
  by virtue of weapons.csv already lacking those qualifiers.
- Emits columns: Weapon Name, Range, Type, Traits.

Run:  python scripts/streamline_weapons.py
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "weapons.csv"
AMMO = ROOT / "data" / "AmmunitionRules.csv"
OUT = ROOT / "data" / "WeaponRules.csv"


def translate_min(min_range: int) -> int | None:
    if min_range <= 0:
        return None
    if min_range <= 2:
        return 1
    if min_range <= 4:
        return 2
    if min_range <= 6:
        return 4
    if min_range <= 8:
        return 8
    return 16  # 9-10


def translate_long(long_range: int) -> int:
    if long_range <= 1:
        return 4
    if long_range <= 3:
        return 6
    if long_range <= 10:
        return 8
    if long_range <= 12:
        return 12
    if long_range <= 15:
        return 14
    if long_range <= 19:
        return 18
    if long_range <= 29:
        return 20
    if long_range <= 35:
        return 28
    return 36


def format_range(min_r: int, long_r: int) -> str:
    total = translate_long(long_r)
    minimum = translate_min(min_r)
    if minimum is None:
        return f'{total}"'
    return f'{minimum}"-{total}"'


# ---------------------------------------------------------------------------
# Type classification
# ---------------------------------------------------------------------------

MELEE_TOKENS = {
    "Talons", "Claw", "Flail", "Hatchet", "Lance", "Vibroblade",
    "Retractable Blade", "Sword", "Wrecking Ball",
}

ENERGY_TOKENS = (
    "Laser", "PPC", "Flamer", "Plasma Cannon", "Plasma Rifle",
)

MISSILE_TOKENS = (
    "LRM", "MRM", "SRM", "ATM", "iATM", "Streak", "Rocket Launcher",
    "Thunderbolt", "Arrow IV", "MML", "Narc", "iNarc", "Bomb Bay",
    "Cruise Missile",
)


def classify(name: str) -> str:
    for tok in MELEE_TOKENS:
        if tok in name:
            return "Support"
    for tok in MISSILE_TOKENS:
        if f" {tok}" in f" {name}" or name.endswith(tok) or name.startswith(tok):
            # Use word-boundary-ish match
            if any(part == tok for part in name.replace("/", " ").split()):
                return "Missile"
            if tok in ("ATM", "iATM", "MRM", "MML", "LRM", "SRM"):
                return "Missile"
            if tok in name:
                return "Missile"
    for tok in ENERGY_TOKENS:
        if tok in name:
            return "Energy"
    # Default: ballistic (covers AC, Gauss, HAG, LB-X, Ultra AC, Rotary AC,
    # ProtoMech AC, Machine Gun, Rifle, Cannon (artillery), Taser, MagShot, Bombast).
    return "Ballistic"


# ---------------------------------------------------------------------------
# Special-ammo / trait inference
# ---------------------------------------------------------------------------

# Weapon families known to support multiple ammo types.
SPECIAL_AMMO_FAMILIES = (
    "ATM", "iATM",
    "LB 2-X AC", "LB 5-X AC", "LB 10-X AC", "LB 20-X AC",
    "LRM", "MRM", "MML", "SRM",
    "Arrow IV", "Long Tom Cannon", "Sniper Cannon", "Thumper Cannon",
    "AC/2", "AC/5", "AC/10", "AC/20",
    "Ultra AC", "Rotary AC", "HAG",
    "Narc Missile Beacon", "iNarc Launcher",
)

# Curated trait hints. Empty string means no extra traits.
TRAIT_HINTS: dict[str, str] = {
    # ATM family already characterised in legacy data.
    "Clan ATM 3": "Artemis IV, Barrage",
    "Clan ATM 6": "Artemis IV, Barrage",
    "Clan ATM 9": "Artemis IV, Barrage",
    "Clan ATM 12": "Artemis IV, Barrage",
    "Clan iATM 3": "Artemis V, Barrage",
    "Clan iATM 6": "Artemis V, Barrage",
    "Clan iATM 9": "Artemis V, Barrage",
    "Clan iATM 12": "Artemis V, Barrage",
    # Autocannons.
    "Inner Sphere AC/2": "Light, Rapid Fire",
    "Inner Sphere AC/5": "Light AT",
    "Inner Sphere AC/10": "Anti-Tank",
    "Inner Sphere AC/20": "Anti-Tank, Demolisher",
    "Inner Sphere Light AC/2": "Light, Rapid Fire",
    "Inner Sphere Light AC/5": "Light AT",
    "Inner Sphere Heavy Rifle": "Anti-Tank",
    "Inner Sphere Bomb Bay": "Bombing Run",
    # Pulse traits.
    # Streak family (lock-on).
    "Clan Streak SRM 2": "Lock-On",
    "Clan Streak SRM 4": "Lock-On",
    "Clan Streak SRM 6": "Lock-On",
    "Inner Sphere Streak SRM 2": "Lock-On",
    "Inner Sphere Streak SRM 4": "Lock-On",
    "Inner Sphere Streak SRM 6": "Lock-On",
    "Clan Streak LRM 5": "Lock-On",
    "Clan Streak LRM 10": "Lock-On",
    "Clan Streak LRM 15": "Lock-On",
    "Clan Streak LRM 20": "Lock-On",
    # Artillery.
    "Inner Sphere Long Tom Cannon": "Artillery, Demolisher",
    "Inner Sphere Sniper Cannon": "Artillery",
    "Inner Sphere Thumper Cannon": "Artillery",
    "Clan Arrow IV": "Artillery, Homing",
    "Inner Sphere Arrow IV": "Artillery, Homing",
    # Gauss / heavy hitters.
    "Inner Sphere Heavy Gauss Rifle": "Anti-Tank, Demolisher",
    "Inner Sphere Improved Heavy Gauss Rifle": "Anti-Tank, Demolisher",
    "Clan Gauss Rifle": "Anti-Tank",
    "Inner Sphere Gauss Rifle": "Anti-Tank",
    "Clan Improved Gauss Rifle": "Anti-Tank",
    "Inner Sphere Improved Gauss Rifle": "Anti-Tank",
    "Inner Sphere Light Gauss Rifle": "Light AT",
    "Inner Sphere Silver Bullet Gauss Rifle": "Light AT",
    "Clan AP Gauss Rifle": "Light",
    "Inner Sphere MagShot Gauss Rifle": "Light",
    # HAG.
    "Clan HAG/20": "Anti-Tank, Cluster",
    "Clan HAG/30": "Anti-Tank, Cluster",
    "Clan HAG/40": "Anti-Tank, Demolisher, Cluster",
    # PPCs.
    "Inner Sphere Heavy PPC": "Anti-Tank",
    "Inner Sphere Light PPC": "Light",
    "Inner Sphere Snub-Nose PPC": "Snub",
    # Flamers / plasma.
    "Clan ER Flamer": "Light, Inferno",
    "Inner Sphere ER Flamer": "Light, Inferno",
    "Clan Flamer": "Light, Inferno",
    "Inner Sphere Flamer": "Light, Inferno",
    "Clan Heavy Flamer": "Inferno",
    "Inner Sphere Heavy Flamer": "Inferno",
    "Clan Plasma Cannon": "Inferno",
    "Inner Sphere Plasma Rifle": "Inferno",
    # Machine guns.
    "Clan Machine Gun": "Light, Anti-Infantry",
    "Inner Sphere Machine Gun": "Light, Anti-Infantry",
    "Clan Light Machine Gun": "Light, Anti-Infantry",
    "Inner Sphere Light Machine Gun": "Light, Anti-Infantry",
    "Clan Heavy Machine Gun": "Anti-Infantry",
    "Inner Sphere Heavy Machine Gun": "Anti-Infantry",
    # Rotary / Ultra (rapid fire).
    "Clan Rotary AC/2": "Light, Rapid Fire",
    "Clan Rotary AC/5": "Light AT, Rapid Fire",
    "Inner Sphere Rotary AC/2": "Light, Rapid Fire",
    "Inner Sphere Rotary AC/5": "Light AT, Rapid Fire",
    "Clan Ultra AC/2": "Light, Rapid Fire",
    "Clan Ultra AC/5": "Light AT, Rapid Fire",
    "Clan Ultra AC/10": "Anti-Tank, Rapid Fire",
    "Clan Ultra AC/20": "Anti-Tank, Demolisher, Rapid Fire",
    "Inner Sphere Ultra AC/2": "Light, Rapid Fire",
    "Inner Sphere Ultra AC/5": "Light AT, Rapid Fire",
    "Inner Sphere Ultra AC/10": "Anti-Tank, Rapid Fire",
    "Inner Sphere Ultra AC/20": "Anti-Tank, Demolisher, Rapid Fire",
    # LB-X (cluster).
    "Clan LB 2-X AC": "Light, Cluster",
    "Clan LB 5-X AC": "Light AT, Cluster",
    "Clan LB 10-X AC": "Anti-Tank, Cluster",
    "Clan LB 20-X AC": "Anti-Tank, Demolisher, Cluster",
    "Inner Sphere LB 2-X AC": "Light, Cluster",
    "Inner Sphere LB 5-X AC": "Light AT, Cluster",
    "Inner Sphere LB 10-X AC": "Anti-Tank, Cluster",
    "Inner Sphere LB 20-X AC": "Anti-Tank, Demolisher, Cluster",
    # Rocket launchers (one-shot).
    "Inner Sphere Rocket Launcher 10": "One-Shot, Barrage",
    "Inner Sphere Rocket Launcher 15": "One-Shot, Barrage",
    "Inner Sphere Rocket Launcher 20": "One-Shot, Barrage",
    # Narc / iNarc / TAG-like.
    "Clan Narc Missile Beacon": "Tagger",
    "Inner Sphere Narc Missile Beacon": "Tagger",
    "Inner Sphere iNarc Launcher": "Tagger",
    # Taser.
    "Inner Sphere BattleMech Taser": "Stun",
    # Bomb Bay (already listed above).
    # Pulse lasers (general "Pulse" trait).
}

PULSE_TRAIT = "Pulse"
ER_TRAIT = "Extended Range"
HEAVY_TRAIT = "Heavy"
VSP_TRAIT = "Variable"
XPULSE_TRAIT = "Pulse"


def derive_traits(name: str) -> list[str]:
    traits: list[str] = []
    hint = TRAIT_HINTS.get(name, "")
    if hint:
        traits.extend(t.strip() for t in hint.split(","))

    # Pulse / X-Pulse / VSP.
    if "Pulse Laser" in name or "X-Pulse Laser" in name:
        if PULSE_TRAIT not in traits:
            traits.append(PULSE_TRAIT)
    if "VSP Laser" in name and VSP_TRAIT not in traits:
        traits.append(VSP_TRAIT)
    # ER.
    if name.startswith("Clan ER") or name.startswith("Inner Sphere ER"):
        if ER_TRAIT not in traits:
            traits.append(ER_TRAIT)
    # Heavy lasers.
    if "Heavy Large Laser" in name or "Heavy Medium Laser" in name or "Heavy Small Laser" in name:
        if HEAVY_TRAIT not in traits:
            traits.append(HEAVY_TRAIT)
    # Improved.
    if name.startswith("Clan Improved") or name.startswith("Inner Sphere Improved"):
        if "Improved" not in traits:
            traits.append("Improved")
    # Extended LRM (long-range).
    if "Extended LRM" in name and "Long-Range" not in traits:
        traits.append("Long-Range")
    # Enhanced LRM.
    if "Enhanced LRM" in name and "Artemis IV" not in traits:
        traits.append("Artemis IV")
    return traits


def has_special_ammo(name: str, ammo_weapons: set[str]) -> bool:
    # Direct hit on AmmunitionRules entries.
    for w in ammo_weapons:
        if w and w.lower() in name.lower():
            return True
    # Family heuristics.
    for fam in SPECIAL_AMMO_FAMILIES:
        if fam in name:
            return True
    return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def load_ammo_weapons() -> set[str]:
    if not AMMO.exists():
        return set()
    seen: set[str] = set()
    with AMMO.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            w = (row.get("Weapon Name") or "").strip()
            if w:
                seen.add(w)
    return seen


def main() -> None:
    ammo_weapons = load_ammo_weapons()

    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    with SRC.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for r in reader:
            name = r["Weapon Name"].strip()
            if not name or name in seen:
                continue
            seen.add(name)
            try:
                min_r = int(r["Min"])
                long_r = int(r["Long"])
            except ValueError:
                continue
            rng = format_range(min_r, long_r)
            wtype = classify(name)
            traits = derive_traits(name)
            if has_special_ammo(name, ammo_weapons) and "Special Ammo" not in traits:
                traits.append("Special Ammo")
            # Melee weapons get range "Melee".
            if wtype == "Support" and long_r == 0 and min_r == 0:
                rng = "Melee"
            rows.append({
                "Weapon Name": name,
                "Range": rng,
                "Type": wtype,
                "Traits": ", ".join(traits),
            })

    rows.sort(key=lambda x: (x["Type"], x["Weapon Name"]))

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["Weapon Name", "Range", "Type", "Traits"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} weapons to {OUT}")


if __name__ == "__main__":
    main()
