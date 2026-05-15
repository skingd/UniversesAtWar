"""Generate data/reference/InfantryWeapons.csv and BattleArmorWeapons.csv.

Naming-convention rules applied when translating raw MegaMek tag names:
  IS   → Inner Sphere
  CL   → Clan
  BA   → Battle Armor  (dropped from display name inside BA file; context is implicit)
  OS   → One Shot      → "(One Shot)" suffix + Limited(1) trait
  RL   → Rocket Launcher

Columns kept:  Weapon Name, Range
Columns BLANK: Heat, Dice, To-Hit, AP, Type
Traits:        "Special Ammo" where ammo-fed; "Limited(1)" for One-Shot weapons;
               combined where both apply.

Heat is intentionally omitted — Infantry and Battle Armor do not track heat.
"""
from __future__ import annotations
import csv, pathlib

OUT_DIR = pathlib.Path("data/reference")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Load WeaponRules.csv for range lookups ───────────────────────────────────
wr_range: dict[str, str] = {}
with pathlib.Path("data/WeaponRules.csv").open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        wr_range[row["Weapon Name"].strip().lower()] = row["Range"].strip()

def wr(name: str) -> str:
    """Return range string from WeaponRules.csv, or '' if not found."""
    return wr_range.get(name.lower(), "")

# ── CSV helpers ───────────────────────────────────────────────────────────────
HEADERS = ["Weapon Name", "Range", "Heat", "Dice", "To-Hit", "AP", "Type", "Traits"]

def R(name: str, rng: str, traits: str = "") -> dict:
    return {"Weapon Name": name, "Range": rng,
            "Heat": "", "Dice": "", "To-Hit": "", "AP": "", "Type": "",
            "Traits": traits}

def write_csv(path: pathlib.Path, weapons: list[dict]) -> None:
    seen: set[str] = set()
    rows: list[dict] = []
    for w in weapons:
        key = w["Weapon Name"].lower()
        if key not in seen:
            seen.add(key)
            rows.append(w)
    rows.sort(key=lambda r: r["Weapon Name"])
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {path}  ({len(rows)} weapons)")

# ═══════════════════════════════════════════════════════════════════════════════
# BATTLE ARMOR WEAPONS
# ═══════════════════════════════════════════════════════════════════════════════
# Ranges derive from WeaponRules.csv where an analog exists; estimates otherwise.
# "BA" is implicit in file context, so ISBA → "Inner Sphere", CLBA → "Clan".

