"""Generate output/detachments/detachments_battlearmor.json.

Reads .blk files from .cache/mm-data/data/mekfiles/battlearmor/**,
applies design rules from design/battlearmor.md, and outputs a
detachments JSON following the same schema as detachments_vehicle.json.

Key rules:
- heat_threshold: null  (BA/infantry omit heat entirely)
- armor_save: "5+"  (all BA)
- special_rules: Skimmer + CAF value
- CAF +4 if suit has any claw/manipulator EXCEPT mine-removal tool
- CAF +1 if only mine-removal, or no melee/manipulator gear
- detachment_size: Clan base=5/max=10, IS base=4/max=8
- points: round(BV / 10), BV from output/bv_cache.json keyed by mul_id
"""
from __future__ import annotations

import csv
import json
import pathlib
import re

# ── Paths ─────────────────────────────────────────────────────────────────────
BA_DIR    = pathlib.Path(".cache/mm-data/data/mekfiles/battlearmor")
OUT       = pathlib.Path("output/detachments/detachments_battlearmor.json")
BV_CACHE  = pathlib.Path("output/bv_cache.json")
AMMO_CSV  = pathlib.Path("data/AmmunitionRules.csv")
BA_WPNS   = pathlib.Path("data/reference/BattleArmorWeapons.csv")

OUT.parent.mkdir(parents=True, exist_ok=True)

# ── Load BV cache (keyed by mul_id as string) ─────────────────────────────────
bv_cache: dict[str, int] = {}
if BV_CACHE.exists():
    bv_cache = json.loads(BV_CACHE.read_text())
    print(f"Loaded BV cache: {len(bv_cache)} entries")

# ── Load BattleArmorWeapons.csv → valid display-name set + traits lookup ──────
ba_weapon_display: set[str] = set()          # valid display weapon names
ba_weapon_has_special_ammo: set[str] = set() # weapon names that take ammo
with BA_WPNS.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        name = row.get("Weapon Name", "").strip()
        traits = row.get("Traits", "").strip()
        if name:
            ba_weapon_display.add(name)
            if "Special Ammo" in traits:
                ba_weapon_has_special_ammo.add(name)

# ── Load AmmunitionRules.csv → ammo options keyed by weapon name ──────────────
ammo_by_weapon: dict[str, list[str]] = {}
if AMMO_CSV.exists():
    with AMMO_CSV.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            wname = row.get("Weapon Name", "").strip()
            aname = row.get("Ammo Name", "").strip()
            if wname and aname:
                ammo_by_weapon.setdefault(wname, [])
                if aname not in ammo_by_weapon[wname]:
                    ammo_by_weapon[wname].append(aname)

