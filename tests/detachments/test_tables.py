"""Tests for src.detachments.tables."""
from __future__ import annotations

import pytest

from src.detachments.tables import (
    armor_save,
    base_speed_field,
    detachment_label,
    detachment_size,
    movement_inches,
    scale,
    tier,
    unit_type_label,
    wounds,
)


class TestArmorSave:
    @pytest.mark.parametrize("armor,expected", [
        (0,   "5+"), (20,  "5+"),
        (21,  "4+"), (80,  "4+"),
        (81,  "3+"), (250, "3+"),
        (251, "2+"), (300, "2+"),
        (301, "1+"), (704, "1+"),
    ])
    def test_mech(self, armor, expected):
        assert armor_save(armor, "mech") == expected

    def test_mech_and_aerospace_share_table(self):
        for armor, expected in [(20, "5+"), (80, "4+"), (200, "3+"), (300, "2+"), (400, "1+")]:
            assert armor_save(armor, "mech") == armor_save(armor, "aerospace")

    @pytest.mark.parametrize("armor,expected", [
        (0,   "5+"), (50,  "5+"), (99,  "5+"),
        (100, "4+"), (200, "4+"), (299, "4+"),
        (300, "3+"), (350, "3+"), (400, "3+"),
        (401, "2+"), (576, "2+"),
    ])
    def test_vehicle(self, armor, expected):
        assert armor_save(armor, "vehicle") == expected

    @pytest.mark.parametrize("armor,expected", [
        (0,   "5+"), (20,  "5+"),
        (21,  "4+"), (80,  "4+"),
        (81,  "3+"), (250, "3+"),
        (251, "2+"), (300, "2+"),
        (301, "1+"), (704, "1+"),
    ])
    def test_aerospace(self, armor, expected):
        assert armor_save(armor, "aerospace") == expected

    def test_missing(self):
        assert armor_save(None, "mech") is None
        assert armor_save("NA", "vehicle") is None


class TestMovement:
    def test_mech_exact(self):
        assert movement_inches(8, "mech") == ("10\"", True)
        assert movement_inches(3, "mech") == ("5\"", True)
        assert movement_inches(16, "mech") == ("17\"", True)

    def test_aerospace_exact(self):
        assert movement_inches(6, "aerospace") == ("22\"", True)

    def test_vehicle_exact(self):
        assert movement_inches(3, "vehicle") == ("5\"", True)
        assert movement_inches(18, "vehicle") == ("19\"", True)

    def test_mech_speed_13_falls_to_12(self):
        # design table skips 13 → caller gets the row for 12 + exact=False.
        mv, exact = movement_inches(13, "mech")
        assert mv == "14\""
        assert exact is False

    def test_aerospace_speed_13_falls_to_12(self):
        mv, exact = movement_inches(13, "aerospace")
        assert mv == "28\""
        assert exact is False

    def test_above_max_clamps(self):
        mv, exact = movement_inches(99, "mech")
        assert mv == "17\""
        assert exact is False

    def test_below_min(self):
        # mech table starts at 2 — speed 1 has no row.
        assert movement_inches(1, "mech") == (None, False)

    def test_missing(self):
        assert movement_inches(None, "mech") == (None, False)


class TestTier:
    def test_mech(self):
        assert tier(20, "mech") == "light"
        assert tier(35, "mech") == "light"
        assert tier(50, "mech") == "medium"
        assert tier(75, "mech") == "heavy"
        assert tier(100, "mech") == "assault"
        assert tier(200, "mech") == "superheavy"

    def test_vehicle(self):
        assert tier(25, "vehicle") == "light"
        assert tier(50, "vehicle") == "medium"
        assert tier(80, "vehicle") == "heavy"
        assert tier(150, "vehicle") == "assault"

    def test_aerospace(self):
        assert tier(30, "aerospace") == "light"
        assert tier(70, "aerospace") == "medium"
        assert tier(95, "aerospace") == "heavy"
        assert tier(200, "aerospace") == "superheavy"


class TestWoundsAndScale:
    def test_mech_wounds(self):
        assert wounds(20, "mech") == 2
        assert wounds(50, "mech") == 4
        assert wounds(75, "mech") == 6
        assert wounds(100, "mech") == 8

    def test_vehicle_wounds(self):
        assert wounds(25, "vehicle") == 1
        assert wounds(80, "vehicle") == 3
        assert wounds(150, "vehicle") == 4

    def test_aerospace_wounds(self):
        assert wounds(30, "aerospace") == 1
        assert wounds(95, "aerospace") == 3

    def test_mech_scale(self):
        assert scale(20, "mech") == 2
        assert scale(50, "mech") == 3
        assert scale(75, "mech") == 3
        assert scale(100, "mech") == 4

    def test_vehicle_scale(self):
        assert scale(25, "vehicle") == 1
        assert scale(50, "vehicle") == 2
        assert scale(150, "vehicle") == 3

    def test_aerospace_scale_constant(self):
        assert scale(30, "aerospace") == 2
        assert scale(95, "aerospace") == 2


class TestDetachmentSize:
    def test_mech_always_singleton(self):
        assert detachment_size(20, "mech", "Inner Sphere") == (1, 1)
        assert detachment_size(100, "mech", "Clan") == (1, 1)

    def test_vehicle_inner_sphere(self):
        assert detachment_size(25, "vehicle", "Inner Sphere") == (4, 12)
        assert detachment_size(150, "vehicle", "Inner Sphere") == (1, 4)

    def test_vehicle_clan(self):
        assert detachment_size(25, "vehicle", "Clan") == (5, 15)
        assert detachment_size(150, "vehicle", "Clan") == (1, 5)

    def test_aerospace_inner_sphere(self):
        assert detachment_size(30, "aerospace", "Inner Sphere") == (1, 4)
        assert detachment_size(150, "aerospace", "Inner Sphere") == (1, 1)

    def test_aerospace_clan(self):
        assert detachment_size(30, "aerospace", "Clan") == (1, 5)
        assert detachment_size(150, "aerospace", "Clan") == (1, 1)


class TestLabels:
    def test_detachment_label(self):
        assert detachment_label("mech", "Inner Sphere") == "BattleMech"
        assert detachment_label("mech", "Clan") == "BattleMech"
        assert detachment_label("vehicle", "Inner Sphere") == "Vehicle Lance"
        assert detachment_label("vehicle", "Clan") == "Vehicle Star"
        assert detachment_label("aerospace", "Inner Sphere") == "Aerospace Lance"
        assert detachment_label("aerospace", "Clan") == "Aerospace Star"

    def test_unit_type_label(self):
        assert unit_type_label("mech") == "BattleMech"
        assert unit_type_label("vehicle") == "Vehicle"
        assert unit_type_label("aerospace") == "Aerospace"

    def test_base_speed_field(self):
        assert base_speed_field("mech") == "walk_mp"
        assert base_speed_field("vehicle") == "cruise_mp"
        assert base_speed_field("aerospace") == "safe_thrust"
        assert base_speed_field("infantry") is None
