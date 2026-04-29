"""Tests for itemization.catalogues — Part 1 classification + coverage."""
from __future__ import annotations

from src.itemization.catalogues import (
    build_catalogues,
    classify_equipment_type,
    classify_upgrade,
    classify_weapon_subcategory,
)


class TestWeaponSubcategory:
    def test_autocannon(self):
        assert classify_weapon_subcategory("AC/20") == "autocannon"
        assert classify_weapon_subcategory("LB 10-X AC") == "autocannon"

    def test_gauss(self):
        assert classify_weapon_subcategory("Gauss Rifle") == "gauss"
        assert classify_weapon_subcategory("Heavy Gauss Rifle") == "gauss"
        assert classify_weapon_subcategory("Magshot") == "gauss"

    def test_lasers(self):
        assert classify_weapon_subcategory("Medium Laser") == "laser"
        assert classify_weapon_subcategory("Medium Pulse Laser") == "pulse-laser"
        assert classify_weapon_subcategory("ER Large Laser") == "er-laser"

    def test_ppc(self):
        assert classify_weapon_subcategory("PPC") == "ppc"
        assert classify_weapon_subcategory("ER PPC") == "ppc"

    def test_missiles(self):
        assert classify_weapon_subcategory("LRM 20") == "lrm"
        assert classify_weapon_subcategory("SRM 6") == "srm"
        assert classify_weapon_subcategory("Streak SRM 4") == "streak"

    def test_unknown(self):
        assert classify_weapon_subcategory("") == "unknown"
        assert classify_weapon_subcategory(None) == "unknown"
        assert classify_weapon_subcategory("Whatsit Cannon") == "other"


class TestUpgradeClassification:
    def test_masc(self):
        out = classify_upgrade("MASC")
        assert out == ("masc", "move", "binary")

    def test_xl_engine(self):
        out = classify_upgrade("XL Engine")
        assert out is not None
        assert out[0] == "engine-xl"
        assert out[1] == "wounds"

    def test_endo_steel(self):
        assert classify_upgrade("Endo Steel")[0] == "structure-endo-steel"

    def test_stealth_armor(self):
        assert classify_upgrade("Stealth Armor")[0] == "armor-stealth"

    def test_double_heat_sink(self):
        out = classify_upgrade("Double Heat Sink")
        assert out == ("heat-sink-double", "heat", "scaled")

    def test_artemis(self):
        assert classify_upgrade("Artemis IV FCS")[0] == "artemis"

    def test_non_upgrade(self):
        assert classify_upgrade("Medium Laser") is None
        assert classify_upgrade("") is None


class TestEquipmentType:
    def test_explicit_type(self):
        assert classify_equipment_type({"equipment_type": "electronics"}) == "electronics"

    def test_inferred_heat(self):
        assert classify_equipment_type({"display_name": "Double Heat Sink"}) == "heat"

    def test_inferred_mobility(self):
        assert classify_equipment_type({"display_name": "Jump Jet"}) == "mobility"

    def test_fallback(self):
        assert classify_equipment_type({"display_name": "Mystery Box"}) == "other"


class TestBuildCatalogues:
    def _records(self):
        return [
            {
                "canonical_id": "is-medium-laser",
                "display_name": "Medium Laser",
                "category": "energy",
                "tech_base": "Inner Sphere",
                "weight_tons": "1",
                "damage": "5",
                "heat": "3",
                "range": {"minimum": "0", "short": "3", "medium": "6", "long": "9"},
                "space": {"battlemech": "1"},
            },
            {
                "canonical_id": "is-ammo-ac-20",
                "display_name": "Inner Sphere Ammo AC/20",
                "category": "ammunition",
                "tech_base": "Inner Sphere",
                "weight_tons": "1",
                "weapon_ref": "AC/20",
                "ammo_per_ton": "5",
            },
            {
                "canonical_id": "is-masc",
                "display_name": "MASC",
                "category": "equipment",
                "tech_base": "Inner Sphere",
                "weight_tons": "3",
                "equipment_type": "enhancement",
                "space": {"battlemech": "3"},
            },
            {
                "canonical_id": "is-double-heat-sink",
                "display_name": "Double Heat Sink",
                "category": "equipment",
                "tech_base": "Inner Sphere",
                "weight_tons": "1",
                "space": {"battlemech": "3"},
            },
        ]

    def test_classification(self):
        result = build_catalogues(self._records(), {"mech": []})
        assert len(result["weapons"]) == 1
        assert result["weapons"][0]["subcategory"] == "laser"
        assert len(result["ammunition"]) == 1
        assert result["ammunition"][0]["weapon_ref"] == "AC/20"
        assert len(result["equipment"]) == 2
        # MASC and Double Heat Sink are both upgrades
        labels = {u["upgrade_label"] for u in result["upgrades"]}
        assert "masc" in labels
        assert "heat-sink-double" in labels

    def test_coverage_no_alias(self):
        result = build_catalogues(self._records(), {"mech": []})
        cov = result["coverage"]
        # without alias_index, coverage skips uncatalogued + orphan checks
        assert cov["uncatalogued_count"] == 0
        assert cov["orphan_count"] == 0
        assert cov["blocking"] is False

    def test_weapon_range_extraction(self):
        result = build_catalogues(self._records(), {"mech": []})
        w = result["weapons"][0]
        assert w["short_range"] == 3.0
        assert w["medium_range"] == 6.0
        assert w["long_range"] == 9.0
        assert w["damage"] == "5"  # raw passthrough
        assert w["heat"] == 3.0