# ── Raw tag → display name mapping ───────────────────────────────────────────
# Covers the raw MegaMek tag names found in <Squad Equipment>/<Point Equipment>
RAW_TO_DISPLAY: dict[str, str] = {
    # ── Melee ────────────────────────────────────────────────────────────────
    "BAHeavyBattleClaw":          "Battle Armor Heavy Battle Claw",
    "BAHeavyBattleClawVibro":     "Battle Armor Heavy Battle Claw (Vibro)",
    "BABattleClaw":               "Battle Armor Battle Claw",
    "BABattleClawVibro":          "Battle Armor Battle Claw (Vibro)",
    "BABattleClawMagnets":        "Battle Armor Battle Claw (Magnets)",
    # ── Clan Energy ──────────────────────────────────────────────────────────
    "CLBAERMicroLaser":           "Clan ER Micro Laser",
    "CLBAERSmallLaser":           "Clan ER Small Laser",
    "CLBAERSmallPulseLaser":      "Clan ER Small Pulse Laser",
    "CLBAERMediumLaser":          "Clan ER Medium Laser",
    "BACLERMediumPulseLaser":     "Clan ER Medium Pulse Laser",
    "CLBAFlamer":                 "Clan Flamer",
    "CLBAHeavyFlamer":            "Clan Heavy Flamer",
    "CLBAMicroPulseLaser":        "Clan Micro Pulse Laser",
    "CLBASmall Laser":            "Clan Small Laser",
    "CLBASmallLaser":             "Clan Small Laser",
    "CLBASmallPulseLaser":        "Clan Small Pulse Laser",
    "CLBAMediumPulseLaser":       "Clan Medium Pulse Laser",
    # ── IS Energy ────────────────────────────────────────────────────────────
    "ISBASmallLaser":             "Small Laser",
    "ISBASmallPulseLaser":        "Small Pulse Laser",
    "ISBASmallVSPLaser":          "Small VSP Laser",
    "ISBAMediumLaser":            "Medium Laser",
    "ISBAMediumPulseLaser":       "Medium Pulse Laser",
    "ISBAMediumVSPLaser":         "Medium VSP Laser",
    "ISBAERSmallLaser":           "ER Small Laser",
    "ISBAERMediumLaser":          "ER Medium Laser",
    "ISBAPlasmaRifle":            "Plasma Rifle",
    # ── Clan Ballistic ────────────────────────────────────────────────────────
    "CLBAAPGaussRifle":           "Clan AP Gauss Rifle",
    "CLBAMG":                     "Clan Machine Gun",
    "CLBALightMG":                "Clan Light Machine Gun",
    "CLBAHeavyMG":                "Clan Heavy Machine Gun",
    "CLBAHeavy Recoilless Rifle": "Clan Heavy Recoilless Rifle",
    "CLBAMedium Recoilless Rifle":"Clan Medium Recoilless Rifle",
    "CLBALight Recoilless Rifle": "Clan Light Recoilless Rifle",
    # ── IS Ballistic ──────────────────────────────────────────────────────────
    "ISBAMagshotGaussRifle":      "Magshot Gauss Rifle",
    "BADavidLightGaussRifle":     "Battle Armor David Light Gauss Rifle",
    "ISBAKingDavidLightGaussRifle":"King David Light Gauss Rifle",
    "ISBATsunamiHeavyGaussRifle": "Tsunami Heavy Gauss Rifle",
    "ISBAHeavyMachineGun":        "Heavy Machine Gun",
    "ISBAFireDrakeNeedler":       "Firedrake Needler",
    # ── Clan SRMs ─────────────────────────────────────────────────────────────
    "CLBASRM1":                   "Clan SRM 1",
    "CLBASRM2":                   "Clan SRM 2",
    "CLBASRM3":                   "Clan SRM 3",
    "CLBASRM4":                   "Clan SRM 4",
    "CLBASRM5":                   "Clan SRM 5",
    "CLBASRM6":                   "Clan SRM 6",
    "CLBASRM1OS":                 "Clan SRM 1 (One Shot)",
    "CLBASRM2OS":                 "Clan SRM 2 (One Shot)",
    "CLBASRM2 (OS)":              "Clan SRM 2 (One Shot)",
    "CLBASRM3OS":                 "Clan SRM 3 (One Shot)",
    "CLBASRM3 (OS)":              "Clan SRM 3 (One Shot)",
    "CLBASRM4OS":                 "Clan SRM 4 (One Shot)",
    "CLBASRM5OS":                 "Clan SRM 5 (One Shot)",
    "CLBASRM6OS":                 "Clan SRM 6 (One Shot)",
    # Clan Advanced SRM (homing; analogous to Streak SRM)
    "CLAdvancedSRM2":             "Clan Advanced SRM 2",
    "CLAdvancedSRM2OS":           "Clan Advanced SRM 2 (One Shot)",
    "CLAdvancedSRM3":             "Clan Advanced SRM 3",
    "CLAdvancedSRM4OS":           "Clan Advanced SRM 4 (One Shot)",
    "CLAdvancedSRM5":             "Clan Advanced SRM 5",
    "CLAdvancedSRM6":             "Clan Advanced SRM 6",
    # ── Clan LRMs ─────────────────────────────────────────────────────────────
    "CLBALRM2OS":                 "Clan LRM 2 (One Shot)",
    "CLBALRM3":                   "Clan LRM 3",
    "CLBALRM4":                   "Clan LRM 4",
    "CLBALRM5":                   "Clan LRM 5 (One Shot)",   # always OS in data
    "CLBALRM5 (OS)":              "Clan LRM 5 (One Shot)",
    # ── Clan Grenade / Mortar ─────────────────────────────────────────────────
    "CLBAHeavyGrenadeLauncher":   "Clan Heavy Grenade Launcher",
    "CLBAMicroBomb":              "Clan Micro Bomb",
    "CLBAHeavyMortar":            "Clan Heavy Mortar",
    "CLBALightMortar":            "Clan Light Mortar",
    # ── IS SRMs ───────────────────────────────────────────────────────────────
    "ISBASRM1":                   "SRM 1",
    "ISBASRM2":                   "SRM 2",
    "ISBASRM3":                   "SRM 3",
    "ISBASRM4":                   "SRM 4",
    "ISBASRM5":                   "SRM 5",
    "ISBASRM6":                   "SRM 6",
    "ISBASRM1OS":                 "SRM 1 (One Shot)",
    "ISBASRM2OS":                 "SRM 2 (One Shot)",
    "ISBASRM3OS":                 "SRM 3 (One Shot)",
    "ISBASRM4OS":                 "SRM 4 (One Shot)",
    "ISBASRM5OS":                 "SRM 5 (One Shot)",
    "ISBASRM6OS":                 "SRM 6 (One Shot)",
    # ── IS LRMs ───────────────────────────────────────────────────────────────
    "ISBALRM2OS":                 "LRM 2 (One Shot)",
    "ISBALRM3":                   "LRM 3",
    "ISBALRM5":                   "LRM 5",
    # ── IS Grenade / Misc ─────────────────────────────────────────────────────
    "ISBAMicroGrenadeLauncher":   "Micro Grenade Launcher",
    "BAMineLauncher":             "Battle Armor Mine Launcher",
    # ── IS Missile / Rocket extras ─────────────────────────────────────────────
    "ISBASupportPPC":              "Support PPC",
    "ISBARL1":                    "Rocket Launcher 1",
    "ISBARL2":                    "Rocket Launcher 2",
    "ISBARL4":                    "Rocket Launcher 4",
    "ISBARL5":                    "Rocket Launcher 5",
    "ISBAMRM1":                   "Mini-Rocket Pod 1",
    "ISBAMRM2":                   "Mini-Rocket Pod 2",
    "ISBAMRM3":                   "Mini-Rocket Pod 3",
    "ISBAMRM5":                   "Mini-Rocket Pod 5",
    "ISBATubeArtillery":          "Tube Artillery",
    # ── Clan Missile extras ──────────────────────────────────────────────────────
    "CLBAMicroBombLauncher":       "Clan Micro Bomb",
    # ── Bearhunter Autocannon ────────────────────────────────────────────────────
    "Machine Gun (Bearhunter AC)": "Battle Armor Bearhunter Autocannon",
    # ── LB-X AC ─────────────────────────────────────────────────────────────────
    "Battle Armor LB-X AC":       "Battle Armor LB-X Autocannon",
    # ── Clan Energy extras ───────────────────────────────────────────────────────
    "CLBAHeavySmallLaser":        "Clan Heavy Small Laser",
    "CLBALightTAG":               "Clan Light TAG",
    # ── APM-mounted infantry weapons ──────────────────────────────────────────
    "InfantryAssaultRifle":       "Assault Rifle",
    "Laser Rifle (Mauser 960)":   "Laser Rifle (Mauser 960)",
    "Laser Rifle (Mauser IIC IAS)": "Mauser IIC IAS Laser Rifle",
    "InfantryClanMauserIICIAS":   "Mauser IIC IAS Laser Rifle",
    "Mauser IIC IAS":             "Mauser IIC IAS Laser Rifle",
}