BA: list[dict] = [

    # ── Melee ─────────────────────────────────────────────────────────────────
    R("Battle Armor Heavy Battle Claw",        "Melee"),
    R("Battle Armor Heavy Battle Claw (Vibro)", "Melee"),

    # ── Clan Energy ───────────────────────────────────────────────────────────
    R("Clan ER Micro Laser",        wr("Clan ER Micro Laser")        or '8"'),
    R("Clan ER Small Laser",        wr("Clan ER Small Laser")        or '8"'),
    R("Clan ER Small Pulse Laser",  wr("Clan ER Small Pulse Laser")  or '8"'),
    R("Clan ER Medium Laser",       wr("Clan ER Medium Laser")       or '14"'),
    R("Clan ER Medium Pulse Laser", wr("Clan ER Medium Pulse Laser") or '14"'),
    R("Clan Flamer",                wr("Clan Flamer")                or '6"'),
    R("Clan Heavy Flamer",          wr("Clan Heavy Flamer")          or '8"'),
    R("Clan Micro Pulse Laser",     wr("Clan Micro Pulse Laser")     or '6"'),
    R("Clan Small Laser",           wr("Clan Small Laser")           or '6"'),
    R("Clan Small Pulse Laser",     wr("Clan Small Pulse Laser")     or '8"'),
    R("Clan Medium Pulse Laser",    wr("Clan Medium Pulse Laser")    or '12"'),

    # ── Inner Sphere Energy ───────────────────────────────────────────────────
    R("Inner Sphere Small Laser",        wr("Inner Sphere Small Laser")        or '6"'),
    R("Inner Sphere Small Pulse Laser",  wr("Inner Sphere Small Pulse Laser")  or '6"'),
    R("Inner Sphere Small VSP Laser",    wr("Inner Sphere Small VSP Laser")    or '6"'),
    R("Inner Sphere Medium Laser",       wr("Inner Sphere Medium Laser")       or '8"'),
    R("Inner Sphere Medium Pulse Laser", wr("Inner Sphere Medium Pulse Laser") or '8"'),
    R("Inner Sphere Medium VSP Laser",   wr("Inner Sphere Medium VSP Laser")   or '8"'),
    R("Inner Sphere ER Small Laser",     wr("Inner Sphere ER Small Laser")     or '8"'),
    R("Inner Sphere ER Medium Laser",    wr("Inner Sphere ER Medium Laser")    or '12"'),
    R("Inner Sphere Plasma Rifle",       wr("Inner Sphere Plasma Rifle")       or '14"'),

    # ── Clan Ballistic ────────────────────────────────────────────────────────
    R("Clan AP Gauss Rifle",         wr("Clan AP Gauss Rifle")        or '8"'),
    R("Clan Machine Gun",            wr("Clan Machine Gun")           or '6"'),
    R("Clan Light Machine Gun",      wr("Clan Light Machine Gun")     or '8"'),
    R("Clan Heavy Machine Gun",      wr("Clan Heavy Machine Gun")     or '4"'),
    R("Clan Light Recoilless Rifle", '6"'),
    R("Clan Medium Recoilless Rifle",'8"'),
    R("Clan Heavy Recoilless Rifle", '10"'),

    # ── Inner Sphere Ballistic ────────────────────────────────────────────────
    # "MagShot" spelling in WeaponRules vs "Magshot" in raw tag — try both
    R("Inner Sphere Magshot Gauss Rifle",
        wr("Inner Sphere MagShot Gauss Rifle") or wr("Inner Sphere Magshot Gauss Rifle") or '8"'),
    R("Battle Armor David Light Gauss Rifle",        '8"'),
    R("Inner Sphere King David Light Gauss Rifle",   '8"'),
    R("Inner Sphere Tsunami Heavy Gauss Rifle",      '8"'),
    R("Inner Sphere Heavy Machine Gun",  wr("Inner Sphere Heavy Machine Gun") or '4"'),
    R("Inner Sphere Firedrake Needler",  '4"'),

    # ── Clan SRMs ─────────────────────────────────────────────────────────────
    R("Clan SRM 1",           '8"', "Special Ammo"),
    R("Clan SRM 2",           wr("Clan SRM 2") or '8"', "Special Ammo"),
    R("Clan SRM 3",           '8"', "Special Ammo"),
    R("Clan SRM 4",           wr("Clan SRM 4") or '8"', "Special Ammo"),
    R("Clan SRM 5",           '8"', "Special Ammo"),
    R("Clan SRM 6",           wr("Clan SRM 6") or '8"', "Special Ammo"),
    R("Clan SRM 1 (One Shot)",'8"', "Limited(1)"),
    R("Clan SRM 2 (One Shot)",'8"', "Limited(1)"),
    R("Clan SRM 3 (One Shot)",'8"', "Limited(1)"),
    R("Clan SRM 5 (One Shot)",'8"', "Limited(1)"),

    # Advanced SRM = Clan Streak-SRM analogue (homing, improved accuracy)
    R("Clan Advanced SRM 2",            wr("Clan Streak SRM 2") or '12"', "Special Ammo"),
    R("Clan Advanced SRM 2 (One Shot)", wr("Clan Streak SRM 2") or '12"', "Limited(1)"),
    R("Clan Advanced SRM 3",            '12"', "Special Ammo"),
    R("Clan Advanced SRM 4 (One Shot)", '12"', "Limited(1)"),
    R("Clan Advanced SRM 5",            '12"', "Special Ammo"),
    R("Clan Advanced SRM 6",            '12"', "Special Ammo"),

    # ── Clan LRMs ─────────────────────────────────────────────────────────────
    R("Clan LRM 3",            wr("Clan LRM 5") or '20"', "Special Ammo"),
    R("Clan LRM 4",            wr("Clan LRM 5") or '20"', "Special Ammo"),
    R("Clan LRM 2 (One Shot)", wr("Clan LRM 5") or '20"', "Limited(1), Special Ammo"),
    R("Clan LRM 5 (One Shot)", wr("Clan LRM 5") or '20"', "Limited(1), Special Ammo"),

    # ── Clan Grenade / Mortar ─────────────────────────────────────────────────
    R("Clan Heavy Grenade Launcher", '6"',       "Special Ammo"),
    R("Clan Micro Bomb",             '2"'),
    R("Clan Light Mortar",           '4"-12"',   "Special Ammo"),
    R("Clan Heavy Mortar",           '4"-16"',   "Special Ammo"),

    # ── Inner Sphere SRMs ─────────────────────────────────────────────────────
    R("Inner Sphere SRM 1",           '8"', "Special Ammo"),
    R("Inner Sphere SRM 2",           wr("Inner Sphere SRM 2") or '8"', "Special Ammo"),
    R("Inner Sphere SRM 3",           '8"', "Special Ammo"),
    R("Inner Sphere SRM 4",           wr("Inner Sphere SRM 4") or '8"', "Special Ammo"),
    R("Inner Sphere SRM 5",           '8"', "Special Ammo"),
    R("Inner Sphere SRM 6",           wr("Inner Sphere SRM 6") or '8"', "Special Ammo"),
    R("Inner Sphere SRM 1 (One Shot)",'8"', "Limited(1)"),
    R("Inner Sphere SRM 2 (One Shot)",'8"', "Limited(1)"),
    R("Inner Sphere SRM 3 (One Shot)",'8"', "Limited(1)"),
    R("Inner Sphere SRM 4 (One Shot)",'8"', "Limited(1)"),
    R("Inner Sphere SRM 5 (One Shot)",'8"', "Limited(1)"),
    R("Inner Sphere SRM 6 (One Shot)",'8"', "Limited(1)"),

    # ── Inner Sphere LRMs ─────────────────────────────────────────────────────
    R("Inner Sphere LRM 3",            wr("Inner Sphere LRM 5") or '4"-20"', "Special Ammo"),
    R("Inner Sphere LRM 5",            wr("Inner Sphere LRM 5") or '4"-20"', "Special Ammo"),
    R("Inner Sphere LRM 2 (One Shot)", wr("Inner Sphere LRM 5") or '4"-20"', "Limited(1), Special Ammo"),

    # ── Inner Sphere Grenade / Misc ───────────────────────────────────────────
    R("Inner Sphere Micro Grenade Launcher", '4"'),
    R("Battle Armor Mine Launcher",          '4"', "Special Ammo"),

    # ── TAG ───────────────────────────────────────────────────────────────────
    R("Clan Light TAG", '8"'),

    # ── Anti-Personnel Mount weapons (infantry small arms fired via APM) ──────
    # These match entries in InfantryWeapons.csv; included here because
    # many BA loadouts carry them via the BAAPMount slot.
    R("Assault Rifle",           '6"'),
    R("Laser Rifle (Mauser 960)",'8"'),
    R("Mauser IIC IAS Laser Rifle", '8"'),
]

