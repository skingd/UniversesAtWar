# Detachment Profile JSON — First Pass (`detachments_*.json`)

## Status
First-pass data pipeline that consumes the canonical `data/index/*` records and produces per-unit-type detachment JSON files for use by the future graphical card generator. **No graphical output**; this plan is data-only.

## Purpose
`design/units-translation.md` defines every translation needed to turn a BattleTech unit blob into a Universes At War detachment profile (armor save, movement, wounds, scale, detachment size, weapon expansion, special rules). This pipeline applies those translations end-to-end and emits machine-readable JSON the rendering layer can consume directly.

### Inputs
- `data/index/{mech,vehicle,aerospace}_index.json` — already carry `walk_mp`/`cruise_mp`/`safe_thrust`, `armor_total`, `tonnage`, `tech_base`, `raw_equipment_refs` (per-slot, one entry per physical installation).
- `data/index/equipment_aliases.json` — alias map for resolving raw weapon names against the rules CSV.
- `data/WeaponRules.csv` — canonical weapon profiles (`Weapon Name, Range, Heat, Dice, To-Hit, AP, Type, Traits`).
- `data/AmmunitionRules.csv` — special-ammo options per weapon (`Ammo Name, Weapon Name, Range, Heat, Dice, To-Hit, AP, Type, Traits, Points`).
- `design/units-translation.md` — translation tables.

### Outputs
All under `output/detachments/`:
- `detachments_mech.json`
- `detachments_vehicle.json`
- `detachments_aerospace.json`
- `coverage.json` / `coverage.md` — unmapped weapons, missing speed rows, skipped units.

### Locked decisions
- **Scope:** mech + vehicle + aerospace. Infantry deferred to a follow-up plan.
- **File shape:** per-type files (the eventual card generator iterates one type at a time).
- **Source filter:** `tech_base ∈ {Inner Sphere, Clan}` — primitive / mixed / unknown are skipped (counted in coverage).
- **Points:** schema field present, value `null` (no formula yet).
- **Unmapped weapons:** emitted with `unmapped: true` + null profile fields; aggregated into the coverage report.
- **Equipment → special_rules:** name-only passthrough from the unit file (per `design/units-translation.md` §Equipment Translation). No rule glossary lookup.

### Out of scope
- No card / image / PDF rendering.
- No modifications to `data/index/*` or any unit files.
- No points calculation.
- No special-rule glossary or rule-text resolution.
- Infantry detachments.

---

## Detachment record schema

```jsonc
{
  "id":             "<canonical_id>",
  "name":           "Atlas (AS7-D)",
  "detachment":     "BattleMech" | "Vehicle Lance" | "Vehicle Star" | "Aerospace Lance" | "Aerospace Star",
  "unit_type":      "BattleMech" | "Vehicle" | "Aerospace",
  "scale":          4,
  "tier":           "assault",
  "tech_base":      "Inner Sphere" | "Clan",
  "tonnage":        100.0,
  "armor_save":     "3+",
  "movement":       "5\"",
  "wounds":         8,
  "detachment_size": { "base": 1, "max": 1 },
  "points":         null,
  "weapons": [
    { "name": "AC/20", "range": "3\"", "dice": 20, "to_hit": "5+",
      "ap": -4, "heat": 7, "type": "Ballistic", "traits": ["Anti-Tank"],
      "unmapped": false },
    /* one entry per physical weapon — no x2 / (2) compression */
  ],
  "upgrade_options": {
    "special_ammo": [
      { "name": "ER", "weapon": "Clan ATM 6", "range": "2\"-14\"",
        "dice": 1, "to_hit": "4+", "ap": -2, "heat": 1,
        "type": "Missile", "traits": ["Anti-Tank"], "points": 5 }
    ],
    "detachment_size": [
      { "size": 8, "points": null },
      { "size": 12, "points": null }
    ]
  },
  "special_rules":  ["Artemis IV", "ECM Suite", "MASC"],
  "source_path":    "<absolute path>"
}
```