# ── Equipment that is GEAR (not weapons) ──────────────────────────────────────
# Items in this set are skipped for weapons but used for CAF determination.
GEAR_SKIP: set[str] = {
    # Manipulators (tracked separately for CAF)
    "BABasicManipulator",
    "BAArmoredGlove",
    "BACuttingTorch",
    "BASalvageArm",
    # Mine clearance (CAF +1, not +4)
    "BABasicManipulatorMineClearance",
    # Mounts — weapon comes separately on a different line
    "BAAPMount",
    "ISDetachableWeaponPack",   # DWP mount; actual weapon listed with :DWP loc
    # Jump/mobility
    "BAJumpJet", "BAImprovedJumpJet", "BAVTOL", "BAUMU",
    "BAPartialWing", "BAMyomerBooster", "BAJumpBooster",
    # Utility
    "BASearchlight", "BARemoteSensor", "BAMagneticClamp",
    "BAMagneticClamps", "BAParaFoil", "BACargo",
    "BAMineDispenser",
    # Additional gear tags seen in the corpus
    "BAExtendedLifeSupport",
    "BAMechanicalJumpBooster",
    "BAIndustrialDrill",
    "BAMEA",                    # Multi-Environment Adaptation
    "BattleArmorC3",
    "BA-Magnetic Clamp",
    "BAParafoil",              # different capitalisation from BAParaFoil
    "CLBAMyomerBooster",       # Clan BA Myomer Booster
    "ISBASpaceOperationsAdaptation",
    "ISImprovedSensors",
    "CLImprovedSensors",
    "IS BA ECM",
    "IS BA LEOS",
    "Camo System",
    "ISBAHeatSensor",
    "ISBARemoteSensorDispenser",
    "BABloodhoundASP",
    "BACargoLifter",
    "CL BA ECM",
    "BAISAngelECMSuite",
    "Mission Equipment Storage",
    "ISBC3i",
    "ISBALightActiveProbe",
    "BAPowerpack",
    "HHSearchlight",
    "ISBAAPDS",
    "BABattleMechNIU",
    # Armor mods
    "IS BA Advanced",
    "IS BA Stealth (Basic)", "IS BA Stealth (Standard)", "IS BA Stealth (Improved)",
    "IS BA Mimetic",
    "IS BA Reactive (Blazer)",
    "IS BA Laser Reflective (Reflec/Glazed)",
    "Clan BA Laser Reflective (Reflec/Glazed)",
    "Clan BA Fire Resistant",
    "Clan BA Reactive (Blazer)",
    "Clan BA Stealth (Improved)",
    "Clan BA Stealth (Basic)",
    "Clan BA Stealth (Standard)",
    "Clan BA Stealth (Prototype)",
    "IS BA Stealth (Prototype)",
}