# ═══════════════════════════════════════════════════════════════════════════════
# INFANTRY WEAPONS
# ═══════════════════════════════════════════════════════════════════════════════
# Ranges estimated from BattleTech Total Warfare infantry weapon tables
# (p.215–219) at the project's 1 hex = 2" ground-scale.
# Weapons appearing under both human-readable and InfantryXxx internal names
# in the corpus are deduplicated to a single canonical row.

INF: list[dict] = [

    # ── Assault Rifles / Carbines ─────────────────────────────────────────────
    R("Assault Rifle",                '6"'),
    R("Auto Rifle",                   '6"'),
    R("TK Assault Rifle",             '6"'),
    R("Gyrojet Rifle",                '6"'),
    R("Gyroslug Rifle",               '6"'),
    R("Rifle (Bolt-Action)",          '8"'),
    R("Sniper Rifle",                 '10"'),
    R("Sniper Rifle (Bolt Action)",   '12"'),
    R("Sniper Rifle (Hammel Marksman)",'12"'),
    R("Zeus Heavy Rifle",             '8"'),
    R("Federated Long Rifle",         '8"'),
    R("Federated-Barrett M42B",       '6"'),
    R("Imperator AX-22 Assault Rifle",'6"'),
    R("M&G G-150 Rifle",              '6"'),
    R("Elephant Gun",                 '8"'),

    # ── Submachine Guns / Pistols ─────────────────────────────────────────────
    R("Submachine Gun",        '4"'),
    R("Gunther MP-20 SMG",     '4"'),
    R("Auto-Pistol",           '2"'),
    R("Claymore Pistol",       '2"'),
    R("Needler Pistol",        '2"'),
    R("Auto-Shotgun",          '2"'),

    # ── Laser Rifles ──────────────────────────────────────────────────────────
    R("Laser Rifle",                         '8"'),
    R("ER Laser Rifle",                      '10"'),
    R("IS Pulse Laser Rifle",                '8"'),
    R("Blazer Laser Rifle",                  '8"'),
    R("Ebony Assault Laser Rifle",           '8"'),
    R("Federated-Barrett M61A Laser Rifle",  '8"'),
    R("Hellbore Assault Laser",              '8"'),
    R("Intek Laser Rifle",                   '8"'),
    R("Laser Pistol",                        '4"'),
    R("Magna Laser Rifle",                   '8"'),
    R("Marx XX Laser Rifle",                 '8"'),
    R("Mauser 960 Laser Rifle",              '8"'),
    R("Mauser 1200 LSS Laser Rifle",         '8"'),
    R("Mauser IIC IAS Laser Rifle",          '8"'),   # Clan variant
    R("Maxell PL-10 Laser Rifle",            '8"'),
    R("Minolta 9000 Laser Rifle",            '8"'),
    R("Sunbeam Starfire ER Laser Rifle",     '10"'),
    R("Support Laser",                       '10"'),
    R("Support Pulse Laser",                 '10"'),
    R("Heavy Laser (Infantry)",              '10"'),
    R("Clan ER Micro Laser (Infantry)",      '8"'),
    R("Clan ER Heavy Laser (Infantry)",      '14"'),
    R("Particle Cannon (Semi-Portable)",     '12"'),
    R("Support PPC (Snub-Nose)",             '8"'),
    R("Heavy PPC (Infantry)",               '12"'),

    # ── Machine Guns ──────────────────────────────────────────────────────────
    R("Machine Gun (Portable)", '6"'),
    R("Machine Gun (Support)",  '6"'),

    # ── Flamers ───────────────────────────────────────────────────────────────
    R("Flamer (Man-Portable)", '4"'),
    R("Heavy Flamer (Man-Pack)",'6"'),

    # ── Needler Rifles ────────────────────────────────────────────────────────
    R("Needler Rifle",                  '4"'),
    R("Firedrake Support Needler",      '4"'),
    R("M&G Flechette Needler Rifle",    '4"'),
    R("Shredder Heavy Needler Rifle",   '4"'),

    # ── Gauss Weapons ─────────────────────────────────────────────────────────
    R("Clan Gauss SMG",                    '4"'),
    R("David Light Gauss Rifle",           '8"'),
    R("King David Light Gauss Rifle",      '8"'),
    R("Tsunami Heavy Gauss Rifle",         '10"'),
    R("Grand Mauler Gauss Cannon",         '10"'),
    R("Gungnir Heavy Support Gauss Rifle", '12"'),
    R("Thunderstroke II Gauss Rifle",      '10"'),

    # ── Grenade Launchers ─────────────────────────────────────────────────────
    R("Grenade Launcher",                     '4"'),
    R("Compact Grenade Launcher",             '4"'),
    R("Auto Grenade Launcher",                '4"'),
    R("Auto Grenade Launcher (Inferno)",      '4"', "Special Ammo"),
    R("Heavy Grenade Launcher (Inferno)",     '4"', "Special Ammo"),
    R("Mini Grenade (Inferno)",               '2"', "Special Ammo"),

    # ── SRM Launchers ─────────────────────────────────────────────────────────
    R("Infantry SRM",                          '8"'),
    R("Infantry Standard SRM",                 '8"'),
    R("Infantry Standard SRM (Inferno)",       '8"', "Special Ammo"),
    R("Infantry Heavy SRM",                    '8"'),
    R("Infantry Light SRM",                    '8"'),
    R("Standard SRM Launcher (Two-Shot)",      '8"'),
    R("Heavy SRM Launcher (One Shot)",         '8"', "Limited(1)"),
    R("Light SRM Launcher",                    '8"'),

    # ── LRM / MRM Launchers ───────────────────────────────────────────────────
    R("Infantry LRM",          '20"', "Special Ammo"),
    R("FarShot LRM Launcher",  '20"', "Special Ammo"),
    R("Infantry One-Shot MRM", '14"', "Limited(1)"),

    # ── AA Weapons ────────────────────────────────────────────────────────────
    R("AA Weapon Mk.1 (Light)",        '8"'),
    R("AA Weapon Mk.2 (Man-Portable)", '8"'),

    # ── Support / Heavy ───────────────────────────────────────────────────────
    R("Bearhunter Superheavy Autocannon", '6"'),
    R("Portable Autocannon",             '8"'),
    R("Semi-Portable Autocannon",        '8"'),
    R("Plasma Rifle (Man-Portable)",     '8"'),
    R("Infantry MPPR",                   '8"'),   # Man-Portable Particle/Plasma Rifle

    # ── Recoilless Rifles ─────────────────────────────────────────────────────
    R("Light Recoilless Rifle",  '6"'),
    R("Medium Recoilless Rifle", '8"'),
    R("Heavy Recoilless Rifle",  '10"'),

    # ── Mortars ───────────────────────────────────────────────────────────────
    R("Light Mortar",  '4"-12"', "Special Ammo"),
    R("Heavy Mortar",  '4"-16"', "Special Ammo"),

    # ── Melee ─────────────────────────────────────────────────────────────────
    R("Avenger CCW",  "Melee"),
    R("Stunstick",    "Melee"),
    R("Vibroblade",   "Melee"),
    R("Vibro-katana", "Melee"),

    # ── Utility ───────────────────────────────────────────────────────────────
    R("Infantry TAG",       '12"'),
    R("VLAW",               '8"', "Limited(1)"),   # one-shot light AT rocket
    R("Tranquilizer Gun",   '4"'),
    R("Sonic Stunner",      '4"'),
]

# ── Write ──────────────────────────────────────────────────────────────────────
write_csv(OUT_DIR / "InfantryWeapons.csv",     INF)
write_csv(OUT_DIR / "BattleArmorWeapons.csv",  BA)

# ── Diagnostics: show which BA weapons used wr() fallbacks ───────────────────
print("\nRange cross-check (BA weapons resolved via WeaponRules.csv):")
for w in BA:
    found = wr_range.get(w["Weapon Name"].lower())
    if found:
        print(f"  ✓  {w['Weapon Name']:50s}  {w['Range']}")
