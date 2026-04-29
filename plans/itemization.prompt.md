# Itemization & Capability Aggregation — Rules Porting Verification

## Status
Verification gate that runs **after** `data-check` has passed and **before** translation rules are finalized in `design/rules.prompt.md`. Produces master itemization catalogues and capability distribution reports in `output/itemization/`.

## Purpose
To guarantee that **every weapon, equipment item, and unit capability** present in the source data is enumerated and statistically characterised before any translation table is written. Without this list we cannot prove rule coverage, and without the aggregations we cannot collapse continuous BattleTech ranges (range bands, MP, tonnage, heat, damage) into the discrete LI attribute bands (`SHORT/MEDIUM/LONG`, movement inches, armour saves, etc.).

This work has **two parts**:
1. **Part 1 — Itemization:** an exhaustive, deduplicated catalogue of every installable thing (weapons, ammo, equipment, upgrades).
2. **Part 2 — Aggregation:** statistical distributions of every numeric capability across units and weapons, used to derive translation thresholds.

---

## Inputs
- `data/index/equipment_index.json` — canonical equipment catalogue (from `data-check` Phase A)
- `data/index/equipment_aliases.json` — alias map
- `data/index/{mech,vehicle,aerospace,infantry}_index.json` — unit indices
- `data/index/reference_index.json` — reference data (engines, gyros, armor, structure, quirks)
- Raw unit files under `mechs/`, `vehicles/`, `aerospace/`, `infantry/`
- Raw equipment under `weaponsandequipment/`

## Outputs
All under `output/itemization/`:
- `weapons.json` / `weapons.md`
- `ammunition.json` / `ammunition.md`
- `equipment.json` / `equipment.md`
- `upgrades.json` / `upgrades.md`
- `capabilities_units.json` / `capabilities_units.md`
- `capabilities_weapons.json` / `capabilities_weapons.md`
- `translation_bands.json` — proposed LI bucket boundaries derived from the aggregations
- `REPORT.md` — master summary with coverage metrics

---

# Part 1 — Itemization Catalogue

## Goal
Produce a single, deduplicated, canonical list of **every installable thing** in the dataset, grouped by functional class. Each entry must carry enough metadata to be matched 1:1 against an entry in the eventual LI translation table.

## P1.1 — Weapons Catalogue
Walk every weapon file in `weaponsandequipment/` (ballistic, energy, missile, physical, infantry weapons). Emit one row per `canonical_id` with:

| Field | Source | Notes |
|---|---|---|
| `canonical_id` | equipment index | stable slug |
| `display_name` | `name` | |
| `category` | folder | ballistic / energy / missile / physical / infantry |
| `subcategory` | inferred | autocannon / gauss / PPC / laser / pulse / LRM / SRM / MRL / streak / ATM / flamer / MG / melee / etc. |
| `tech_base` | `tech_base` | IS / Clan / Mixed / Primitive |
| `damage` | `damage` | numeric or cluster note |
| `heat` | `heat` | |
| `min_range` / `short` / `medium` / `long` / `extreme` | range block | hexes |
| `tonnage` | `tonnage` | |
| `crit_slots` | `criticals` | |
| `ammo_per_ton` | linked ammo | nullable |
| `cluster` | `cluster_table` ref | LRM/SRM/MRL/cluster only |
| `special_rules` | `special` array | OS, AP, X-Pulse, Streak, ER, LB-X, Ultra, Rotary, Rapid-Fire, etc. |
| `era_introduced` / `era_extinct` | availability | |
| `usage_count` | unit cross-ref | how many distinct units mount it |
| `mounting_unit_types` | unit cross-ref | mech / vehicle / aerospace / infantry / battlearmor |

Sort by `category`, `tech_base`, `tonnage`. Output to `weapons.json` and a Markdown table in `weapons.md`.

## P1.2 — Ammunition Catalogue
Same structure for every ammo entry, plus:
- `weapon_ref` — canonical_id of the weapon(s) that consume it
- `shots_per_ton`
- `damage_modifier` — for special munitions (Inferno, Precision, Armor-Piercing, Tandem-Charge, Smoke, Flare, Mine Clearance, Swarm, Narc-capable, Artemis-capable, etc.)
- `special_munition_flag` — boolean

