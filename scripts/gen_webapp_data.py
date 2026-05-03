"""Generate output/webapp/ data files for the web app.

Produces:
    output/webapp/units-meta.json  - lightweight search index (all unit types)
    output/webapp/weapons.json     - weapon profiles keyed by name
    output/webapp/ammo.json        - ammo profiles keyed by "AmmoName|WeaponName"
"""
from __future__ import annotations

import csv
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent.parent
OUTPUT = ROOT / "output" / "webapp"
DETACHMENTS = ROOT / "output" / "detachments"

# Fields kept in the lightweight meta index (everything else is in the per-type files)
_META_FIELDS = {
    "id", "name", "unit_type", "tier", "tech_base", "era",
    "tonnage", "points", "armor_save", "movement", "wounds", "heat_threshold",
}

_UNIT_FILES = {
    "mech": DETACHMENTS / "detachments_mech.json",
    "vehicle": DETACHMENTS / "detachments_vehicle.json",
    "aerospace": DETACHMENTS / "detachments_aerospace.json",
}


def _load_detachments() -> list[dict]:
    units: list[dict] = []
    for unit_type, path in _UNIT_FILES.items():
        if not path.exists():
            print(f"  WARNING: {path} not found, skipping", file=sys.stderr)
            continue
        records = json.loads(path.read_text(encoding="utf-8"))
        print(f"  {unit_type}: {len(records)} records")
        units.extend(records)
    return units


def _build_units_meta(units: list[dict]) -> list[dict]:
    meta = []
    for u in units:
        entry = {k: u.get(k) for k in _META_FIELDS}
        meta.append(entry)
    return meta


def _load_weapons() -> dict[str, dict]:
    weapons: dict[str, dict] = {}
    path = ROOT / "data" / "WeaponRules.csv"
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            name = row.get("Weapon Name", "").strip()
            if not name:
                continue
            traits_raw = row.get("Traits", "").strip()
            traits = [t.strip() for t in traits_raw.split(",") if t.strip()] if traits_raw else []
            weapons[name] = {
                "name": name,
                "range": row.get("Range", "").strip(),
                "heat": _int_or_none(row.get("Heat", "")),
                "dice": _int_or_none(row.get("Dice", "")),
                "to_hit": row.get("To-Hit", "").strip(),
                "ap": _int_or_none(row.get("AP", "")),
                "type": row.get("Type", "").strip(),
                "traits": traits,
            }
    return weapons


def _load_ammo() -> dict[str, dict]:
    ammo: dict[str, dict] = {}
    path = ROOT / "data" / "AmmunitionRules.csv"
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ammo_name = row.get("Ammo Name", "").strip()
            weapon_name = row.get("Weapon Name", "").strip()
            if not ammo_name or not weapon_name:
                continue
            key = f"{ammo_name}|{weapon_name}"
            traits_raw = row.get("Traits", "").strip()
            traits = [t.strip() for t in traits_raw.split(",") if t.strip()] if traits_raw else []
            dice_raw = (row.get("Dice") or row.get("Dice ", "") or "").strip()
            ammo[key] = {
                "ammo_name": ammo_name,
                "weapon_name": weapon_name,
                "range": row.get("Range", "").strip(),
                "heat": _int_or_none(row.get("Heat", "")),
                "dice": _int_or_none(dice_raw),
                "to_hit": row.get("To-Hit", "").strip(),
                "ap": _int_or_none(row.get("AP", "")),
                "type": row.get("Type", "").strip(),
                "traits": traits,
                "points": _int_or_none(row.get("Points", "")),
            }
    return ammo


def _int_or_none(s: str | None) -> int | None:
    if s is None:
        return None
    s = str(s).strip()
    try:
        return int(s)
    except ValueError:
        return None


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)

    print("Loading detachments...")
    units = _load_detachments()
    print(f"  Total: {len(units)} units")

    print("Building units-meta.json...")
    meta = _build_units_meta(units)
    (OUTPUT / "units-meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"  Wrote {len(meta)} entries")

    print("Building units-mech.json...")
    mechs = [u for u in units if (u.get("unit_type") or "").lower() in ("mech", "battlemech")]
    (OUTPUT / "units-mech.json").write_text(
        json.dumps(mechs, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"  Wrote {len(mechs)} mech entries")

    print("Building units-vehicle.json...")
    vehicles = [u for u in units if (u.get("unit_type") or "").lower() == "vehicle"]
    (OUTPUT / "units-vehicle.json").write_text(
        json.dumps(vehicles, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"  Wrote {len(vehicles)} vehicle entries")

    print("Building units-aerospace.json...")
    aerospace = [u for u in units if (u.get("unit_type") or "").lower() == "aerospace"]
    (OUTPUT / "units-aerospace.json").write_text(
        json.dumps(aerospace, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"  Wrote {len(aerospace)} aerospace entries")

    print("Building weapons.json...")
    weapons = _load_weapons()
    (OUTPUT / "weapons.json").write_text(
        json.dumps(weapons, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"  Wrote {len(weapons)} weapon profiles")

    print("Building ammo.json...")
    ammo = _load_ammo()
    (OUTPUT / "ammo.json").write_text(
        json.dumps(ammo, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    print(f"  Wrote {len(ammo)} ammo entries")

    print("Done. Output:", OUTPUT)


if __name__ == "__main__":
    main()