# ── Items that grant CAF +4 (manipulators / claws, excluding mine clearing) ───
CAF_PLUS_4_GEAR: set[str] = {
    "BABattleClaw", "BABattleClawVibro", "BABattleClawMagnets",
    "BAHeavyBattleClaw", "BAHeavyBattleClawVibro",
    "BABasicManipulator", "BAArmoredGlove", "BACuttingTorch",
    "BASalvageArm",
}
# Mine clearance grants only CAF +1
CAF_MINE_ONLY: set[str] = {"BABasicManipulatorMineClearance"}

# ── Ammo-only lines (skip entirely) ───────────────────────────────────────────
AMMO_RE = re.compile(
    r"^(BA-SRM|BA-Advanced SRM|BACL Ammo|IS BA Ammo|Clan Ammo|IS Ammo|"
    r"BA-LRM|IS MRM|Ammo )"
    r"|Ammo$|\bAmmo\b.*Shots|\bAmmo\b",
    re.IGNORECASE,
)

# ── Helper: slugify ────────────────────────────────────────────────────────────
def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

# ── Helper: year → era ────────────────────────────────────────────────────────
def year_to_era(year: int | None) -> str:
    if year is None:
        return "Unknown"
    if year < 2300: return "Early"
    if year < 2780: return "Star League"
    if year < 3049: return "Succession Wars"
    if year < 3060: return "Clan Invasion"
    if year < 3067: return "FedCom Civil War"
    if year < 3080: return "Jihad"
    if year < 3150: return "Dark Age"
    return "IlClan"

