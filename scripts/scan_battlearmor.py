"""Scan BattleArmor .blk files from the local mm-data sparse clone.

Looks under ``.cache/mm-data/data/mekfiles/battlearmor`` (sparse-checked
out from https://github.com/MegaMek/mm-data) and writes
``battlearmor_overview.json`` next to ``infantry_overview.json``.
"""
from __future__ import annotations
import json, pathlib, re, collections

ROOT = pathlib.Path(".cache/mm-data/data/mekfiles/battlearmor")
files = list(ROOT.rglob("*.blk"))
print("battlearmor files:", len(files))

TAG_RE = re.compile(r"<([^>/\s][^>]*)>\s*\n(.*?)\n</\1>", re.DOTALL)

def parse(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    out: dict = {"_path": str(path)}
    for m in TAG_RE.finditer(text):
        tag = m.group(1).strip()
        body = m.group(2).strip()
        # Multi-line lists vs single value
        if "\n" in body:
            out[tag] = [ln.strip() for ln in body.splitlines() if ln.strip()]
        else:
            out[tag] = body
    return out

units = [parse(f) for f in files]

def tb(u: dict) -> str:
    raw = (u.get("type") or "").lower()
    return "Clan" if raw.startswith("clan") else "Inner Sphere"

clan = [u for u in units if tb(u) == "Clan"]
is_  = [u for u in units if tb(u) == "Inner Sphere"]
print("Clan", len(clan), "IS", len(is_))

def to_int(v) -> int | None:
    try:
        return int(str(v).strip())
    except (TypeError, ValueError):
        return None

def collect_int(units, key):
    out = []
    for u in units:
        v = to_int(u.get(key))
        if v is not None:
            out.append(v)
    return out

for label, group in [("Clan", clan), ("IS", is_)]:
    for k in ("Trooper Count", "weightclass", "cruiseMP", "jumpingMP"):
        vals = collect_int(group, k)
        if vals:
            print(f"{label} {k}: min={min(vals)} max={max(vals)} median={sorted(vals)[len(vals)//2]} n={len(vals)}")

def col(units, key):
    c = collections.Counter()
    for u in units:
        v = u.get(key)
        if isinstance(v, list):
            v = ", ".join(v)
        if v:
            c[str(v).strip()] += 1
    return c

# Equipment: weapons vs gear vs armor mods
WEAPON_HINTS = ("Rifle", "MG", "MachineGun", "Cannon", "SRM", "LRM", "Laser",
                "Plasma", "Flamer", "Gauss", "Rocket", "Mortar", "Grenade",
                "Bomb", "TAG", "Recoilless", "Mine", "Pulse", "Heavy Recoilless",
                "Light Recoilless", "Medium Recoilless", "Magshot", "Rifleman",
                "BAFireDrake", "BAGrandMauler", "BAKingDavid", "BAHeavy",
                "BALight", "Inferno", "InfernoSRM", "Infantry")
EQUIPMENT_NON_WEAPON = ("Manipulator", "MyomerBooster", "JumpJet", "ImprovedJumpJet",
                        "MountingBars", "AntiPersonnelMount", "Anti-Personnel Mount",
                        "Stealth", "Mimetic", "MagneticClamp", "MagneticClamps",
                        "ParaFoil", "MissionEquipment", "Searchlight",
                        "RemoteSensor", "PartialWing", "Cargo", "Detachable",
                        "MineDispenser", "Camo", "Battle Claw", "Claws",
                        "Battle Claws", "Battle Claw (Magnets)",
                        "Battle Claw (Vibro)", "BAJumpJet", "BAVTOL",
                        "BAUMU", "BAManipulator", "BAArmor")

def split_equipment(unit):
    weapons = []
    gear = []
    # IS uses <Squad Equipment>, Clan uses <Point Equipment>; some fall back
    # to <Trooper N Equipment>. Pull from whichever block is populated.
    eq = unit.get("Squad Equipment") or unit.get("Point Equipment") or []
    if not eq:
        for i in range(1, 7):
            block = unit.get(f"Trooper {i} Equipment")
            if block:
                eq = block
                break
    if isinstance(eq, str):
        eq = [eq]
    for line in eq:
        name = line.split(":", 1)[0].strip()
        if not name:
            continue
        # Heuristic: weapon if matches weapon hints and not in non-weapon list
        is_gear = any(g.lower() in name.lower() for g in EQUIPMENT_NON_WEAPON)
        is_weapon = any(w.lower() in name.lower() for w in WEAPON_HINTS)
        if is_gear and not is_weapon:
            gear.append(name)
        elif is_weapon:
            weapons.append(name)
        else:
            gear.append(name)
    return weapons, gear

weapons_clan = collections.Counter()
weapons_is   = collections.Counter()
gear_clan    = collections.Counter()
gear_is      = collections.Counter()
for u in clan:
    w, g = split_equipment(u)
    for x in w: weapons_clan[x] += 1
    for x in g: gear_clan[x] += 1
for u in is_:
    w, g = split_equipment(u)
    for x in w: weapons_is[x] += 1
    for x in g: gear_is[x] += 1

def squad_summary(units):
    out = []
    for u in units:
        w, g = split_equipment(u)
        out.append({
            "name": u.get("Name"),
            "model": u.get("Model", ""),
            "motion": u.get("motion_type"),
            "cruise_mp": u.get("cruiseMP"),
            "jump_mp": u.get("jumpingMP"),
            "trooper_count": u.get("Trooper Count"),
            "weightclass": u.get("weightclass"),
            "role": u.get("role"),
            "year": u.get("year"),
            "weapons": sorted(set(w)),
            "gear": sorted(set(g)),
        })
    return out

# Weight class meaning per TacOps p.318: 0=PA(L), 1=Light, 2=Medium, 3=Heavy, 4=Assault
WEIGHTCLASS_LABELS = {
    "0": "PA(L) (≤ 0.4 t)",
    "1": "Light (0.5–0.75 t)",
    "2": "Medium (0.8–1.0 t)",
    "3": "Heavy (1.05–1.5 t)",
    "4": "Assault (1.55–2.0 t)",
}

def weightclass_dist(units):
    c = col(units, "weightclass")
    return [(WEIGHTCLASS_LABELS.get(k, f"Unknown ({k})"), n) for k, n in c.most_common()]

out = {
    "totals": {"Clan": len(clan), "IS": len(is_), "files": len(files)},
    "platoon_ranges": {
        label: {
            k: (lambda v: {"min": min(v) if v else None,
                            "max": max(v) if v else None,
                            "n": len(v)})(collect_int(grp, k))
            for k in ("Trooper Count", "weightclass", "cruiseMP", "jumpingMP")
        }
        for label, grp in [("Clan", clan), ("IS", is_)]
    },
    "motion_clan": col(clan, "motion_type").most_common(),
    "motion_is": col(is_, "motion_type").most_common(),
    "roles_clan": col(clan, "role").most_common(),
    "roles_is": col(is_, "role").most_common(),
    "weightclass_clan": weightclass_dist(clan),
    "weightclass_is": weightclass_dist(is_),
    "weapons_clan": weapons_clan.most_common(),
    "weapons_is": weapons_is.most_common(),
    "gear_clan": gear_clan.most_common(),
    "gear_is": gear_is.most_common(),
    "squads_clan": squad_summary(clan),
    "squads_is": squad_summary(is_),
}
pathlib.Path("battlearmor_overview.json").write_text(json.dumps(out, indent=2))
print("wrote battlearmor_overview.json")
