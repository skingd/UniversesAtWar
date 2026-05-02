"""Tests for src.detachments.assemble."""
from __future__ import annotations

import pytest

from src.detachments.assemble import (
    Coverage,
    build_all,
    build_detachment,
)
from src.detachments.weapons import (
    AmmoOption,
    WeaponProfile,
    build_weapon_index,
)


@pytest.fixture
def weapon_index():
    return build_weapon_index([
        WeaponProfile(name="AC/20", range='8"', heat=7, dice=4,
                      to_hit="4+", ap=-3, type="Ballistic", traits=["Heavy"]),
        WeaponProfile(name="Medium Laser", range='6"', heat=3, dice=2,
                      to_hit="4+", ap=-1, type="Energy", traits=[]),
        WeaponProfile(name="LRM 20", range='14"', heat=6, dice=4,
                      to_hit="5+", ap=0, type="Missile", traits=["Indirect"]),
        WeaponProfile(name="SRM 6", range='4"', heat=4, dice=3,
                      to_hit="4+", ap=-1, type="Missile", traits=[]),
    ])


@pytest.fixture
def ammo_index():
    return {
        "LRM 20": [
            AmmoOption(name="Inferno", weapon_name="LRM 20", range='14"',
                       heat=6, dice=4, to_hit="5+", ap=0, type="Missile",
                       traits=["Fire"], points=10),
        ],
    }


def _atlas_record():
    return {
        "canonical_id": "atlas-as7-d",
        "chassis": "Atlas",
        "model": "AS7-D",
        "tonnage": 100.0,
        "walk_mp": 3,
        "armor_total": 304.0,
        "tech_base": "Inner Sphere",
        "unit_type": "mech",
        "raw_equipment_refs": [
            "Shoulder", "Hand Actuator",
            "AC/20", "Medium Laser", "Medium Laser",
            "LRM 20", "SRM 6",
            "IS Ammo AC/20", "IS Ammo LRM 20",
            "Endo Steel", "Ferro-Fibrous",
            "CASE",
        ],
        "source_path": "/some/path/atlas.mtf",
    }


def _locust_record():
    return {
        "canonical_id": "locust-lct-1v",
        "chassis": "Locust",
        "model": "LCT-1V",
        "tonnage": 20.0,
        "walk_mp": 8,
        "armor_total": 64.0,
        "tech_base": "Inner Sphere",
        "unit_type": "mech",
        "raw_equipment_refs": [
            "Medium Laser", "Machine Gun", "Machine Gun",
            "IS Ammo MG",
        ],
    }


def _is_vehicle_record():
    return {
        "canonical_id": "demolisher-mki",
        "chassis": "Demolisher",
        "model": "Mk. I",
        "tonnage": 80.0,
        "cruise_mp": 3,
        "armor_total": 200.0,
        "tech_base": "Inner Sphere",
        "unit_type": "vehicle",
        "raw_equipment_refs": ["AC/20", "AC/20"],
    }


def _clan_vehicle_record():
    return {
        "canonical_id": "clan-light-tank",
        "chassis": "Skadi",
        "model": "Prime",
        "tonnage": 25.0,
        "cruise_mp": 7,
        "armor_total": 60.0,
        "tech_base": "Clan",
        "unit_type": "vehicle",
        "raw_equipment_refs": ["Medium Laser"],
    }


def _aero_record():
    return {
        "canonical_id": "leviathan",
        "chassis": "Leviathan",
        "model": "Prime",
        "tonnage": 200.0,            # super heavy (>100)
        "safe_thrust": 4,
        "armor_total": 240.0,
        "tech_base": "Inner Sphere",
        "unit_type": "aerospace",
        "raw_equipment_refs": ["LRM 20"],
    }


def _mixed_record():
    r = _atlas_record()
    r["tech_base"] = "Mixed (IS Chassis)"
    return r


class TestAtlas:
    def test_core_stats(self, weapon_index, ammo_index):
        cov = Coverage(unit_type="mech")
        d = build_detachment(_atlas_record(), weapon_index, ammo_index, None, cov)
        assert d is not None
        assert d["name"] == "Atlas AS7-D"
        assert d["detachment"] == "BattleMech"
        assert d["unit_type"] == "BattleMech"
        assert d["tech_base"] == "Inner Sphere"
        assert d["tonnage"] == 100.0
        assert d["armor_save"] == "3+"   # 304 → 300-400 → 3+
        assert d["movement"] == "5\""    # walk 3 → 5"
        assert d["wounds"] == 8          # assault
        assert d["scale"] == 4
        assert d["tier"] == "assault"
        assert d["detachment_size"] == {"base": 1, "max": 1}
        assert d["points"] is None

    def test_weapons_one_per_install(self, weapon_index, ammo_index):
        d = build_detachment(_atlas_record(), weapon_index, ammo_index, None, Coverage("mech"))
        names = [w["name"] for w in d["weapons"]]
        # 1× AC/20, 2× Medium Laser, 1× LRM 20, 1× SRM 6
        assert names == ["AC/20", "Medium Laser", "Medium Laser", "LRM 20", "SRM 6"]
        ac20 = d["weapons"][0]
        assert ac20["unmapped"] is False
        assert ac20["dice"] == 4
        assert ac20["heat"] == 7

    def test_special_rules_drop_ferro_endo_ammo(self, weapon_index, ammo_index):
        d = build_detachment(_atlas_record(), weapon_index, ammo_index, None, Coverage("mech"))
        assert "CASE" in d["special_rules"]
        assert all("ferro" not in s.lower() for s in d["special_rules"])
        assert all("endo" not in s.lower() for s in d["special_rules"])
        assert all("ammo" not in s.lower() for s in d["special_rules"])

    def test_special_ammo_from_lrm20(self, weapon_index, ammo_index):
        d = build_detachment(_atlas_record(), weapon_index, ammo_index, None, Coverage("mech"))
        ammo = d["upgrade_options"]["special_ammo"]
        assert len(ammo) == 1
        assert ammo[0]["name"] == "Inferno"
        assert ammo[0]["weapon_name"] == "LRM 20"

    def test_mech_no_size_upgrades(self, weapon_index, ammo_index):
        d = build_detachment(_atlas_record(), weapon_index, ammo_index, None, Coverage("mech"))
        assert d["upgrade_options"]["detachment_size"] == []


