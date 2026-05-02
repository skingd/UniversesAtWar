"""Tests for src.detachments.weapons."""
from __future__ import annotations

from pathlib import Path

import pytest

from src.datacheck.alias_resolver import build_alias_index
from src.detachments.weapons import (
    AmmoOption,
    WeaponProfile,
    build_weapon_index,
    load_ammunition_rules,
    load_weapon_rules,
)


WEAPON_CSV = (
    'Weapon Name,Range,Heat,Dice,To-Hit,AP,Type,Traits\r\n'
    'Clan AP Gauss Rifle,"8""",0,2,5+,-1,Ballistic,"Light, Rapid Fire"\r\n'
    'Inner Sphere Medium Laser,"6""",3,2,4+,-1,Energy,\r\n'
    'PPC,"12""",10,3,3+,-2,Energy,Heavy\r\n'
)

AMMO_CSV = (
    'Ammo Name,Weapon Name,Range,Heat,Dice,To-Hit,AP,Type,Traits,Points\r\n'
    'ER,Clan ATM 3,"2""-14""",1,1,4+,-2,Missile,Anti-Tank,5\r\n'
    'HE,Clan ATM 3,"2""-9""",1,2,4+,-3,Missile,,3\r\n'
)


@pytest.fixture
def weapon_csv_path(tmp_path: Path) -> Path:
    p = tmp_path / "WeaponRules.csv"
    p.write_text(WEAPON_CSV, encoding="utf-8")
    return p


@pytest.fixture
def ammo_csv_path(tmp_path: Path) -> Path:
    p = tmp_path / "AmmunitionRules.csv"
    p.write_text(AMMO_CSV, encoding="utf-8")
    return p


class TestLoadWeaponRules:
    def test_parses_all_rows(self, weapon_csv_path):
        profs = load_weapon_rules(weapon_csv_path)
        assert len(profs) == 3
        names = {p.name for p in profs}
        assert names == {"Clan AP Gauss Rifle", "Inner Sphere Medium Laser", "PPC"}

    def test_traits_split(self, weapon_csv_path):
        profs = load_weapon_rules(weapon_csv_path)
        ap = next(p for p in profs if p.name == "Clan AP Gauss Rifle")
        assert ap.traits == ["Light", "Rapid Fire"]
        ml = next(p for p in profs if p.name == "Inner Sphere Medium Laser")
        assert ml.traits == []
        ppc = next(p for p in profs if p.name == "PPC")
        assert ppc.traits == ["Heavy"]

    def test_numeric_fields(self, weapon_csv_path):
        profs = load_weapon_rules(weapon_csv_path)
        ap = next(p for p in profs if p.name == "Clan AP Gauss Rifle")
        assert ap.heat == 0
        assert ap.dice == 2
        assert ap.ap == -1
        assert ap.to_hit == "5+"
        assert ap.type == "Ballistic"

    def test_skips_blank_rows(self, tmp_path):
        p = tmp_path / "w.csv"
        p.write_text("Weapon Name,Range,Heat,Dice,To-Hit,AP,Type,Traits\n,,,,,,,\n", encoding="utf-8")
        assert load_weapon_rules(p) == []


class TestLoadAmmunitionRules:
    def test_groups_by_weapon(self, ammo_csv_path):
        d = load_ammunition_rules(ammo_csv_path)
        assert list(d.keys()) == ["Clan ATM 3"]
        assert len(d["Clan ATM 3"]) == 2
        names = {a.name for a in d["Clan ATM 3"]}
        assert names == {"ER", "HE"}

    def test_points_optional(self, ammo_csv_path):
        d = load_ammunition_rules(ammo_csv_path)
        er = next(a for a in d["Clan ATM 3"] if a.name == "ER")
        assert er.points == 5


class TestWeaponIndexResolve:
    def test_direct_name_lookup(self, weapon_csv_path):
        profs = load_weapon_rules(weapon_csv_path)
        idx = build_weapon_index(profs)
        prof, kind = idx.resolve("PPC")
        assert prof is not None
        assert prof.name == "PPC"
        assert kind == "name"

    def test_tech_prefix_strip(self, weapon_csv_path):
        profs = load_weapon_rules(weapon_csv_path)
        idx = build_weapon_index(profs)
        # raw "Medium Laser; Inner Sphere" → parse_reference strips the tech
        # suffix, leaving "Medium Laser". Our CSV name is "Inner Sphere
        # Medium Laser" — so direct normalize won't match. But we register
        # the canonical_id route (when alias_index given) and the tech
        # prefix-strip fallback. Without an alias index, we expect the
        # bare-name lookup to miss for this csv (since the CSV name has
        # the prefix). Verify the fallback tech-prefix strip matches when
        # the CSV uses the bare name.
        prof, kind = idx.resolve("Inner Sphere PPC")
        assert prof is not None and prof.name == "PPC"
        assert kind == "name"

    def test_ammo_filtered(self, weapon_csv_path):
        profs = load_weapon_rules(weapon_csv_path)
        idx = build_weapon_index(profs)
        prof, kind = idx.resolve("Ammo PPC")
        assert prof is None
        assert kind == "ammo"

    def test_miss(self, weapon_csv_path):
        profs = load_weapon_rules(weapon_csv_path)
        idx = build_weapon_index(profs)
        prof, kind = idx.resolve("Mystery Cannon Mk.IV")
        assert prof is None
        assert kind == "miss"

    def test_canonical_route(self, weapon_csv_path):
        # Equipment record has display_name matching CSV but a tech prefix
        # variant of the raw ref should still resolve via alias_index→canonical.
        equipment_records = [{
            "canonical_id": "ppc",
            "display_name": "PPC",
            "tech_base": "Inner Sphere",
        }]
        profs = load_weapon_rules(weapon_csv_path)
        idx = build_weapon_index(profs, equipment_records=equipment_records)
        alias = build_alias_index(equipment_records)
        prof, kind = idx.resolve("PPC; Inner Sphere", alias_index=alias)
        assert prof is not None
        assert prof.name == "PPC"
        assert kind == "canonical"