# ── Helper: weight class → tier ───────────────────────────────────────────────
_TIER = {0: "light", 1: "light", 2: "medium", 3: "heavy", 4: "assault"}

def wc_to_tier(wc: int | None) -> str:
    return _TIER.get(wc or 0, "light")

# ── Helper: parse tag-block file ──────────────────────────────────────────────
TAG_RE = re.compile(r"<([^>/\s][^>]*)>\s*\n(.*?)\n</\1>", re.DOTALL)

def parse_blk(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    out: dict = {}
    for m in TAG_RE.finditer(text):
        tag = m.group(1).strip()
        body = m.group(2).strip()
        if "\n" in body:
            out[tag] = [ln.strip() for ln in body.splitlines() if ln.strip()]
        else:
            out[tag] = body
    return out

# ── Helper: get equipment lines from unit ─────────────────────────────────────
def get_equipment(unit: dict) -> list[str]:
    eq = unit.get("Squad Equipment") or unit.get("Point Equipment")
    if not eq:
        for i in range(1, 7):
            eq = unit.get(f"Trooper {i} Equipment")
            if eq:
                break
    if isinstance(eq, str):
        return [eq] if eq else []
    return list(eq) if eq else []

def get_slotless(unit: dict) -> list[str]:
    sl = unit.get("slotless_equipment")
    if isinstance(sl, str):
        return [sl] if sl else []
    return list(sl) if sl else []

# ── Helper: parse one equipment line → (raw_name, location) ──────────────────
def parse_eq_line(line: str) -> tuple[str, str]:
    """Return (raw_name, location).  Strips Shots# suffix from ammo lines."""
    # Remove shot counts: ':Shots4#' etc.
    line = re.sub(r":Shots\d+#?$", "", line.strip())
    parts = line.split(":", 1)
    raw = parts[0].strip()
    loc = parts[1].strip() if len(parts) > 1 else ""
    return raw, loc

# ── Helper: tech base ─────────────────────────────────────────────────────────
def tech_base(unit: dict) -> str:
    t = (unit.get("type") or "").lower()
    return "Clan" if t.startswith("clan") else "Inner Sphere"

# ── Helper: movement string ───────────────────────────────────────────────────
def movement_str(unit: dict) -> str:
    motion = (unit.get("motion_type") or "Leg").strip()
    try:
        cruise = int(str(unit.get("cruiseMP") or 1).strip())
    except ValueError:
        cruise = 1
    try:
        jump = int(str(unit.get("jumpingMP") or 0).strip())
    except ValueError:
        jump = 0
    if motion in ("Jump", "VTOL") and jump > 0:
        return f'{jump * 2}"'
    if motion == "UMU" and jump > 0:
        return f'{jump * 2}" (UMU)'
    return f'{cruise * 2}"'

# ── Helper: build ammo upgrades for a weapon display name ─────────────────────
def ammo_upgrades(weapon_name: str) -> list[dict]:
    """Map BA weapon to the closest standard weapon for ammo lookup."""
    # Direct match
    if weapon_name in ammo_by_weapon:
        return [{"ammo_name": a, "weapon_name": weapon_name, "points": 5}
                for a in ammo_by_weapon[weapon_name]]
    # Map BA SRM 1/3/5 → SRM 2/4/6
    for ba, std in [
        ("Clan SRM 1", "Clan SRM 2"), ("Clan SRM 3", "Clan SRM 2"),
        ("Clan SRM 5", "Clan SRM 6"), ("Clan SRM 4", "Clan SRM 4"),
        ("Clan Advanced SRM 2", "Clan SRM 2"),
        ("Clan Advanced SRM 3", "Clan SRM 2"),
        ("Clan Advanced SRM 5", "Clan SRM 6"),
        ("Clan Advanced SRM 6", "Clan SRM 6"),
        ("Clan LRM 3", "Clan LRM 5"), ("Clan LRM 4", "Clan LRM 5"),
        ("SRM 1", "SRM 2"),
        ("SRM 3", "SRM 2"),
        ("SRM 5", "SRM 6"),
        ("LRM 3", "LRM 5"),
    ]:
        if weapon_name == ba and std in ammo_by_weapon:
            return [{"ammo_name": a, "weapon_name": weapon_name, "points": 5}
                    for a in ammo_by_weapon[std]]
    return []

# ── Helper: pluralise weapon for bullets list ─────────────────────────────────
_NUMS = ["", "Two ", "Three ", "Four ", "Five ", "Six "]

def pluralise_bullet(name: str, count: int) -> str:
    if count <= 1:
        return name
    prefix = _NUMS[count] if count < len(_NUMS) else f"{count}× "
    return prefix + name

# ── Main build loop ───────────────────────────────────────────────────────────
files = sorted(BA_DIR.rglob("*.blk"))
print(f"Processing {len(files)} .blk files …")

detachments: list[dict] = []
unmapped_counts: dict[str, int] = {}
skipped_ammo_lines = 0

for path in files:
    unit = parse_blk(path)

    if (unit.get("UnitType") or unit.get("unit type") or "").strip() not in (
        "BattleArmor", ""
    ):
        continue  # skip non-BA entries

    name_raw  = (unit.get("Name") or "").strip()
    model_raw = (unit.get("Model") or "").strip()
    full_name = f"{name_raw} {model_raw}".strip() if model_raw else name_raw

    mul_id = (unit.get("mul id:") or "").strip()
    try:
        year = int(str(unit.get("year") or 0).strip())
    except ValueError:
        year = None
    try:
        wc = int(str(unit.get("weightclass") or 0).strip())
    except ValueError:
        wc = 0

    tb = tech_base(unit)

    # ── BV → points ──────────────────────────────────────────────────────────
    bv = bv_cache.get(mul_id) if mul_id else None
    points = round(bv / 10) if bv and bv > 0 else None

    # ── Detachment size ───────────────────────────────────────────────────────
    if tb == "Clan":
        det_base, det_max = 5, 10
    else:
        det_base, det_max = 4, 8

    # ── Parse equipment ───────────────────────────────────────────────────────
    eq_lines  = get_equipment(unit)
    slotless  = get_slotless(unit)
    all_gear  = eq_lines + slotless

    weapons_list: list[dict] = []   # for JSON
    weapon_counts: dict[str, int] = {}

    has_caf4_gear   = False  # true if any claw/manipulator (non mine-clearing)
    has_mine_only   = False  # true if ONLY mine-clearing manipulator present
    any_manipulator = False  # any manipulator or claw at all

    for line in all_gear:
        if not line.strip():
            continue
        raw, loc = parse_eq_line(line)

        # Skip ammo-only lines
        if AMMO_RE.search(raw) or raw.endswith(" Ammo"):
            skipped_ammo_lines += 1
            continue

        # CAF tracking
        if raw in CAF_PLUS_4_GEAR:
            has_caf4_gear = True
            any_manipulator = True
        if raw in CAF_MINE_ONLY:
            any_manipulator = True
            # mine only — doesn't grant +4

        # Skip gear that isn't a weapon in the weapon list
        if raw in GEAR_SKIP:
            continue

        # Translate raw name → display name
        display = RAW_TO_DISPLAY.get(raw)
        if display is None:
            # Mark unmapped but still include if it looks weapon-like
            unmapped_counts[raw] = unmapped_counts.get(raw, 0) + 1
            mapped = False
        else:
            mapped = display in ba_weapon_display

        if display is None:
            continue  # truly unknown — skip

        weapon_counts[display] = weapon_counts.get(display, 0) + 1
        weapons_list.append({
            "name":           display,
            "raw_ref":        raw + (f":{loc}" if loc else ""),
            "mount_location": loc or None,
            "traits_added":   [],
            "unmapped":       not mapped,
        })

    # Deduplicate weapons_list preserving order (keep first occurrence)
    seen_wpn: set[str] = set()
    deduped: list[dict] = []
    for w in weapons_list:
        if w["name"] not in seen_wpn:
            seen_wpn.add(w["name"])
            deduped.append(w)
    weapons_list = deduped

    # ── CAF determination ─────────────────────────────────────────────────────
    caf = 4 if has_caf4_gear else 1

    # ── Build weapons_bulleted ────────────────────────────────────────────────
    weapons_bulleted = [
        pluralise_bullet(w["name"], weapon_counts[w["name"]])
        for w in weapons_list
    ]

    # ── Special ammo upgrade options ──────────────────────────────────────────
    special_ammo: list[dict] = []
    for w in weapons_list:
        if w["name"] in ba_weapon_has_special_ammo and not w["unmapped"]:
            opts = ammo_upgrades(w["name"])
            for o in opts:
                if o not in special_ammo:
                    special_ammo.append(o)

    # ── Detachment size upgrade ───────────────────────────────────────────────
    if tb == "Clan":
        upgrade_size_add = 5
    else:
        upgrade_size_add = 4
    upgrade_cost = (points * upgrade_size_add) if points else None
    detachment_size_upgrades = [{"add": upgrade_size_add, "cost": upgrade_cost}]

    # ── Assemble detachment entry ─────────────────────────────────────────────
    det_id = slugify(full_name)
    detachments.append({
        "id":             det_id,
        "name":           full_name,
        "detachment":     "Clan Star" if tb == "Clan" else "Inner Sphere Company",
        "unit_type":      "Battle Armor",
        "scale":          1,
        "tier":           wc_to_tier(wc),
        "tech_base":      tb,
        "era":            year_to_era(year),
        "tonnage":        None,
        "armor_save":     "5+",
        "movement":       movement_str(unit),
        "heat_threshold": None,         # BA omits heat mechanic entirely
        "wounds":         1,
        "detachment_size": {"base": det_base, "max": det_max},
        "points":         points,
        "weapons_bulleted": weapons_bulleted,
        "weapons":        weapons_list,
        "upgrade_options": {
            "special_ammo":    special_ammo,
            "detachment_size": detachment_size_upgrades,
        },
        "caf":            f"+{caf}",
        "morale":         "3+",
        "special_rules":  ["Skimmer", f"CAF: +{caf}"],
    })

# ── Sort & write ──────────────────────────────────────────────────────────────
detachments.sort(key=lambda d: (d["tech_base"], d["name"]))

with OUT.open("w", encoding="utf-8") as f:
    json.dump(detachments, f, indent=2, ensure_ascii=False)

print(f"\nWrote {len(detachments)} Battle Armor detachments → {OUT}")
print(f"  Skipped ammo-only equipment lines: {skipped_ammo_lines}")
if unmapped_counts:
    top = sorted(unmapped_counts.items(), key=lambda kv: -kv[1])[:20]
    print(f"\n  Top unmapped raw equipment names:")
    for nm, cnt in top:
        print(f"    {cnt:4d}  {nm}")

# ── Quick stats ───────────────────────────────────────────────────────────────
with_points    = sum(1 for d in detachments if d["points"] is not None)
clan_count     = sum(1 for d in detachments if d["tech_base"] == "Clan")
is_count       = sum(1 for d in detachments if d["tech_base"] == "Inner Sphere")
caf4_count     = sum(1 for d in detachments if "CAF: +4" in d["special_rules"])
caf1_count     = sum(1 for d in detachments if "CAF: +1" in d["special_rules"])
no_weapons     = sum(1 for d in detachments if not d["weapons"])
print(f"\n  Clan: {clan_count}  |  Inner Sphere: {is_count}")
print(f"  Points resolved: {with_points}/{len(detachments)}")
print(f"  CAF +4: {caf4_count}  |  CAF +1: {caf1_count}")
print(f"  Entries with no weapons: {no_weapons}")