---

## Phases

### Phase 1 — Translation tables module
File: `src/detachments/tables.py` (pure data + lookup functions).

1. `armor_save(armor_total, unit_type)` — mech ladder: `0–99=5+, 100–299=4+, 300–400=3+, 401+=2+`. Vehicle/Aerospace share: `0–20=5+, 21–80=4+, 81–250=3+, 251–300=2+, 301+=1+`.
2. `movement_inches(speed, unit_type)` — per-type lookup (mech/aerospace/vehicle). The mech and aerospace tables in `design/units-translation.md` skip speed `13`; the recommended handling is **fall to the next-lower row + log warning** (collected in coverage). See _Open considerations_ §1.
3. `wounds(tonnage, unit_type)` — tier ladder per type (mech/vehicle: light/medium/heavy/assault; aerospace: light/medium/heavy/superheavy).
4. `scale(tonnage, unit_type)` — same tier ladder, different values per type.
5. `detachment_size(tonnage, unit_type, tech_base)` — `(base, max)`. Mechs always `(1, 1)`. Vehicles/aerospace use the IS vs Clan tables.
6. `detachment_label(unit_type, tech_base)` — `"BattleMech"` for mechs; `"Vehicle Lance"` (IS) / `"Vehicle Star"` (Clan); `"Aerospace Lance"` (IS) / `"Aerospace Star"` (Clan). See _Open considerations_ §2.

Tests: `tests/detachments/test_tables.py` — every breakpoint + every tier + both tech bases + the missing-speed gaps.

### Phase 2 — Weapon catalogue loader
File: `src/detachments/weapons.py`.

1. `load_weapon_rules(path)` → `dict[str, WeaponProfile]`. Fields kept verbatim from CSV; `dice`/`heat`/`ap` parsed to int; `traits` split on `, `; `range` and `to_hit` stay strings (range can be `"8\""` or `"2\"-14\""`).
2. `load_ammunition_rules(path)` → `dict[str, list[AmmoOption]]`, grouped by `Weapon Name`, each entry carrying its `Ammo Name`, full profile, and `points`.
3. `resolve_weapon(raw_name, weapon_index, alias_index)` → canonical CSV `Weapon Name` or `None`. Resolution order:
   1. Exact match.
   2. Strip `Inner Sphere ` / `Clan ` prefix and retry.
   3. Consult `data/index/equipment_aliases.json`.
   4. Give up (caller marks the weapon `unmapped`).

Tests: `tests/detachments/test_weapons.py` — synthetic CSV fixture; spot-check alias paths (`Inner Sphere AC/20` → `AC/20`, `Clan ER Large Laser` round-trips, `LRM 20` resolves both with and without prefix).

### Phase 3 — Equipment → special-rules passthrough
File: `src/detachments/equipment.py`.

1. `partition_refs(raw_refs, weapon_index, alias_index)` → `(weapon_refs, equipment_refs)`. Anything that resolves via `resolve_weapon` is a weapon; everything else is equipment.
2. `special_rules_from_equipment(equipment_refs)` — drop bare structure/armor types (Ferro-Fibrous, Endo Steel, etc.) and any residual ammo strings; keep everything else **as named in the unit file**, dedup, preserve first-seen order. Drop list lives in a single `_DROP_SUBSTRINGS` constant for easy extension.

Tests: `tests/detachments/test_equipment.py` — synthetic ref lists exercising drops, dedup, and order preservation.

### Phase 4 — Detachment assembly
File: `src/detachments/assemble.py`.

