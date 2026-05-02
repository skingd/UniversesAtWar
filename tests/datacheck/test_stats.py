"""Tests for src.datacheck.stats — base-stat extractors."""
from __future__ import annotations

from src.datacheck.stats import (
    extract_armor_total,
    extract_cruise_mp,
    extract_engine_rating,
    extract_heat_sink_count,
    extract_infantry_movement,
    extract_jump_mp,
    extract_run_mp,
    extract_safe_thrust,
    extract_walk_mp,
    to_float,
    to_int,
)


class TestNumericCoercion:
    def test_to_float_passthrough(self):
        assert to_float(3.5) == 3.5
        assert to_float(7) == 7.0

    def test_to_float_strings(self):
        assert to_float("12") == 12.0
        assert to_float("12.5 tons") == 12.5

    def test_to_float_na(self):
        assert to_float("NA") is None
        assert to_float(None) is None
        assert to_float(True) is None

    def test_to_int(self):
        assert to_int("3.7") == 3
        assert to_int(None) is None


class TestArmorTotal:
    def test_dict(self):
        ap = {"LA": 10, "RA": 10, "CT": 25, "Internal": "NA"}
        assert extract_armor_total({"Armor": ap}) == 45.0

    def test_armor_points_alias(self):
        assert extract_armor_total({"Armor Points": {"Front": 30, "Rear": 5}}) == 35.0

    def test_list_of_dicts(self):
        ap = [{"Front": 10}, {"Rear": 5}, {"Side": 7}]
        assert extract_armor_total({"Armor": ap}) == 22.0

    def test_list_of_numbers(self):
        assert extract_armor_total({"Armor": [10, 5, "NA", 7]}) == 22.0

    def test_scalar(self):
        assert extract_armor_total({"Armor": 88}) == 88.0

    def test_missing(self):
        assert extract_armor_total({}) is None

    def test_all_non_numeric(self):
        assert extract_armor_total({"Armor": {"x": "NA", "y": "-"}}) is None


class TestMechMovement:
    def test_walk_mp(self):
        assert extract_walk_mp({"Walk MP": 4}) == 4
        assert extract_walk_mp({"walk_mp": "3"}) == 3
        assert extract_walk_mp({}) is None

    def test_jump_mp_explicit_zero(self):
        # Atlas-style: jump_mp explicitly 0 must NOT collapse to None.
        assert extract_jump_mp({"Jump MP": 0}) == 0

    def test_jump_mp_present(self):
        assert extract_jump_mp({"Jump MP": 5}) == 5

    def test_jump_mp_missing(self):
        assert extract_jump_mp({}) is None

    def test_run_mp_derived(self):
        assert extract_run_mp({"Walk MP": 4}) == 6
        assert extract_run_mp({"Walk MP": 8}) == 12

    def test_run_mp_explicit(self):
        assert extract_run_mp({"Walk MP": 4, "Run MP": 7}) == 7

    def test_run_mp_missing(self):
        assert extract_run_mp({}) is None


class TestVehicleAerospaceMovement:
    def test_cruise_mp(self):
        assert extract_cruise_mp({"Cruise MP": 5}) == 5

    def test_cruise_missing(self):
        assert extract_cruise_mp({}) is None

    def test_safe_thrust(self):
        assert extract_safe_thrust({"Safe Thrust": 6}) == 6
        assert extract_safe_thrust({}) is None


class TestInfantry:
    def test_movement_with_mode(self):
        mp, mode = extract_infantry_movement({"Movement Points": 3, "Motion Type": "Foot"})
        assert mp == 3
        assert mode == "Foot"

    def test_walk_mp_fallback(self):
        mp, _ = extract_infantry_movement({"Walk MP": 2})
        assert mp == 2

    def test_motion_type_lookup(self):
        # No explicit MP field — derived from Motion Type per Total Warfare.
        assert extract_infantry_movement({"Motion Type": "Foot"}) == (1, "Foot")
        assert extract_infantry_movement({"Motion Type": "Wheeled"}) == (3, "Wheeled")
        assert extract_infantry_movement({"Motion Type": "Hover"}) == (5, "Hover")
        assert extract_infantry_movement({"Motion Type": "VTOL"}) == (6, "VTOL")

    def test_unknown_motion_type(self):
        mp, mode = extract_infantry_movement({"Motion Type": "Teleport"})
        assert mp is None
        assert mode == "Teleport"

    def test_missing(self):
        mp, mode = extract_infantry_movement({})
        assert mp is None
        assert mode is None


class TestEngineHeatSinks:
    def test_engine_dict(self):
        assert extract_engine_rating({"Engine": {"rating": 300}}) == 300.0

    def test_engine_scalar(self):
        assert extract_engine_rating({"Engine": "200"}) == 200.0

    def test_heat_sinks_dict(self):
        assert extract_heat_sink_count({"Heat Sinks": {"count": 12}}) == 12

    def test_heat_sinks_int(self):
        assert extract_heat_sink_count({"Heat Sinks": 10}) == 10


class TestExtractBaseStatsIntegration:
    """`_extract_base_stats` is the per-unit-type dispatcher used inside
    build_unit_index. Verify it returns the right field set for each type."""

    def test_dispatch(self):
        from src.datacheck.index_builder import _extract_base_stats

        mech_blob = {"Walk MP": 4, "Jump MP": 0, "Armor": {"CT": 30, "LT": 20}}
        out = _extract_base_stats(mech_blob, "mech")
        assert out == {"walk_mp": 4, "jump_mp": 0, "armor_total": 50.0}

        veh_blob = {"Cruise MP": 5, "Armor": [10, 10, 5, 5]}
        out = _extract_base_stats(veh_blob, "vehicle")
        assert out == {"cruise_mp": 5, "armor_total": 30.0}

        aero_blob = {"Safe Thrust": 6, "Armor": 40}
        out = _extract_base_stats(aero_blob, "aerospace")
        assert out == {"safe_thrust": 6, "armor_total": 40.0}

        inf_blob = {"Movement Points": 2, "Motion Type": "Tracked"}
        out = _extract_base_stats(inf_blob, "infantry")
        assert out == {"movement_points": 2, "movement_mode": "Tracked"}

    def test_dispatch_missing_fields(self):
        from src.datacheck.index_builder import _extract_base_stats

        out = _extract_base_stats({}, "mech")
        assert out == {"walk_mp": None, "jump_mp": None, "armor_total": None}

    def test_dispatch_unknown_type(self):
        from src.datacheck.index_builder import _extract_base_stats

        assert _extract_base_stats({}, "spaceship") == {}
