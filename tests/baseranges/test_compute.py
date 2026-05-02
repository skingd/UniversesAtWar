"""Tests for src.baseranges.compute."""
from __future__ import annotations

from src.baseranges.compute import (
    UNIT_TYPE_CONFIG,
    compute_all,
    compute_unit_type,
    required_field_counts,
)


def _mech(walk, jump, armor, tonnage):
    return {
        "unit_type": "mech",
        "walk_mp": walk,
        "jump_mp": jump,
        "armor_total": armor,
        "tonnage": tonnage,
    }


class TestComputeMech:
    def test_overall_min_max_median(self):
        records = [
            _mech(8, 8, 64, 20),    # light
            _mech(6, 0, 96, 35),    # light
            _mech(4, 4, 192, 50),   # medium
            _mech(3, 0, 304, 75),   # heavy
            _mech(3, 0, 307, 100),  # assault
        ]
        out = compute_unit_type(records, "mech")
        ov = out["overall"]
        assert ov["n"] == 5
        assert ov["movement"]["min"] == 3.0
        assert ov["movement"]["max"] == 8.0
        assert ov["movement"]["median"] == 4.0
        assert ov["armor"]["min"] == 64.0
        assert ov["armor"]["max"] == 307.0
        assert ov["armor"]["median"] == 192.0

    def test_per_tier_split(self):
        records = [
            _mech(8, 8, 64, 20),
            _mech(6, 0, 96, 35),
            _mech(4, 4, 192, 50),
            _mech(3, 0, 304, 75),
            _mech(3, 0, 307, 100),
        ]
        out = compute_unit_type(records, "mech")
        tiers = out["by_tier"]
        assert set(tiers) == {"light", "medium", "heavy", "assault"}
        assert tiers["light"]["n"] == 2
        assert tiers["light"]["movement"]["min"] == 6.0
        assert tiers["light"]["movement"]["max"] == 8.0
        assert tiers["assault"]["armor"]["max"] == 307.0

    def test_skips_missing_fields(self):
        records = [
            _mech(4, None, None, 50),
            _mech(None, None, 100, 50),
        ]
        out = compute_unit_type(records, "mech")
        assert out["overall"]["movement"]["count"] == 1
        assert out["overall"]["armor"]["count"] == 1


class TestComputeOtherTypes:
    def test_vehicle(self):
        recs = [
            {"cruise_mp": 5, "armor_total": 30, "tonnage": 25},
            {"cruise_mp": 3, "armor_total": 80, "tonnage": 80},
        ]
        out = compute_unit_type(recs, "vehicle")
        assert out["overall"]["movement"]["min"] == 3.0
        assert out["overall"]["movement"]["max"] == 5.0
        assert "light" in out["by_tier"]
        assert "heavy" in out["by_tier"]

    def test_aerospace(self):
        recs = [
            {"safe_thrust": 6, "armor_total": 40, "tonnage": 30},
            {"safe_thrust": 4, "armor_total": 80, "tonnage": 95},
        ]
        out = compute_unit_type(recs, "aerospace")
        assert out["overall"]["movement"]["min"] == 4.0
        assert out["overall"]["movement"]["max"] == 6.0

    def test_infantry_buckets_by_motion_mode(self):
        recs = [
            {"movement_points": 1, "movement_mode": "Foot"},
            {"movement_points": 2, "movement_mode": "Foot"},
            {"movement_points": 4, "movement_mode": "Tracked"},
        ]
        out = compute_unit_type(recs, "infantry")
        assert out["tier_label"] == "motion_mode"
        assert "armor" not in out["overall"]
        assert out["by_tier"]["Foot"]["n"] == 2
        assert out["by_tier"]["Tracked"]["movement"]["max"] == 4.0


class TestComputeAll:
    def test_runs_only_provided_types(self):
        out = compute_all({
            "mech": [_mech(4, 0, 100, 50)],
            "vehicle": [{"cruise_mp": 5, "armor_total": 30, "tonnage": 25}],
        })
        assert set(out) == {"mech", "vehicle"}

    def test_unknown_type_rejected(self):
        import pytest
        with pytest.raises(ValueError):
            compute_unit_type([], "spaceship")


class TestStrictCounts:
    def test_required_field_counts(self):
        recs = [
            {"walk_mp": 4, "armor_total": None},
            {"walk_mp": None, "armor_total": 50},
        ]
        c = required_field_counts(recs, "mech")
        assert c == {"walk_mp": 1, "armor_total": 1}

    def test_unit_type_config_supports_all_types(self):
        assert set(UNIT_TYPE_CONFIG) == {"mech", "vehicle", "aerospace", "infantry"}