1. `build_detachment(unit_record, weapon_index, ammo_index, alias_index)` → record matching the schema above. Weapon list is **expanded one row per physical installation** (so two LRM 20s produce two entries). `upgrade_options.special_ammo` is the union of `ammo_index[weapon_name]` entries for each unique weapon present.
2. `build_all(records, unit_type, ...)` → `(detachments, coverage)`. Filters by tech base, dispatches per record, accumulates a `Coverage` dataclass.
3. `Coverage` → JSON-serializable: `unmapped_weapons: {name: count}`, `missing_speed: [{unit_id, speed}]`, `skipped_unknown_tech_base: int`, `skipped_missing_armor: int`, `skipped_missing_movement: int`.

Tests: `tests/detachments/test_assemble.py` — fixtures for an Atlas-like, a Locust-like, a Demolisher-like, and one ASF; assert weapon expansion (no compression), special-ammo synthesis, IS-vs-Clan detachment-size split, and the `tech_base` filter.

### Phase 5 — CLI + wiring
- `src/detachments/cli.py` + `src/detachments/__main__.py`.
- Flags: `--index-dir data/index`, `--weapon-rules data/WeaponRules.csv`, `--ammo-rules data/AmmunitionRules.csv`, `--output-dir output/detachments`, `--types mech vehicle aerospace`.
- Writes `detachments_<type>.json` per type plus `coverage.{json,md}`.
- Prints per-type summary: `N detachments, M unmapped weapons, K skipped`.
- Register `uaw-detachments = "src.detachments.cli:main"` in `pyproject.toml`.

### Phase 6 — Verification
1. Full pytest suite green (existing 115 + new tests).
2. Run `uaw-detachments` against the existing indices.
3. Spot-checks:
   - **Atlas AS7-D** (armor 304, walk 3, 100t): `armor_save=3+`, `movement=5"`, `wounds=8`, `scale=4`, `detachment="BattleMech"`. Weapons include AC/20 + 2× Medium Laser + LRM 20 + SRM 6, all `unmapped=false`.
   - **Locust LCT-1V** (armor 64, walk 8, 20t): `armor_save=5+`, `movement=10"`, `wounds=2`, `scale=2`.
   - **Demolisher (Mk. I)** (cruise 3, 80t, IS): `detachment="Vehicle Lance"`, `detachment_size={base:4, max:12}`, `scale=2`.
   - One Clan vehicle: `detachment="Vehicle Star"`, `detachment_size={base:5, max:15}`.
4. Inspect `coverage.md`: top-N unmapped weapons each become a TODO row to add to `WeaponRules.csv`. Confirm `missing_speed` and `skipped_*` counts are sensible (expected: small).

---

## Relevant files
- `design/units-translation.md` — translation tables (read-only).
- `data/WeaponRules.csv`, `data/AmmunitionRules.csv` — weapon + ammo source.
- `data/index/{mech,vehicle,aerospace}_index.json` — extended unit index.
- `data/index/equipment_aliases.json` — alias map.
- `src/datacheck/index_builder._extract_equipment_refs` — confirms each equipment slot is one entry (basis for "no x2" weapon expansion).
- `src/itemization/aggregations.{mech_tier,vehicle_tier,aerospace_tier}` — reuse for `tier` field on each record.
- New module: `src/detachments/{__init__.py, __main__.py, cli.py, tables.py, weapons.py, equipment.py, assemble.py}`.
- New tests: `tests/detachments/test_{tables,weapons,equipment,assemble}.py`.
- `pyproject.toml` — add `uaw-detachments` entry point.

## Open considerations
1. **Missing speed rows in `design/units-translation.md`:** mech and aerospace tables both skip `13`. _Recommendation:_ collapse to the next-lower row and warn in coverage. _Alternative:_ raise it as a translation-table gap and refuse to convert affected units.
2. **Clan detachment naming:** the design doc only names IS variants. _Recommendation:_ `"Vehicle Star"` / `"Aerospace Star"` for Clan, mirroring BattleTech canon. Confirm before Phase 1 ships.
3. **`upgrade_options.detachment_size` with null points:** acceptable as a placeholder, or omit the array entirely until a points formula exists?