class TestLocust:
    def test_core_stats(self, weapon_index, ammo_index):
        d = build_detachment(_locust_record(), weapon_index, ammo_index, None, Coverage("mech"))
        assert d["armor_save"] == "5+"  # 64 → 5+
        assert d["movement"] == "10\""  # walk 8 → 10"
        assert d["wounds"] == 2
        assert d["scale"] == 2
        assert d["tier"] == "light"

    def test_machine_gun_unmapped(self, weapon_index, ammo_index):
        cov = Coverage("mech")
        d = build_detachment(_locust_record(), weapon_index, ammo_index, None, cov)
        names = [w["name"] for w in d["weapons"]]
        assert names.count("Machine Gun") == 2
        unmapped = [w for w in d["weapons"] if w["unmapped"]]
        assert len(unmapped) == 2
        assert all(w["name"] == "Machine Gun" for w in unmapped)
        assert cov.unmapped_weapons.get("Machine Gun") == 2


class TestVehicle:
    def test_inner_sphere_demolisher(self, weapon_index, ammo_index):
        d = build_detachment(_is_vehicle_record(), weapon_index, ammo_index, None, Coverage("vehicle"))
        assert d["detachment"] == "Vehicle Lance"
        assert d["unit_type"] == "Vehicle"
        assert d["tier"] == "heavy"
        assert d["scale"] == 2
        assert d["wounds"] == 3
        assert d["movement"] == "5\""    # cruise 3 → 5"
        assert d["armor_save"] == "3+"   # 200 → 81-250 → 3+
        assert d["detachment_size"] == {"base": 4, "max": 12}
        # 4→12: 8 placeholder upgrade rows.
        ups = d["upgrade_options"]["detachment_size"]
        assert [u["size"] for u in ups] == [5, 6, 7, 8, 9, 10, 11, 12]
        assert all(u["points"] is None for u in ups)

    def test_clan_vehicle_size_and_label(self, weapon_index, ammo_index):
        d = build_detachment(_clan_vehicle_record(), weapon_index, ammo_index, None, Coverage("vehicle"))
        assert d["detachment"] == "Vehicle Star"
        assert d["detachment_size"] == {"base": 5, "max": 15}
        ups = d["upgrade_options"]["detachment_size"]
        assert [u["size"] for u in ups] == list(range(6, 16))


class TestAerospace:
    def test_inner_sphere_super_heavy(self, weapon_index, ammo_index):
        d = build_detachment(_aero_record(), weapon_index, ammo_index, None, Coverage("aerospace"))
        assert d["detachment"] == "Aerospace Lance"
        assert d["movement"] == "20\""   # safe thrust 4 → 20"
        assert d["scale"] == 2
        assert d["wounds"] == 4          # 200t → super heavy → 4
        assert d["tier"] == "superheavy"
        assert d["detachment_size"] == {"base": 1, "max": 1}


class TestSkipBehavior:
    def test_mixed_tech_base_skipped(self, weapon_index, ammo_index):
        cov = Coverage("mech")
        d = build_detachment(_mixed_record(), weapon_index, ammo_index, None, cov)
        assert d is None
        assert cov.skipped_unknown_tech_base == 1

    def test_missing_armor_skipped(self, weapon_index, ammo_index):
        rec = _atlas_record()
        rec["armor_total"] = None
        cov = Coverage("mech")
        d = build_detachment(rec, weapon_index, ammo_index, None, cov)
        assert d is None
        assert cov.skipped_missing_armor == 1

    def test_missing_movement_skipped(self, weapon_index, ammo_index):
        rec = _atlas_record()
        rec["walk_mp"] = None
        cov = Coverage("mech")
        d = build_detachment(rec, weapon_index, ammo_index, None, cov)
        assert d is None
        assert cov.skipped_missing_movement == 1

    def test_speed_gap_recorded(self, weapon_index, ammo_index):
        rec = _atlas_record()
        rec["walk_mp"] = 13   # mech table skips 13
        cov = Coverage("mech")
        d = build_detachment(rec, weapon_index, ammo_index, None, cov)
        assert d is not None
        assert d["movement"] == "14\""    # falls back to row 12
        assert len(cov.missing_speed) == 1


class TestBuildAll:
    def test_aggregates_and_filters(self, weapon_index, ammo_index):
        records = [_atlas_record(), _locust_record(), _mixed_record()]
        out, cov = build_all(records, "mech", weapon_index, ammo_index)
        assert len(out) == 2
        assert cov.total_records == 3
        assert cov.emitted == 2
        assert cov.skipped_unknown_tech_base == 1
