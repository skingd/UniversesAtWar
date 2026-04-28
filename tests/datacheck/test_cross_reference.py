"""Tests for cross-reference resolution."""
from __future__ import annotations

from src.datacheck.alias_resolver import build_alias_index
from src.datacheck.cross_reference import (
    resolve_eras,
    resolve_quirks,
    resolve_unit_equipment,
)


def _make_alias_index():
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
            "mtf_reference": "AC/20",
            "category": "ballistic",
            "tech_base": "Inner Sphere",
        },
    ]
    return build_alias_index(equipment)


def test_resolve_unit_equipment_counts_correctly():
    alias = _make_alias_index()
    units = {
        "mech": [{
            "key": "1",
            "chassis": "Test",
            "model": "X",
            "source_path": "/tmp/x.json",
            "raw_equipment_refs": [
                "Empty",                        # structural
                "Medium Laser; Inner Sphere",   # exact
                "AC/20; Inner Sphere",          # exact
                "Hand Actuator",                # structural
                "Bogus Weapon Mk7",             # unresolved
            ],
            "raw_quirks": [],
        }],
    }
    report, issues = resolve_unit_equipment(units, alias)
    totals = report["totals"]
    assert totals["total_refs"] == 5
    assert totals["structural"] == 2
    assert totals["unresolved"] == 1
    # 2 resolved out of 3 non-structural = 66.67%
    assert 60 < report["resolution_rate"] <= 67
    # issue should be raised for the unresolved entry
    assert any(i.category == "unresolved-equipment" for i in issues)


def test_resolve_quirks_known_and_unknown():
    units = {
        "mech": [{
            "key": "1",
            "source_path": "/tmp/x.json",
            "raw_quirks": [
                "Battle Fists LA",       # known (with location suffix)
                "Command Mech",          # known
                "Fictional Quirk",       # unknown
            ],
        }],
    }
    reference = {
        "quirk_names": {
            "positive": {
                "battle_fists_la": "Battle Fists LA",
                "command_mech": "Command Mech",
            },
            "negative": {},
            "weapon_quirks": {},
        }
    }
    report, issues = resolve_quirks(units, reference)
    assert report["total"] == 3
    assert report["unknown_count"] == 1
    assert any("Fictional Quirk" in i.message for i in issues)


def test_resolve_eras_flags_out_of_range():
    units = {
        "mech": [
            {"key": "1", "source_path": "/tmp/a.json", "era": 3050},
            {"key": "2", "source_path": "/tmp/b.json", "era": 9999},  # outside any era
            {"key": "3", "source_path": "/tmp/c.json", "era": None},   # skipped
        ],
    }
    reference = {
        "eras": [
            {"name": "Clan Invasion", "startYear": 3049, "endYear": 3061},
        ]
    }
    report, issues = resolve_eras(units, reference)
    assert report["total_with_year"] == 2
    assert report["out_of_range"] == 1
    assert any(i.category == "era-gap" for i in issues)
