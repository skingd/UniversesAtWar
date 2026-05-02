# BattleTech Data Check Report

STATUS: PASS

**Total issues:** 148 error / 6023 warning

## Blocking issues
_(none)_

---

## 1. Inventory

| Unit Type | Count |
|---|---|
| mech | 4219 |
| vehicle | 1447 |
| aerospace | 572 |
| infantry | 1393 |

| Weapon Category | Count |
|---|---|
| ammunition | 1 |
| ballistic | 52 |
| energy | 55 |
| missile | 57 |
| physical | 11 |
| infantry | 1 |
| equipment | 65 |

- **Reference files:** 34
- **Parse failures:** 0

## 2. Canonical Indices Built

- equipment_index.json — **778** records (incl. **537** synthesized from unit references)
- equipment_aliases.json — **3117** alias keys
- reference_index.json — 34 reference files indexed
- mech_index.json / vehicle_index.json / aerospace_index.json / infantry_index.json built

## 3. Equipment Reference Resolution

| Outcome | Count |
|---|---|
| Total references | 180388 |
| Exact match | 7688 |
| Tech-disambiguated match | 36985 |
| Structural (skipped) | 135691 |
| **Unresolved** | **24** |

**Resolution rate (excluding structural):** 99.946%
**Overall unresolved percentage:** 0.054%
**Gated unresolved % (gate types: mech,vehicle,aerospace):** **0.056%**

### Per unit type

| Unit Type | Total Refs | Structural | Resolved | Unresolved | Resolution Rate | Unresolved % |
|---|---|---|---|---|---|---|
| aerospace ✓ | 2741 | 5 | 2735 | 1 | 99.963% | 0.037% |
| infantry | 2041 | 0 | 2041 | 0 | 100.0% | 0.0% |
| mech ✓ | 170301 | 135653 | 34648 | 0 | 100.0% | 0.0% |
| vehicle ✓ | 5305 | 33 | 5249 | 23 | 99.564% | 0.436% |

_✓ = counted toward FAIL gate_

### Top 20 unresolved references

| Reference | Frequency |
|---|---|
| `CLLargeChemLaserAmmo` | 9 |
| `ISLongTomAmmo` | 8 |
| `ISCruiseMissile50Ammo` | 2 |
| `ISArmorPiercingMortarAmmo1` | 1 |
| `ClanImprovedLRM10Ammo` | 1 |
| `CLImpAmmoSRM6` | 1 |
| `CLLargeChemLaserAmmo:OMNI` | 1 |
| `ClanImprovedLRM20Ammo` | 1 |

## 4. Quirks
- Total: 8548
- Unknown quirks: 1099

## 5. Era Coverage
- Units with year field: 7599
- Years outside known era spans: 2194

## 6. Ammo → Weapon Linkage
- Matched: 0
- Unmatched (orphan ammo): 0

## 7. Required Fields

| Category | Files Checked | Missing Field Issues |
|---|---|---|
| mech | 4219 | 133 |
| vehicle | 1447 | 11 |
| aerospace | 572 | 0 |
| infantry | 1393 | 0 |
| equipment | 778 | 4 |

## 8. Range Validation
- Numeric / range violations: 49

## 9. Duplicates
- mech_duplicate_keys: 9
- vehicle_duplicate_keys: 3
- aerospace_duplicate_keys: 3
- infantry_duplicate_keys: 149
- equipment_duplicate_numeric_ids: 0

## 10. Orphan Equipment (informational)
- Equipment never referenced by any unit: **107**

---

See `output/data-check/` for per-issue CSVs and `issues.jsonl` for the full machine-readable issue stream.