## P1.3 — Equipment Catalogue
Every non-weapon, non-ammo item that can occupy a critical slot. Includes (non-exhaustive): heat sinks (single, double, Clan DHS, laser HS, compact), jump jets (standard, improved, mech-mech-pack), CASE / CASE II, Targeting Computer, C3 (Master / Slave / Boosted / Improved / Emergency), TAG, Narc, Artemis IV / V FCS, Apollo FCS, Beagle Active Probe / Bloodhound / Light Active Probe / Watchdog, Guardian / Angel / Chameleon ECM, Null-Signature, Void-Signature, AES, MASC, Supercharger, Triple-Strength Myomer, Hardened/Reactive/Reflective/Stealth/Ferro-Lamellor armor mounts, Endo Steel / Composite / Reinforced internals, XL/Light/XXL/Compact/Fuel-Cell/ICE engines, gyros (Standard/XL/Heavy-Duty/Compact), cockpits (Standard/Small/Industrial/Command/Torso-Mounted/Primitive), Cargo, Lift Hoists, Searchlights, Communications gear, Mine Dispensers, Remote Sensor Dispensers, Coolant Pods, etc.

Per entry capture:
- `canonical_id`, `display_name`, `category` (heat / mobility / electronics / defence / fcs / structural / utility)
- `tonnage`, `crit_slots`
- `tech_base`, `era_introduced` / `era_extinct`
- `mechanical_effect` — short text drawn from source description
- `usage_count`, `mounting_unit_types`

## P1.4 — Upgrades Catalogue
A separate view that filters Part 1.3 down to **chassis-level upgrades** that change a unit's identity rather than just adding a capability. These are the items most likely to require a dedicated LI special rule rather than a stat tweak. Required entries (verify each is present):

- Engine types: XL, Light, XXL, Compact, Fuel-Cell, Fission, ICE, Primitive
- Internal structure: Endo Steel, Endo-Composite, Composite, Reinforced, Industrial, Primitive
- Armor types: Standard, Ferro-Fibrous (Light/Heavy/Standard), Ferro-Lamellor, Hardened, Reactive, Reflective, Stealth, Stealth (Vehicle), Ferro-Aluminum (aero), Patchwork
- Gyros: XL, Heavy-Duty, Compact
- Cockpits: Small, Command, Torso-Mounted, Primitive, Industrial, Interface
- Movement upgrades: MASC, Supercharger, TSM, Partial Wing, Jump Booster, Mechanical Jump Boosters, UMU
- Signature/EW: Stealth Armor system, Null-Sig, Void-Sig, Chameleon LPS, Mimetic Armor (BA)
- Command/coordination: C3 family, TAG, Narc, Improved Narc, Artemis IV/V, Apollo
- Heat: Coolant Pod, Compact HS, Laser HS, Clan DHS, RISC Heat Sinks
- Specialty: AES, BattleMech Shield, Claws, Talons, Spikes, Bloodhound APS

For each upgrade, additionally record:
- `affects_stat` — which LI stat it should bias (move / armour-save / range-band / special-rule-only)
- `binary_or_scaled` — does it grant a flag, or modify a number?

## P1.5 — Coverage Verification
Cross-check that:
- Every `canonical_id` in `equipment_index.json` appears in exactly one of the four catalogues above.
- Every equipment string referenced by any unit (post alias resolution) appears in P1.1–P1.3.
- Every entry in P1.4 maps back to a row in P1.3.
- Flag any item that has `usage_count == 0` as **orphan** (informational, not blocking).
- Flag any item present in unit files but missing from all four catalogues as **uncatalogued** (blocking — must be fixed before Part 2 runs).

---

# Part 2 — Capability Aggregation

## Goal
For every numeric capability that influences LI translation, compute the full distribution so that the rules document can pick defensible bucket boundaries instead of guessing.

## P2.1 — Unit Capability Distributions
For each unit type (mech / vehicle / aerospace / infantry) compute, per numeric field:

- `count` (non-null)
- `min`, `max`
- `mean`, `median` (the user's "average and mean")
- `std_dev`
- percentiles: `p10`, `p25`, `p50`, `p75`, `p90`, `p95`, `p99`
- `histogram` — bucketed counts at the field's natural granularity (1 MP, 5 tons, 10 armour points, etc.)
- `by_tier` breakdown (light / medium / heavy / assault for mechs; equivalent slicing for the others)
- `by_era` breakdown
- `by_tech_base` breakdown (IS / Clan / Mixed)

Required fields per unit type:

**BattleMechs**
- `tonnage`
- `walk_mp`, `run_mp` (derived = ⌈walk × 1.5⌉), `jump_mp`
- `engine_rating`
- total `armor_points`, armor-by-location (head / CT / CT-rear / side torso / side-torso-rear / arm / leg)
- total `internal_structure`
- `heat_sink_count`, `heat_sink_type`
- `weapon_count`, `total_weapon_tonnage`, `total_weapon_heat_alpha` (sum of `heat` if all weapons fire)
- `crit_slots_used` / `crit_slots_free`
- `BV` and `BV2` if present
- `quirk_count`

**Combat Vehicles**
- `tonnage`
- `cruise_mp`, `flank_mp` (= ⌈cruise × 1.5⌉)
- armor totals by facing (front / side / rear / turret)
- `crew_size`, `weapon_count`, `total_weapon_heat_alpha`
- `motion_type` distribution (categorical)

**Aerospace**
- `tonnage`
- `safe_thrust`, `max_thrust`
- `structural_integrity`
- armor by facing (nose / wing / aft)
- `fuel_points`
- `weapon_count`, `total_weapon_heat_alpha`

**Infantry**
- `platoon_size`
- `motion_type` distribution
- `damage_per_trooper`, `range_brackets`
- `armor_divisor` (if present)
- `anti_mech_capable` rate
- `field_gun_count` and gun tonnage

Output: `capabilities_units.json` (machine-readable) and `capabilities_units.md` (formatted tables grouped by unit type).

## P2.2 — Weapon Capability Distributions
Across the entire weapons catalogue, compute the same statistical block (`min/max/mean/median/std/percentiles/histogram`) for:

- `damage` (per-shot, and per-cluster expected value for missile/cluster weapons)
- `heat`
- `min_range`, `short`, `medium`, `long`, `extreme`
- `tonnage`
- `crit_slots`
- `ammo_per_ton` (where applicable)
- derived: `damage_per_heat`, `damage_per_ton`, `damage_per_crit`, `range_total = short + medium + long`

Slice each distribution by:
- `category` (ballistic / energy / missile / physical / infantry)
- `subcategory` (autocannon / laser / PPC / LRM / SRM / etc.)
- `tech_base` (IS / Clan / Mixed)
- `era_introduced` bucket

Output: `capabilities_weapons.json` and `capabilities_weapons.md`.

## P2.3 — Range Band Derivation (the critical reduction)
This is the headline use of Part 2. BattleTech weapons have continuous range bands measured in hexes (typically `short / medium / long`, sometimes plus `min` and `extreme`). LI uses a small fixed set of attribute ranges (`SHORT`, `MEDIUM`, `LONG` measured in inches).

Procedure:
1. From P2.2, take the `long` range distribution across all direct-fire weapons.
2. Compute terciles or k-means clusters (k = 3, plus a 4th `MELEE/POINT-BLANK` bucket for `long ≤ 1`).
3. Propose cut points: e.g. `SHORT ≤ p33`, `MEDIUM ≤ p66`, `LONG > p66`.
4. Validate the proposal by checking that signature weapons end up in their canonical bucket (Medium Laser → SHORT, AC/20 → SHORT, AC/2 → LONG, ER PPC → LONG, Gauss → LONG, LRM-20 → LONG, SRM-6 → SHORT). Adjust until at least 90 % of canonical weapons land correctly.
5. Emit the chosen cut points to `translation_bands.json` along with the rationale.

Repeat the same procedure to derive bands for:
- **Movement** — collapse `walk_mp` (and vehicle `cruise_mp`) into LI movement inches via terciles, then validate against canonical units (Locust → fastest, Atlas → slowest).
- **Armour saves** — collapse total `armor_points / tonnage` ratio into a 5-step save ladder (`6+ / 5+ / 4+ / 3+ / 2+`).
- **Damage / AP** — collapse weapon `damage` into LI attack dice and AP modifier.
- **Wounds** — collapse `internal_structure` totals into LI wound counts (typically 1–4).

Each derivation must include:
- The chosen cut points
- The validation set used
- The hit rate against the validation set
- A list of any canonical weapons/units that landed in the "wrong" bucket and why this was accepted

## P2.4 — Co-occurrence Matrix
Optional but valuable: for the most common upgrades from P1.4, compute the co-occurrence rate with each unit tier. This tells us whether an upgrade like MASC is overwhelmingly a Light/Medium-mech feature (and so should perhaps cost less on those tiers in LI) or distributed across all weights.

---

## Acceptance Criteria

Before this plan is considered complete:

- [ ] Every `canonical_id` from `equipment_index.json` is classified into exactly one of weapons / ammunition / equipment.
- [ ] Every chassis-level upgrade in P1.4 is present and has both `affects_stat` and `binary_or_scaled` filled.
- [ ] No unit equipment reference is uncatalogued (P1.5 returns zero blocking findings).
- [ ] All P2.1 and P2.2 distribution blocks are populated for every required field (no `null` cells).
- [ ] `translation_bands.json` exists and each band has ≥ 90 % validation-set hit rate.
- [ ] `REPORT.md` summarises totals (weapons, ammo, equipment, upgrades), coverage metrics, and the proposed translation bands in a single readable view.

## Downstream Consumers
- `design/rules.prompt.md` — uses `translation_bands.json` to fix the LI stat ladders.
- `plans/card-design.prompt.md` — uses the catalogues to enumerate every special-rule pill that may appear on a card.
- `plans/game-design.prompt.md` — uses the upgrade list to confirm every chassis-altering upgrade has a matching LI rule.
