"""Tests for the equipment alias resolver."""
from __future__ import annotations

import pytest

from src.datacheck.alias_resolver import (
    AliasIndex,
    build_alias_index,
    is_structural,
    parse_reference,
)


# --- parse_reference -------------------------------------------------------

class TestParseReference:
    def test_mech_slot_with_tech_suffix(self):
        p = parse_reference("AC/20; Inner Sphere")
        assert p.name == "AC/20"
        assert p.tech_base == "Inner Sphere"
        assert not p.is_rear
        assert not p.is_omnipod

    def test_clan_omnipod_suffix(self):
        p = parse_reference("ER Large Laser; Clan (OmniPod)")
        assert p.name == "ER Large Laser"
        assert p.tech_base == "Clan"
        assert p.is_omnipod
        assert not p.is_rear

    def test_rear_facing_modifier(self):
        p = parse_reference("Medium Laser; Inner Sphere (R)")
        assert p.name == "Medium Laser"
        assert p.is_rear
        assert p.tech_base == "Inner Sphere"

    def test_vehicle_bare_name(self):
        p = parse_reference("PPC")
        assert p.name == "PPC"
        assert p.tech_base is None

    def test_vehicle_ammo_with_hyphen(self):
        p = parse_reference("IS Ammo LRM-10")
        assert "LRM" in p.name and "10" in p.name
        assert p.tech_base == "Inner Sphere"
        assert p.is_ammo

    def test_camelcase_split(self):
        p = parse_reference("ISMediumLaser")
        # "IS" prefix should be consumed as tech base
        assert p.tech_base == "Inner Sphere"
        assert "Medium" in p.name and "Laser" in p.name

    def test_clan_camelcase(self):
        p = parse_reference("CLActiveProbe")
        assert p.tech_base == "Clan"
        assert "Active" in p.name and "Probe" in p.name

    def test_normalized_key_collapses_hyphens(self):
        a = parse_reference("LRM-10")
        b = parse_reference("LRM 10")
        assert a.normalized_key == b.normalized_key

    def test_empty_slot(self):
        p = parse_reference("Empty")
        assert is_structural(p)

    def test_actuator(self):
        assert is_structural(parse_reference("Hand Actuator"))
        assert is_structural(parse_reference("Upper Arm Actuator"))
        assert is_structural(parse_reference("Hip"))

    def test_engine_is_structural(self):
        assert is_structural(parse_reference("Fusion Engine; Inner Sphere"))


# --- build_alias_index + lookup -------------------------------------------

@pytest.fixture
def sample_index() -> AliasIndex:
    equipment = [
        {
            "canonical_id": "is-medium-laser",
            "numeric_id": "110002",
            "display_name": "Inner Sphere Medium Laser",
            "mtf_reference": "Medium Laser",
            "category": "energy",
            "tech_base": "Inner Sphere",
        },
        {
            "canonical_id": "is-ac-20",
            "numeric_id": "120004",
            "display_name": "Inner Sphere AC/20",
            "mtf_reference": "Autocannon/20",
            "category": "ballistic",
            "tech_base": "Inner Sphere",
        },
        {
            "canonical_id": "clan-er-large-laser",
            "numeric_id": "210006",
            "display_name": "Clan ER Large Laser",
            "mtf_reference": "ER Large Laser",
            "category": "energy",
            "tech_base": "Clan",
        },
        {
            "canonical_id": "is-lrm-10",
            "numeric_id": "130002",
            "display_name": "Inner Sphere LRM 10",
            "mtf_reference": "LRM 10",
            "category": "missile",
            "tech_base": "Inner Sphere",
        },
    ]
    equipment_names = {
        "energy_weapons": {
            "ISMediumLaser": {"display": "Medium Laser", "tech": "Inner Sphere"},
            "ISAC20": {"display": "AC/20", "tech": "Inner Sphere"},
        },
        "ammunition": {
            "IS Ammo LRM-10": {"display": "Ammo LRM 10", "tech": "Inner Sphere"},
        },
    }
    ammunition = [
        {
            "id": "150010",
            "name": "Inner Sphere Ammo LRM 10",
            "weapon_ref": "LRM 10",
            "tech_base": "Inner Sphere",
            "weight_tons": "1",
            "ammo_per_ton": "120",
        },
    ]
    return build_alias_index(equipment, equipment_names, ammunition)


class TestAliasLookup:
    def test_exact_mtf_reference(self, sample_index):
        cid, kind = sample_index.lookup(parse_reference("Medium Laser"))
        assert cid == "is-medium-laser"
        assert kind in {"exact", "tech-disambiguated"}

    def test_mech_slot_resolves(self, sample_index):
        cid, _ = sample_index.lookup(parse_reference("Medium Laser; Inner Sphere"))
        assert cid == "is-medium-laser"

    def test_clan_omnipod_resolves(self, sample_index):
        cid, _ = sample_index.lookup(parse_reference("ER Large Laser; Clan (OmniPod)"))
        assert cid == "clan-er-large-laser"

    def test_vehicle_bare_name(self, sample_index):
        cid, _ = sample_index.lookup(parse_reference("LRM 10"))
        assert cid == "is-lrm-10"

    def test_camelcase_via_equipment_names(self, sample_index):
        cid, _ = sample_index.lookup(parse_reference("ISMediumLaser"))
        assert cid == "is-medium-laser"

    def test_vehicle_ammo_hyphen(self, sample_index):
        cid, _ = sample_index.lookup(parse_reference("IS Ammo LRM-10"))
        # may resolve via the 'is ammo lrm 10' alias built from ammunition.json
        assert cid is not None

    def test_structural_returns_none(self, sample_index):
        cid, kind = sample_index.lookup(parse_reference("Empty"))
        assert cid is None and kind == "structural"

    def test_unknown_returns_none(self, sample_index):
        cid, kind = sample_index.lookup(parse_reference("Quantum Disruptor 9000"))
        assert cid is None and kind == "miss"

    def test_fuzzy_suggest_on_typo(self, sample_index):
        suggestions = sample_index.fuzzy_suggest(parse_reference("Mediium Laser"), score_cutoff=70)
        assert any(cid == "is-medium-laser" for cid, _, _ in suggestions)
