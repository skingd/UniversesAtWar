# UniversesAtWar

A Python toolkit that translates BattleTech units into *Legions Imperialis*-style stat blocks and unit cards, enabling BattleTech mechs, vehicles, aerospace fighters, and infantry to be used in the *Universes at War* fan ruleset.

## Requirements

- Python 3.11+
- Install dependencies: `pip install -e .`
- For PDF/card rendering: `pip install -e ".[render]"`
- For development/tests: `pip install -e ".[dev]"`

## CLI Commands

The package exposes four commands after installation:

### `uaw-datacheck`
Validates BattleTech source data files and builds canonical JSON indices used by all downstream tools.

```
uaw-datacheck --data-dir <path-to-BT-data-files> [--output-dir output/data-check] [--index-dir data/index]
```

Outputs reports to `output/data-check/` and writes unit/equipment indices to `data/index/`.

### `uaw-itemize`
Builds itemization catalogues and capability aggregations from the canonical indices.

```
uaw-itemize [--index-dir data/index] [--output-dir output/itemization] [--data-dir <path>]
```

Outputs translation bands, weapon/equipment catalogues, and coverage reports to `output/itemization/`.

### `uaw-base-ranges`
Distills per-unit-type base movement and armor ranges from the canonical indices.

```
uaw-base-ranges [--index-dir data/index] [--output-dir output/base-value-ranges]
```

Outputs `base_ranges.json` and a Markdown summary to `output/base-value-ranges/`.

### `uaw-detachments`
Assembles full detachment stat blocks (armor save, movement, weapons, upgrade options, and points) for each unit type. Weapon profiles are stored as links only — full profile data is joined from `data/WeaponRules.csv` at render time.

```
uaw-detachments [--index-dir data/index] [--weapon-rules data/WeaponRules.csv] [--ammo-rules data/AmmunitionRules.csv] [--bv-cache output/bv_cache.json] [--output-dir output/detachments]
```

Outputs `detachments_mech.json`, `detachments_vehicle.json`, `detachments_aerospace.json`, and a coverage report to `output/detachments/`.

**Points** are derived as 25% of Battle Value (floor), sourced from `output/bv_cache.json`. The cache is built by scraping the [Master Unit List](https://www.masterunitlist.info) — see `scripts/gen_point_assessment.py` for the one-time fetch script. If no cache is found, points default to `null`.

### `uaw-cards` — Detachment Card Generator

Renders every detachment record into a two-sided HTML card page — one HTML file per unit type. Cards match the *Legions Imperialis* card format:

- **Front**: name/detachment-type header, unit type and scale, detachment size, stat row (Movement, Armor Save, Wounds), weapon bullet list, full weapon profile table (Range, Heat, Dice, To-Hit, AP, Type, Traits), special rules.
- **Back**: points cost, detachment description, size upgrade options with dotted-leader costs, special ammo choices.

```
uaw-cards [--detachments-dir output/detachments] [--weapon-rules data/WeaponRules.csv] [--ammo-rules data/AmmunitionRules.csv] [--output-dir output/cards] [--types mech vehicle aerospace] [--limit N]
```

Outputs `output/cards/cards_mech.html`, `cards_vehicle.html`, and `cards_aerospace.html`.

Use `--limit N` to render only the first `N` detachments per type — useful for a quick spot-check without generating the full files:

```
uaw-cards --limit 10 --output-dir output/cards_sample
```

**Full pipeline** (from raw data files through to final cards):

```
# 1. Build canonical indices from raw BattleTech data files
uaw-datacheck --data-dir <path-to-BT-data-files> --index-dir data/index

# 2. Assemble detachment records (with points via BV cache)
uaw-detachments

# 3. Render HTML cards
uaw-cards
```

## Running Tests

```
pytest
```

## Project Layout

| Path | Purpose |
|---|---|
| `src/datacheck/` | Source data validation and index building |
| `src/itemization/` | Weapon/equipment catalogues and translation bands |
| `src/baseranges/` | Movement and armor range analysis |
| `src/detachments/` | Detachment stat block assembly |
| `src/cards/` | HTML card renderer |
| `data/index/` | Generated canonical JSON indices |
| `data/WeaponRules.csv` | Translated weapon stat rules |
| `data/AmmunitionRules.csv` | Translated ammo rules |
| `design/` | Game design documents and translation tables |
| `output/detachments/` | Generated detachment JSON + coverage report |
| `output/cards/` | Generated HTML card pages |
| `output/bv_cache.json` | Cached Battle Value lookups from Master Unit List |
| `output/` | All generated reports (not committed) |
