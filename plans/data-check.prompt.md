# Data Staging & Validation — Pre-Translation Check

## Status
Pre-flight quality gate. **Must pass before any translation code runs.** Produces validation reports in `output/data-check/` and a master canonical index in `data/index/`.

---

## Goals

1. **Universal indexing** — Every BattleMech, vehicle, aerospace fighter, infantry platoon, weapon, equipment item, and reference entity must be addressable by a stable canonical ID, exactly the same way mechs already are (mechs use `mul id` + `chassis`/`model`).
2. **Cross-reference integrity** — Every equipment string referenced inside a unit file (e.g., `"Medium Laser"` in a mech's `Equipment` array) must resolve to a known weapon/equipment entry. Unresolved references would silently drop weapons during translation.
3. **Data hygiene** — Detect malformed files, missing required fields, duplicate IDs, encoding issues, and other data faults before they corrupt the translation pipeline.

---

## Phases

### Phase A: Inventory & Index Build

**A1. Scan & inventory** — Walk all four unit-type directories and `weaponsandequipment/`. For each file, record: path, file extension, size, parse success/failure. Output: `output/data-check/inventory.json`.

**A2. Build canonical equipment index** — Parse every file in `weaponsandequipment/` (ballistic, energy, missile, physical, infantry, equipment, ammunition). For each item produce a canonical record with:
- `canonical_id` — stable slug (e.g., `is-medium-laser`, derived from filename)
- `numeric_id` — the `id` field from the JSON
- `display_name` — the `name` field
- `category` — ballistic / energy / missile / physical / infantry / equipment / ammunition
- `tech_base` — Inner Sphere / Clan / Mixed
- `aliases` — all known name variants (see A4)

Output: `data/index/equipment_index.json` keyed by `canonical_id`.

**A3. Build canonical unit index** — One index per unit type:
- `data/index/mech_index.json` — keyed by `mul id` (fall back to `chassis|model` when `mul id` missing)
- `data/index/vehicle_index.json` — keyed by `mul id` or `name|model`
- `data/index/aerospace_index.json` — same pattern
- `data/index/infantry_index.json` — same pattern

Each entry records: canonical_id, source_path, era, faction(s), tonnage/weight, raw equipment list (as referenced by the unit file).

**A4. Alias map** — Equipment is referenced inside unit files using human-readable strings that may not match `display_name` exactly (e.g., `"ISMediumLaser"`, `"Medium Laser"`, `"CLERMediumLaser"`, `"IS Ammo AC/20"`). Build an alias map by:
- Cross-referencing `equipment_names.json` and `mwo_equipment_descriptions.json`
- Normalizing whitespace, casing, prefix conventions (`IS`/`CL`/`Clan`/`ER`)
- Recording every spelling variant encountered in actual unit files

Output: `data/index/equipment_aliases.json` mapping `alias → canonical_id`.

**A5. Reference-data index** — Build lookup tables for all `reference/*.json` files (factions, eras, quirks, engines, gyros, cockpits, armor types, structure types, ammunition). Output: `data/index/reference_index.json`.

### Phase B: Cross-Reference Validation

**B1. Resolve all unit equipment references** — For every unit file (mech / vehicle / aerospace / infantry), iterate its equipment slots and attempt to resolve each entry via the alias map → equipment index. Record:
- ✅ resolved (alias match)
- ⚠️ resolved with fuzzy match (Levenshtein distance ≤ 2 — needs human review)
- ❌ unresolved (no match found)

Output: `output/data-check/equipment_resolution.json` and a human-readable summary `equipment_resolution.md`.

**B2. Resolve quirks** — For every mech file, verify each entry in the `Quirks` array exists in `reference/quirk_names.json`. Flag unknown quirks.

**B3. Resolve faction references** — For every unit, verify the manufacturer / faction string maps to an entry in `factions.json`. Flag unknown factions.

**B4. Resolve era references** — Verify each unit's `Era` (year) maps to an era in `eras.json`. Flag year-range gaps.

**B5. Resolve ammunition links** — For every weapon that consumes ammo, verify a matching ammo entry exists in `ammunition.json` (linked via `weapon_ref`).

**B6. Resolve structural references** — For mechs, verify `Engine`, `Gyro`, `Cockpit`, `Structure`, `Myomer`, `Armor` strings map to entries in their respective reference files.

### Phase C: Data Hygiene Checks

**C1. Required-field presence** — Per unit type, verify every required field is present and non-empty:
- Mechs: `chassis`, `model`, `Mass`, `Walk MP`, `Armor Points`, `Equipment`, `TechBase`, `Era`
- Vehicles: `Unit Type`, `Motion Type`, `Tonnage`, `Cruise MP`, `Armor Points`
- Aerospace: `Aerospace Class`, `Safe Thrust`, `Structural Integrity`, `Armor Points`, `Fuel`
- Infantry: `Unit Type`, `Motion Type`, `Platoon` block, `Primary Weapon`
- Weapons: `id`, `name`, `tech_base`, `damage`, `range`

**C2. Type & range validation** — Numeric fields are within plausible ranges:
- Mech `Mass` ∈ [10, 100]
- `Walk MP` ∈ [1, 12]
- `Armor Points` totals don't exceed the per-tonnage maximum from `armor_types.json`
- Weapon `damage` is non-negative; `heat` is non-negative

**C3. Duplicate detection** — Flag duplicate `mul id` across mechs, duplicate `id` across weapons, and duplicate filenames in the same era folder.

**C4. Encoding & parse safety** — Re-parse every JSON with strict mode and every YAML with `yaml.safe_load`. Flag files that:
- Contain BOM markers
- Use non-UTF-8 encoding
- Fail to parse
- Contain unexpected control characters

**C5. Source consistency** — Verify `Original File` (when present) and `Source` field references are internally consistent (era folder matches `Source` book).

**C6. Orphan equipment** — Identify equipment entries in `weaponsandequipment/` that are **never referenced** by any unit. These may be obsolete or reserved for future units; record them in a separate report (informational, not blocking).

**C7. Conversion-report integration** — Cross-check the existing `mechs/conversion_report.json` and `mechs/verification_report.json` against our findings — flag any unit that the source pipeline already marked as problematic.

### Phase D: Reporting

**D1. Master report** — `output/data-check/REPORT.md` summarising:
- Total files scanned per category
- Parse success rate
- Equipment resolution rate (% resolved exact / fuzzy / unresolved)
- Top 20 unresolved equipment strings (with frequency)
- All malformed files (path + reason)
- All duplicate IDs
- Orphan equipment count
- Pass / fail verdict per check

**D2. Per-issue CSVs** — Machine-readable detail files:
- `unresolved_equipment.csv` — unit_path, equipment_string, fuzzy_candidates
- `malformed_files.csv` — path, parse_error
- `duplicates.csv` — id, paths
- `missing_fields.csv` — path, missing_field
- `range_violations.csv` — path, field, value, allowed_range

**D3. Pass/fail gate** — `pipeline.py` checks `output/data-check/REPORT.md` for a `STATUS: PASS` marker before allowing translation to run. Hard-fail conditions: any parse failure, any duplicate canonical ID, any unresolved equipment > threshold (default 1%).

---

## Implementation Plan

### Files to Create

| Path | Purpose |
|---|---|
| `src/datacheck/__init__.py` | Package marker |
| `src/datacheck/inventory.py` | Phase A1 — file walk + parse status |
| `src/datacheck/index_builder.py` | Phases A2–A5 — build all indices |
| `src/datacheck/alias_resolver.py` | Phase A4 — equipment alias normalization + fuzzy match |
| `src/datacheck/cross_reference.py` | Phase B — all resolution checks |
| `src/datacheck/hygiene.py` | Phase C — field/range/encoding/duplicate checks |
| `src/datacheck/reporter.py` | Phase D — report generation |
| `src/datacheck/cli.py` | Entry point: `python -m src.datacheck` |
| `tests/datacheck/test_alias_resolver.py` | Unit tests for alias normalization edge cases |
| `tests/datacheck/test_cross_reference.py` | Unit tests for resolution logic |

### CLI

```
python -m src.datacheck [OPTIONS]

Options:
  --data-dir          Path to BT Data Files root (required)
  --output-dir        Path for reports (default: output/data-check/)
  --index-dir         Path for canonical indices (default: data/index/)
  --strict            Treat warnings as failures
  --fuzzy-threshold   Max Levenshtein distance for fuzzy matches (default: 2)
  --fail-threshold    Max % unresolved equipment (default: 1.0)
  --rebuild-aliases   Force rebuild of alias map (slow)
```

### Dependencies
```
pyyaml          # YAML parsing
defusedxml      # if XML present
rapidfuzz       # fast fuzzy string matching for alias resolution
```

---

## Output Artifacts

```
data/
└── index/                                  ← canonical indices (committed; consumed by translators)
    ├── equipment_index.json
    ├── equipment_aliases.json
    ├── reference_index.json
    ├── mech_index.json
    ├── vehicle_index.json
    ├── aerospace_index.json
    └── infantry_index.json

output/
└── data-check/                             ← validation reports (gitignored; regenerated each run)
    ├── REPORT.md                           ← human-readable master report
    ├── inventory.json
    ├── equipment_resolution.json
    ├── equipment_resolution.md
    ├── unresolved_equipment.csv
    ├── malformed_files.csv
    ├── duplicates.csv
    ├── missing_fields.csv
    ├── range_violations.csv
    └── orphan_equipment.csv
```

---

## Verification

1. Run `python -m src.datacheck --data-dir "C:\Users\sking\OneDrive\Gaming\battletech\Data Files"` — completes without crashing on the full dataset.
2. Open `output/data-check/REPORT.md` — confirm all six categories report counts and the resolution rate exceeds 99%.
3. Spot-check 5 mechs (one per era: 3025, 3050, 3067, 3145, ilClan) — every weapon in their `Equipment` arrays is resolved in `equipment_resolution.json`.
4. Spot-check 3 Clan-tech mechs — Clan-prefixed weapon variants resolve correctly via the alias map.
5. Confirm `data/index/equipment_index.json` is non-empty and contains entries for all six weapon categories + ammunition.
6. Confirm any `STATUS: FAIL` in the report blocks downstream translation when running `python src/pipeline.py`.

---

## Decisions

- **Indexing parity** — Vehicles, aerospace, and infantry get the same `mul id`-based index treatment as mechs. Where `mul id` is missing, fall back to `name|model` composite key.
- **Equipment as first-class entities** — Every weapon, ammo, and equipment item gets a canonical_id (slug) used universally downstream. Unit files reference equipment by canonical_id after the alias resolution step writes back normalized references — OR the translator does the lookup at runtime via the alias map. **Recommendation: runtime lookup** (don't mutate source data).
- **Fuzzy matching is human-review-only** — Fuzzy matches are reported but never auto-applied; the alias map only contains exact aliases that have been verified.
- **Indices are committed to the repo** under `data/index/` — they are deterministic build artifacts of the source data and required for downstream code.
- **Reports are gitignored** under `output/data-check/`.
- **Data files are read-only** — the data-check stage never writes to `Data Files/`.

---

## Further Considerations

1. **Source data updates** — When the user updates `Data Files/` (new units published), how is re-indexing triggered? Recommend: add a freshness check at the top of `pipeline.py` that re-runs datacheck if any source file mtime is newer than `data/index/equipment_index.json`.
2. **Alias map maintenance** — The alias map will grow as new spellings are encountered. Should unresolved-with-fuzzy-suggestion entries be auto-promoted to aliases after manual review? Recommend: a `--accept-fuzzy <unit_path>` CLI flag that promotes the fuzzy suggestion for that file's references into the alias map.
3. **Performance** — Walking 3,000+ unit files and resolving every equipment slot may take time. If runtime exceeds 30 seconds, add concurrent file parsing via `concurrent.futures.ProcessPoolExecutor`.
4. **Schema drift** — If the user updates `Data Files/` and field shapes change (e.g., `Armor Points` becomes a different structure), hygiene checks will catch it but won't auto-adapt. Acceptable trade-off.
