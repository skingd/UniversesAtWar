"""Tests for src.detachments.equipment."""
from __future__ import annotations

import pytest

from src.detachments.equipment import (
    partition_refs,
    special_rules_from_equipment,
)
from src.detachments.weapons import (
    WeaponProfile,
    build_weapon_index,
)


@pytest.fixture
def weapon_index():
    profs = [
        WeaponProfile(name="PPC", range='12"', heat=10, dice=3,
                      to_hit="3+", ap=-2, type="Energy", traits=["Heavy"]),
        WeaponProfile(name="Inner Sphere Medium Laser", range='6"', heat=3,
                      dice=2, to_hit="4+", ap=-1, type="Energy", traits=[]),
    ]
    return build_weapon_index(profs)


class TestPartitionRefs:
    def test_resolved_weapon_to_weapons(self, weapon_index):
        wpns, eqp = partition_refs(["PPC", "PPC"], weapon_index)
        assert wpns == ["PPC", "PPC"]
        assert eqp == []

    def test_ammo_dropped(self, weapon_index):
        wpns, eqp = partition_refs(["IS Ammo PPC", "Ammo LRM 10"], weapon_index)
        assert wpns == []
        assert eqp == []

    def test_unmapped_weapon_routed_to_weapons(self, weapon_index):
        # "AC/20" looks like a weapon (has "ac/" hint) but isn't in our
        # tiny index — partition should still surface it as a weapon ref so
        # the assembler can emit it with `unmapped: true`.
        wpns, eqp = partition_refs(["AC/20"], weapon_index)
        assert wpns == ["AC/20"]
        assert eqp == []

    def test_real_equipment_routed_to_equipment(self, weapon_index):
        wpns, eqp = partition_refs(["CASE", "Double Heat Sink"], weapon_index)
        assert wpns == []
        assert "CASE" in eqp
        assert "Double Heat Sink" in eqp

    def test_structural_dropped(self, weapon_index):
        wpns, eqp = partition_refs(
            ["Heat Sink", "Hand Actuator", "Cockpit"], weapon_index,
        )
        assert wpns == []
        assert eqp == []

    def test_blank_skipped(self, weapon_index):
        wpns, eqp = partition_refs(["", "   ", None], weapon_index)
        assert wpns == [] and eqp == []


class TestSpecialRulesFromEquipment:
    def test_dedup_preserves_order(self):
        rules = special_rules_from_equipment(["CASE", "TAG", "CASE", "Beagle Active Probe"])
        assert rules == ["CASE", "TAG", "Beagle Active Probe"]

    def test_drops_ferro_and_endo(self):
        rules = special_rules_from_equipment([
            "Ferro-Fibrous", "Endo Steel", "CASE", "Endo-Composite",
        ])
        assert rules == ["CASE"]

    def test_drops_ammo_residual(self):
        rules = special_rules_from_equipment(["IS Ammo LRM 10", "TAG"])
        assert rules == ["TAG"]

    def test_strips_tech_prefix(self):
        # parse_reference strips "Inner Sphere " — special_rules should
        # surface the bare name.
        rules = special_rules_from_equipment(["Inner Sphere CASE"])
        assert rules == ["CASE"]
