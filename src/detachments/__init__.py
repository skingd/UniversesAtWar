"""`uaw-detachments` — first-pass detachment profile JSON pipeline.

Consumes `data/index/*` records, applies the translations defined in
`design/units-translation.md`, joins per-weapon profiles from
`data/WeaponRules.csv`, and emits per-unit-type detachment JSON for
the future graphical card generator.
"""
