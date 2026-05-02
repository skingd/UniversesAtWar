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
Assembles full detachment stat blocks (armor save, movement, weapons, upgrade options) for each unit type.

```
uaw-detachments [--index-dir data/index] [--weapons-csv data/WeaponRules.csv] [--ammo-csv data/AmmunitionRules.csv] [--output-dir output/detachments]
```

Outputs `detachments_mech.json`, `detachments_vehicle.json`, `detachments_aerospace.json`, and a coverage report to `output/detachments/`.

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
| `data/index/` | Generated canonical JSON indices |
| `data/WeaponRules.csv` | Translated weapon stat rules |
| `data/AmmunitionRules.csv` | Translated ammo rules |
| `design/` | Game design documents and translation tables |
| `output/` | Generated reports (not committed) |
