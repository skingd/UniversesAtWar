# BattleTech for Legions Imperialis — Game Design Framework

## Status
- Sections marked **[PLACEHOLDER]** are deferred to a separate rules-translation planning effort.
- Sections marked **[COMPLETE]** have finalized content.
- Distilled files are in `C:\Users\sking\OneDrive\Gaming\battletech\Data Files\distilled\`.
---

## 1. Overview & Design Goals [COMPLETE]

### Purpose
This document defines the rules framework for fielding BattleTech units in games of *Legions Imperialis*. The goal is to translate BattleTech's detailed technical simulation into LI-compatible stat blocks and special rules while preserving the distinct tactical identity of each unit class.

### Design Principles
1. **Faithful flavour** — A Clan OmniMech should feel mechanically distinct from an Inner Sphere vehicle; an assault mech should feel very different from a scout.
2. **LI compatibility** — All stats, rules, and point costs must slot cleanly into existing Legions Imperialis gameplay without requiring special tables or interrupting play flow.
3. **Era fidelity** — Unit availability is gated by era keyword; a 3025-era force cannot field Clan tech.
4. **Playability over simulation** — Where perfect accuracy conflicts with clean play, playability wins. Heat and location damage are modelled as special rules, not a parallel sub-game.
5. **Scalability** — The framework must handle 3,000+ units across four unit categories without per-unit hand-tuning.

### Scope
| Unit Category | BT Source Format | LI Unit Class Equivalent |
|---|---|---|
| BattleMech | `.json` (`mechs/`) | Titan / Walker equivalent |
| Combat Vehicle | `.yml` (`vehicles/`) | Tank / Support Vehicle |
| Aerospace Fighter | `.yml` (`aerospace/`) | Flyer / Strike Asset |
| Infantry | `.yml` (`infantry/`) | Legionary / Auxilia equivalent |

All eras from Age of War (2439+) through ilClan (3151+) are in scope.

---

## 2. Unit Categories & Tier Structure [COMPLETE]

### BattleMech Tonnage Tiers
BattleMechs are classified into four weight tiers that map to LI unit scale:

| Tier | Tonnage Range | BT Role Examples | LI Equivalent |
|---|---|---|---|
| Light | 20–35 tons | Scout, Skirmisher, Striker | Light Walker |
| Medium | 40–55 tons | Skirmisher, Brawler, Missile Boat | Standard Walker |
| Heavy | 60–75 tons | Brawler, Sniper, Skirmisher | Heavy Walker |
| Assault | 80–100 tons | Juggernaut, Sniper | Assault Walker |

### Combat Vehicle Motion Types
Vehicle mobility directly informs LI movement class:

| BT Motion Type | LI Move Class | Notes |
|---|---|---|
| Tracked | Standard | Average speed, good off-road |
| Wheeled | Fast (road only) | Penalty in rough terrain |
| Hover | Fast | Ignores water, soft terrain |
| VTOL | Flyer | Uses aerospace movement rules |
| Naval | Special | Rare; treated as barge/support |

### Aerospace Classifications
| BT Class | LI Role |
|---|---|
| Aerospace Fighter | Strike Flyer |
| Conventional Fighter | Light Flyer |
| Small Craft | Support Asset |
| DropShip | Superheavy / Off-table asset [TBD] |

### Infantry Classifications
| BT Platoon Type | LI Unit Type |
|---|---|
| Foot Infantry | Standard Infantry |
| Jump Infantry | Jump Pack Infantry |
| Motorized | Mechanised Infantry |
| Mechanised (battle armour) | Power Armour Infantry |
| Battle Armour (Clan) | Elite Power Armour |

---

## 3. Core Stats Reference [COMPLETE]

The following LI stat fields are generated for every unit card:

| Stat | Description | Source in BT Data |
|---|---|---|
| **Move** | Movement distance in LI move units | Derived from `Walk MP` / `Cruise MP` |
| **Run** | Fast-move distance (typically Move × 1.5) | Derived from `Run MP` / `Flank MP` |
| **Jump** | Jump move distance (0 if no jump) | `Jump MP` |
| **Armour** | Save roll threshold (e.g., 4+) | Derived from total `Armor Points` and tonnage |
| **Wounds** | Hit points before removal | Derived from tonnage tier |
| **Attack** | Number of attack dice | Derived from total weapon damage output |
| **AP** | Armour Penetration value | Derived from peak weapon damage/type |
| **Range** | Primary weapon range band | Derived from dominant weapon `range` |
| **Points** | LI point cost | Composite formula [PLACEHOLDER] |

---

## 4. Movement Translation [PLACEHOLDER]

> **TBD in rules-translation planning.**
>
> Key questions to resolve:
> - Exact MP-to-LI-distance conversion ratio
> - How to handle OmniMech configuration speed variance
> - Jump MP to LI Jump stat mapping
> - VTOL and aerospace movement integration
> - Infantry movement (Leg / Jump / Motorized) mapping

---

## 5. Armor & Saves Translation [PLACEHOLDER]

> **TBD in rules-translation planning.**
>
> Key questions to resolve:
> - Total armor points → save roll formula (e.g., sum of all facing armor / tonnage)
> - How to handle asymmetric facing armor (vehicles with weak rear armor)
> - Distinction between Standard, Ferro-Fibrous, and Clan Ferro armor quality
> - Whether to model internal structure as a separate wound pool or merge into Wounds

---

## 6. Wound Allocation [PLACEHOLDER]

> **TBD in rules-translation planning.**
>
> Key questions to resolve:
> - Wounds per tonnage tier (flat table vs. formula)
> - Whether vehicles and mechs use identical wound scales
> - Critical hit effects (engine, leg, arm actuator) as special rules or random table

---

## 7. Weapon Profiles [PLACEHOLDER]

> **TBD in rules-translation planning.**
>
> Available BT weapon data fields (from `weaponsandequipment/`):
> - `damage` — raw damage value
> - `heat` — heat generated per shot
> - `range` — `{minimum, short, medium, long}` in hexes
> - `ammo_per_ton` — burst/salvo indicator
> - `tech_base` — IS vs. Clan quality differentiation
>
> Key questions to resolve:
> - Damage → Attack dice formula
> - Range band (short/medium/long) → LI range category mapping
> - Heat per shot → how it feeds into the Heat special rule
> - Cluster weapons (LRM, SRM, Ultra AC) → dice count vs. flat Attack
> - Clan weapon superiority over IS equivalents

---

## 8. Special Rules Catalog [COMPLETE — stubs; values TBD]

The following special rules are defined by name and trigger. Exact mechanical effects are deferred to rules-translation planning.

### Mech-Specific Rules

| Rule Name | Trigger / Source | Effect (TBD) |
|---|---|---|
| **Heat Sink (N)** | Mech has N total heat sinks | Reduces Heat build-up from weapons |
| **Running Hot** | Heat generated > heat dissipated in a turn | Unit suffers degraded performance |
| **CASE** | Mech has CASE equipment | Ammo explosion is contained; unit survives |
| **Targeting Computer** | Mech has Targeting Computer | Bonus to attack rolls |
| **TSM (Triple Strength Myomer)** | Mech has TSM | Bonus melee attack when running hot |
| **MASC** | Mech has MASC | One-time speed boost; risk of leg damage |
| **Jump Jets** | `Jump MP` > 0 | Jump Move stat enabled |
| **ECM Suite** | Mech/vehicle has Guardian ECM | Disrupts enemy targeting within range |
| **Active Probe** | Mech has Beagle/Bloodhound/etc. | Reveals hidden units / ignores ECM |
| **Anti-Missile System** | Mech/vehicle has AMS | Reduces incoming missile attacks |

### Weapon-Derived Rules

| Rule Name | Trigger / Source | Effect (TBD) |
|---|---|---|
| **Indirect Fire** | LRM, Arrow IV | Can fire without line of sight |
| **Inferno** | Inferno SRM | Causes Heat build-up on target |
| **Streak** | Streak SRM | All shots hit; no miss roll |
| **Ultra** | Ultra Autocannon | Double rate of fire; jam risk |
| **Rotary** | Rotary AC | High rate of fire; significant jam risk |
| **LBX Cluster** | LB-X Autocannon | Cluster shot vs. single solid slug option |
| **Narc Beacon** | Narc Missile Beacon | Marks target; improves allied indirect fire |
| **TAG** | TAG laser | Guides Arrow IV / Semi-Guided LRM |
| **PPC** | All PPC types | Disrupts electronics (ECM effect) |

### Faction / Tech Rules

| Rule Name | Trigger / Source | Effect (TBD) |
|---|---|---|
| **Clan Tech** | `TechBase` = `Clan` | Better weapons / lighter equipment |
| **OmniMech** | `config` contains `Omni` | Can reconfigure weapon loadout between games |
| **XL Engine** | Mech has XL Engine | Faster but loses side torso → destroyed |
| **Light Engine** | Mech has Light Engine | Less vulnerable than XL; heavier than Standard |
| **Endo Steel** | `Structure` = `Endo Steel` | Weight savings; no game effect |
| **Ferro-Fibrous** | `Armor` = `Ferro-Fibrous` | Improves Armour save |

### Quirk-Derived Rules
Generated from `reference/quirk_names.json`. Positive quirks → beneficial special rules; negative quirks → penalties.

| BT Quirk | LI Rule Name | Effect (TBD) |
|---|---|---|
| Battle Fists | **Battle Fists** | Improved melee attack |
| Command Mech | **Command Node** | Buffs nearby friendly units |
| Easy to Pilot | **Nimble** | Re-roll failed move saves |
| Distracting | **Distracting** | Enemy units targeting this unit suffer penalty |
| Improved Communications | **Comms Array** | Extends command radius |
| Narrow/Low Profile | **Low Profile** | Improved cover save |
| Exposed Actuators | **Exposed Actuators** | Penalty; vulnerable to melee |
| *(all remaining quirks mapped in `src/translators/rules_catalog.py`)* | | |

---

## 9. Heat Mechanic [PLACEHOLDER]

> **TBD in rules-translation planning.**
>
> BattleTech's heat system (heat generated − heat dissipated = heat scale position) is the most complex mechanic to adapt. Options under consideration:
> - **Option A**: Heat as a resource — units accumulate Heat tokens each shooting phase; effects trigger at thresholds.
> - **Option B**: Heat as a special rule — mechs running hot gain a negative status; cleared at end of round.
> - **Option C**: Abstracted into weapon profile — weapons with high heat have reduced Attack dice if overused.

---

## 10. Point Cost Methodology [PLACEHOLDER]

> **TBD in rules-translation planning.**
>
> Inputs available in BT data for cost formula:
> - Tonnage tier
> - Total armor points
> - Total weapon damage output
> - Special equipment count (TSM, TC, ECM, etc.)
> - `TechBase` (Clan > IS)
> - Rules level (1 = standard; 2 = advanced; 3 = experimental)

---

## 11. Faction Keywords [COMPLETE]

Faction keywords are derived directly from `reference/factions.json`. Each unit card displays the primary manufacturer faction as a keyword.

### Major Factions
| Faction ID | Keyword | Type |
|---|---|---|
| `DC` | **Draconis Combine** | Great House |
| `FS` | **Federated Suns** | Great House |
| `FWL` | **Free Worlds League** | Great House |
| `LA` | **Lyran Alliance** | Great House |
| `CC` | **Capellan Confederation** | Great House |
| `CW` | **Clan Wolf** | Clan |
| `CJF` | **Clan Jade Falcon** | Clan |
| `CGS` | **Clan Ghost Bear** | Clan |
| `CSV` | **Clan Smoke Jaguar** | Clan |
| `CSJ` | **Clan Steel Viper** | Clan |
| `CNC` | **Clan Nova Cat** | Clan |
| `Merc` | **Mercenary** | Independent |
| `Periphery` | **Periphery** | Periphery State |

All faction IDs from `factions.json` map to a keyword. Clan units always receive the `Clan Tech` special rule.

---

## 12. Era Keywords [COMPLETE]

Era keywords are derived from `reference/eras.json`. All eras are in scope.

| Era Name | Year Range | Keyword |
|---|---|---|
| Age of War | 2439–2570 | **Age of War** |
| Star League | 2571–2780 | **Star League** |
| Early Succession Wars | 2781–2900 | **Succession Wars** |
| Late Succession Wars | 2901–3049 | **Succession Wars** |
| Clan Invasion | 3050–3061 | **Clan Invasion** |
| Civil War | 3062–3067 | **Civil War** |
| Jihad | 3068–3080 | **Jihad** |
| Dark Age | 3081–3150 | **Dark Age** |
| ilClan | 3151+ | **ilClan** |

Unit availability is enforced by `reference/equipment_availability.json` (equipment introduction years).

---

## 13. App Data Sources & Pipeline Overview [COMPLETE]

### Data Source Map

| BT Data Location | Content | Parser Module |
|---|---|---|
| `Data Files/mechs/**/*.json` | BattleMech unit files | `src/parsers/mech_parser.py` |
| `Data Files/vehicles/**/*.yml` | Combat vehicle files | `src/parsers/vehicle_parser.py` |
| `Data Files/aerospace/**/*.yml` | Aerospace unit files | `src/parsers/aerospace_parser.py` |
| `Data Files/infantry/**/*.yml` | Infantry unit files | `src/parsers/infantry_parser.py` |
| `Data Files/weaponsandequipment/**/*.json` | Weapon & equipment data | `src/parsers/weapon_parser.py` |
| `Data Files/reference/*.json` | Quirks, eras, factions | `src/parsers/reference_parser.py` |

### Pipeline Flow

```
Data Files/
    └── [Parser] → BT dataclass (BattleMech / CombatVehicle / etc.)
                       └── [Translator] → LIUnitCard dataclass
                                              └── [Renderer]
                                                    ├── markdown_renderer.py → output/cards/**/*.md
                                                    ├── image_renderer.py (Playwright) → output/cards/**/*.png
                                                    └── pdf_renderer.py (Weasyprint) → output/rules/*.pdf
```

### CLI Usage
```
python src/pipeline.py [OPTIONS]

Options:
  --unit-type     mech | vehicle | aerospace | infantry | all
  --era           3039u | 3050U | 3067 | ... | all
  --limit         N (max units per type; useful for testing)
  --format        md | png | pdf | all
  --output-dir    path to output directory (default: output/)
  --data-dir      path to BT Data Files root
```

### Python Dependencies
```
pyyaml          # YAML parsing for vehicles/aerospace/infantry
jinja2          # HTML template rendering
weasyprint      # HTML → PDF
playwright      # HTML → PNG (card images)
defusedxml      # Safe XML parsing (if needed for MWO data)
```

### Output Directory Structure
```
output/
├── rules/
│   ├── battletech-li-rules.md
│   └── battletech-li-rules.pdf
└── cards/
    ├── mechs/
    │   ├── 3039u/
    │   │   ├── Atlas_AS7-D.md
    │   │   ├── Atlas_AS7-D.png
    │   │   └── ...
    │   └── 3050U/
    ├── vehicles/
    ├── aerospace/
    └── infantry/
```
