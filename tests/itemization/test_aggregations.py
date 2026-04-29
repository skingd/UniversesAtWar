"""Tests for itemization.aggregations and bands."""
from __future__ import annotations

from src.itemization.aggregations import (
    aerospace_tier,
    aggregate_units,
    aggregate_weapons,
    era_bucket,
    mech_tier,
    vehicle_tier,
)
from src.itemization.bands import (
    derive_translation_bands,
    derive_weapon_range_bands,
)


class TestTierClassification:
    def test_mech_tiers(self):
        assert mech_tier(20) == "light"
        assert mech_tier(35) == "light"
        assert mech_tier(40) == "medium"
        assert mech_tier(60) == "heavy"
        assert mech_tier(100) == "assault"
        assert mech_tier(150) == "superheavy"
        assert mech_tier(None) == "unknown"

    def test_vehicle_tiers(self):
        assert vehicle_tier(20) == "light"
        assert vehicle_tier(80) == "heavy"

    def test_aerospace_tiers(self):
        assert aerospace_tier(35) == "light"
        assert aerospace_tier(70) == "medium"


class TestEraBucket:
    def test_known_eras(self):
        assert era_bucket(2750) == "star-league"
        assert era_bucket(3025) == "succession-wars"
        assert era_bucket(3055) == "clan-invasion"
        assert era_bucket(3151) == "ilclan"

    def test_unknown(self):
        assert era_bucket(None) == "unknown"
        assert era_bucket("not-a-year") == "unknown"


class TestAggregateUnits:
    def test_minimal(self):
        units = {
            "mech": [
                {"tonnage": 20, "era": 3025, "tech_base": "Inner Sphere",
                 "raw_equipment_refs": ["Medium Laser"], "raw_quirks": [],
                 "source_path": "x"},
                {"tonnage": 100, "era": 3025, "tech_base": "Inner Sphere",
                 "raw_equipment_refs": ["AC/20"] * 4, "raw_quirks": ["Battle Fists"],
                 "source_path": "y"},
            ],
            "vehicle": [],
            "aerospace": [],
            "infantry": [],
        }
        out = aggregate_units(units)
        assert out["mech"]["count"] == 2
        assert out["mech"]["tonnage"]["min"] == 20
        assert out["mech"]["tonnage"]["max"] == 100
        assert out["mech"]["tier"]["light"] == 1
        assert out["mech"]["tier"]["assault"] == 1
        assert out["mech"]["tech_base"]["Inner Sphere"] == 2


class TestAggregateWeapons:
    def test_basic(self):
        weapons = [
            {"display_name": "Medium Laser", "category": "energy", "subcategory": "laser",
             "tech_base": "Inner Sphere", "damage": 5, "heat": 3, "tonnage": 1,
             "long_range": 9, "short_range": 3, "medium_range": 6, "crit_slots": 1},
            {"display_name": "AC/20", "category": "ballistic", "subcategory": "autocannon",
             "tech_base": "Inner Sphere", "damage": 20, "heat": 7, "tonnage": 14,
             "long_range": 9, "short_range": 3, "medium_range": 6, "crit_slots": 10},
            {"display_name": "ER PPC", "category": "energy", "subcategory": "ppc",
             "tech_base": "Inner Sphere", "damage": 10, "heat": 15, "tonnage": 7,
             "long_range": 23, "short_range": 7, "medium_range": 14, "crit_slots": 3},
        ]
        out = aggregate_weapons(weapons)
        assert out["count"] == 3
        assert out["overall"]["damage"]["count"] == 3
        assert out["overall"]["damage"]["max"] == 20
        assert out["by_category"]["energy"]["count"] == 2
        assert out["by_subcategory"]["ppc"]["count"] == 1
        # derived
        assert out["derived"]["damage_per_heat"]["count"] == 3


class TestBandDerivation:
    def test_weapon_range_bands(self):
        weapons = [
            {"display_name": "Medium Laser", "long_range": 9},
            {"display_name": "Small Laser",  "long_range": 3},
            {"display_name": "AC/20",        "long_range": 9},
            {"display_name": "AC/2",         "long_range": 24},
            {"display_name": "ER PPC",       "long_range": 23},
            {"display_name": "Gauss Rifle",  "long_range": 22},
            {"display_name": "LRM 20",       "long_range": 21},
            {"display_name": "SRM 6",        "long_range": 9},
            {"display_name": "Machine Gun",  "long_range": 1},
            {"display_name": "Flamer",       "long_range": 1},
            {"display_name": "Large Laser",  "long_range": 15},
            {"display_name": "ER Large Laser", "long_range": 19},
            {"display_name": "ER Medium Laser", "long_range": 14},
            {"display_name": "ER Small Laser",  "long_range": 5},
            {"display_name": "AC/5",         "long_range": 18},
            {"display_name": "AC/10",        "long_range": 15},
            {"display_name": "PPC",          "long_range": 18},
            {"display_name": "LRM 5",        "long_range": 21},
            {"display_name": "LRM 10",       "long_range": 21},
            {"display_name": "LRM 15",       "long_range": 21},
            {"display_name": "SRM 2",        "long_range": 9},
            {"display_name": "SRM 4",        "long_range": 9},
        ]
        out = derive_weapon_range_bands(weapons)
        assert out["validation_total"] > 0
        # We should classify a healthy fraction correctly even on this small set.
        assert out["validation_hits"] >= int(0.5 * out["validation_total"])
        assert "POINT-BLANK" in out["labels"]

    def test_full_pipeline_smoke(self):
        weapons = [{"display_name": "Medium Laser", "long_range": 9, "damage": 5,
                    "heat": 3, "tonnage": 1, "category": "energy",
                    "subcategory": "laser", "tech_base": "Inner Sphere",
                    "short_range": 3, "medium_range": 6, "crit_slots": 1}]
        unit_agg = aggregate_units({
            "mech": [{"tonnage": 50, "era": 3025, "tech_base": "Inner Sphere",
                     "raw_equipment_refs": [], "raw_quirks": [], "source_path": "x"}],
            "vehicle": [], "aerospace": [], "infantry": [],
        })
        weapon_agg = aggregate_weapons(weapons)
        bands = derive_translation_bands(weapons, unit_agg, weapon_agg)
        # Should produce keys for every stat without crashing.
        assert set(bands.keys()) == {"weapon_range", "movement", "armour_save",
                                      "damage_ap", "wounds"}
