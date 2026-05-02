# Base Value Ranges — Movement & Armor Distillation

## Status
Read-only analysis pipeline that runs **after** `uaw-datacheck` has rebuilt the canonical indices. Produces per-unit-type base movement and armor min/max/median ranges in `output/base-value-ranges/`. **Never modifies unit files.**

## Purpose
Translation from BattleTech to Legions Imperialis requires concrete numeric brackets for:

- **Movement** — to map BattleTech base movement points onto LI movement inches.
- **Armor** — to assign LI armor save values from BattleTech armor totals.

This report distills, per unit type, the actual observed minimum, maximum, and median for both metrics — overall, and broken down by tonnage tier (or motion mode for infantry). The output drives later rule decisions in `design/rules.prompt.md`.

### Out of scope
- **MASC bonus** — handled separately as its own translation rule.
- **Run/flank** — derived from base movement; not aggregated here.
- **Jump bonus** — same; jump appears in the index but is not part of the base movement range.
- **Any modification of source unit files.**

---

## Inputs
- `data/index/{mech,vehicle,aerospace,infantry}_index.json` — canonical indices, **extended** with base-stat fields by `src/datacheck/index_builder.py` (Phase 1).

### Required index fields per unit type
| unit_type   | movement field    | armor field     | tier dimension |
|-------------|-------------------|-----------------|----------------|
| `mech`      | `walk_mp`         | `armor_total`   | tonnage tier (`mech_tier`)      |
| `vehicle`   | `cruise_mp`       | `armor_total`   | tonnage tier (`vehicle_tier`)   |
| `aerospace` | `safe_thrust`     | `armor_total`   | tonnage tier (`aerospace_tier`) |
| `infantry`  | `movement_points` | _(n/a)_         | `movement_mode` (motion type)   |

If any of these fields is absent from every record of a unit type, the index pre-dates Phase 1 and `--strict` will refuse to run.

## Outputs
All under `output/base-value-ranges/`:
- `base_ranges.json` — machine-readable per-unit-type summary (count, min, max, mean, median, p10/p25/p50/p75/p90/p95/p99 for movement and armor).
- `base_ranges.md` — human-readable tables per unit type: an Overall row plus a per-tier breakdown.

---

## Architecture

### Phase 1 — Extend the index (one-time code change, then re-scan)
1. Promote shared helpers into `src/datacheck/stats.py`:
   - `to_float`, `to_int` (single source of truth; `src/itemization/common.py` re-exports).
   - `extract_walk_mp`, `extract_jump_mp` (distinguishes explicit `0` from missing), `extract_run_mp` (⌈walk × 1.5⌉ fallback), `extract_cruise_mp`, `extract_safe_thrust`, `extract_armor_total` (sums dict / list / scalar shapes), `extract_infantry_movement` (returns `(mp, motion_type)`), plus `extract_engine_rating` and `extract_heat_sink_count` for downstream reuse.
2. Update `src/itemization/aggregations.py` to import the extractors from `src.datacheck.stats` instead of defining them locally.
3. Extend `src/datacheck/index_builder.build_unit_index` so each record carries the unit-type-specific base fields above. New helper `_extract_base_stats(data, unit_type)` dispatches per type.

### Phase 2 — New `uaw-base-ranges` module
- `src/baseranges/compute.py` — pure functions:
  - `UNIT_TYPE_CONFIG` — per-unit-type field + tier configuration.
  - `compute_unit_type(records, unit_type)` → `{overall: {n, movement, armor}, by_tier: {tier: {n, movement, armor}}}` using `src.itemization.common.summarize` for stat blocks and `src.itemization.aggregations.{mech,vehicle,aerospace}_tier` for tonnage classifiers.
  - `compute_all(indices_by_type)` — runs all available types.
  - `required_field_counts(records, unit_type)` — strict-mode safety check.
- `src/baseranges/reporter.py` — writes both `base_ranges.json` and the Markdown tables.
- `src/baseranges/cli.py` — `uaw-base-ranges` entry point with `--index-dir`, `--output-dir`, `--strict`.

### Phase 3 — Wiring + smoke verification
- Register `uaw-base-ranges = "src.baseranges.cli:main"` in `pyproject.toml`.
- Run the full pytest suite; both new test modules must pass alongside the existing tests.
- **Subagent rule:** any rescan of the raw `Data Files/` corpus or regenerated indices must be dispatched as a `runSubagent` task — never inline. The raw corpus lives on the source machine; the agent driving this plan does not have it locally.

## Tests
- `tests/datacheck/test_stats.py` — every extractor against synthetic parsed-dict fixtures, including the critical "Jump MP: 0 vs missing" distinction and the dispatcher in `_extract_base_stats`.
- `tests/baseranges/test_compute.py` — synthetic per-unit-type record sets exercising overall + per-tier min/max/median, missing-field skipping, infantry-by-motion-mode bucketing, and `--strict` field counts.

## Operational use
Typical workflow once raw data is present:
```
uaw-datacheck --data-dir <Data Files>      # rebuild indices with base stats
uaw-base-ranges --strict                   # produce output/base-value-ranges/
```

Without `--strict`, the tool will silently emit empty summaries when the index is stale; with `--strict`, it exits non-zero and instructs the user to re-run `uaw-datacheck`.
