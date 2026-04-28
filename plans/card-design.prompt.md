# BattleTech Unit Card Design System

## Status
- This document is the authoritative specification for the card rendering system.
- Visual style sections are marked **[PROVISIONAL]** pending review of reference examples in `examples/`.
- Technical sections are marked **[COMPLETE]** and ready for implementation.

---

## 1. Design Goals & Constraints [COMPLETE]

### Goals
1. **Instantly readable** — A player should be able to parse all stats within 2 seconds at arm's length.
2. **Legions Imperialis compatible** — Cards must present the same stat fields and visual language as LI unit cards so they feel native at the table.
3. **Printable** — Cards must work in both colour and greyscale printing. No information should be conveyed by colour alone.
4. **Code-generated** — All cards are produced from Jinja2 templates + Python data; no manual layout.
5. **Era/faction identity** — Each card should visually signal its faction and era at a glance.

### Physical Constraints
| Property | Value |
|---|---|
| Card size | 63 mm × 88 mm (standard poker card / LI card size) |
| Resolution for PNG export | 300 DPI minimum (744 × 1039 px at 300 DPI) |
| Bleed area | 3 mm on all sides (add to CSS `@page` size) |
| Safe area | 5 mm inset from card edge for all text/critical elements |
| Font size minimum | 7pt for secondary stats; 9pt for primary stats |

### Colour & Greyscale
All colour use must pass WCAG AA contrast (4.5:1) against both the card background and in greyscale. Faction colours are applied only to accent elements (header bar, faction badge border), not to stat text.

---

## 2. Card Anatomy [COMPLETE]

### BattleMech Card Layout (primary reference)

```
┌─────────────────────────────────┐  ← card edge (63mm)
│ ╔═══════════════════════════╗   │
│ ║  [FACTION BADGE]  [ERA]   ║   │  ← header bar (faction colour accent)
│ ║  ATLAS  •  AS7-D          ║   │
│ ╚═══════════════════════════╝   │
│                                 │
│   [UNIT SILHOUETTE / IMAGE]     │  ← image zone (optional; placeholder silhouette if absent)
│                                 │
│ ┌─────────────────────────────┐ │
│ │ MOV  RUN  JMP  ARM  WND     │ │  ← primary stat bar
│ │  6"   9"   6"  4+    3      │ │
│ └─────────────────────────────┘ │
│                                 │
│ WEAPONS                         │  ← weapons section header
│ ┌──────────────┬──┬───┬────┐   │
│ │ AC/20        │20│ 3"│ -4 │   │  ← weapon row: Name | Atk | Rng | AP
│ │ Medium Laser │ 5│12"│ -1 │   │
│ │ SRM 6        │ 6│ 9"│ -2 │   │
│ └──────────────┴──┴───┴────┘   │
│                                 │
│ SPECIAL RULES                   │  ← special rules section
│ Heat Sink (20) • CASE           │
│ Command Node • Battle Fists     │
│                                 │
│ ┌─────────────────────────────┐ │
│ │ ASSAULT MECH  •  100t  • ●●● │  ← footer: tier, tonnage, rules level dots
│ └─────────────────────────────┘ │
└─────────────────────────────────┘
```

### Zones (top to bottom)

| Zone | Height % | Content |
|---|---|---|
| Header | 18% | Faction badge, era badge, unit name, variant |
| Image | 22% | Silhouette or art; fallback to faction symbol |
| Stat Bar | 12% | Primary stats: Move, Run, Jump, Armour, Wounds |
| Weapons | 28% | Weapon table (up to 6 rows; overflow to condensed mode) |
| Special Rules | 12% | Comma-separated or pill-style rule names |
| Footer | 8% | Tier label, tonnage, tech base, rules level |

---

## 3. Design Tokens [PROVISIONAL — finalize after examples/ review]

### Typography

| Token | Value | Use |
|---|---|---|
| `--font-heading` | `"Barlow Condensed", sans-serif` | Unit name, section headers |
| `--font-body` | `"Barlow", sans-serif` | Stat values, weapon names |
| `--font-mono` | `"JetBrains Mono", monospace` | Numeric stats |
| `--font-size-unit-name` | `14pt` | Unit chassis name |
| `--font-size-variant` | `9pt` | Variant designation (AS7-D) |
| `--font-size-stat-label` | `6pt` | Stat labels (MOV, RUN, etc.) |
| `--font-size-stat-value` | `11pt` | Stat values |
| `--font-size-weapon-name` | `7.5pt` | Weapon names in table |
| `--font-size-weapon-stat` | `7pt` | Weapon numeric stats |
| `--font-size-special-rule` | `7pt` | Special rule names |
| `--font-size-footer` | `6.5pt` | Footer label text |

### Spacing Scale

| Token | Value |
|---|---|
| `--space-1` | `1mm` |
| `--space-2` | `2mm` |
| `--space-3` | `3mm` |
| `--space-4` | `4mm` |
| `--space-6` | `6mm` |

### Colours — Neutral (all card types)

| Token | Value | Use |
|---|---|---|
| `--colour-card-bg` | `#F5F0E8` | Card background (warm off-white) |
| `--colour-header-bg` | faction-specific | Header bar fill |
| `--colour-header-text` | `#FFFFFF` | Header text |
| `--colour-stat-bg` | `#2B2B2B` | Stat bar background |
| `--colour-stat-text` | `#FFFFFF` | Stat bar values |
| `--colour-stat-label` | `#AAAAAA` | Stat bar labels |
| `--colour-weapon-header` | `#3A3A3A` | Weapon table header row |
| `--colour-weapon-row-alt` | `#E8E2D4` | Alternate weapon row |
| `--colour-rule-pill-bg` | `#2B2B2B` | Special rule pill background |
| `--colour-rule-pill-text` | `#FFFFFF` | Special rule pill text |
| `--colour-footer-bg` | `#1A1A1A` | Footer background |
| `--colour-footer-text` | `#CCCCCC` | Footer text |
| `--colour-border` | `#2B2B2B` | Card border, section dividers |

### Faction Accent Colours [PROVISIONAL]

| Faction | `--colour-header-bg` | Notes |
|---|---|---|
| Draconis Combine | `#8B0000` | Deep red |
| Federated Suns | `#B8860B` | Dark goldenrod |
| Lyran Alliance | `#1C3A6B` | Royal blue |
| Capellan Confederation | `#1A5C1A` | Dark green |
| Free Worlds League | `#6B2FA0` | Purple |
| Clan (all) | `#1A3A1A` | Dark forest green |
| Mercenary | `#4A4A4A` | Charcoal |
| Periphery / Unknown | `#3A2A1A` | Dark brown |

### Rules Level Indicator
Rules level (from BT `Rules Level` field) is displayed as filled dots in the footer:

| Rules Level | Display | Meaning |
|---|---|---|
| 1 | `●○○` | Tournament standard (Total Warfare) |
| 2 | `●●○` | Advanced rules |
| 3 | `●●●` | Experimental / Apocryphal |

---

## 4. Card Variants by Unit Type [COMPLETE]

All four unit types use the same zone structure. Differences are:

### BattleMech
- Header: Chassis + Variant designation + Tonnage tier badge
- Image zone: Mech silhouette (by tonnage class)
- Stat bar: Move, Run, Jump, Armour, Wounds
- Weapons: Full weapon table
- Special rules: Quirks + equipment-derived rules
- Footer: Tier (Light/Medium/Heavy/Assault), tonnage, tech base, rules level

### Combat Vehicle
- Header: Vehicle name + Motion Type badge (Tracked/Hover/VTOL/etc.)
- Image zone: Vehicle silhouette
- Stat bar: Move, Run, Armour, Wounds, Facing (Front/Side/Rear save differences if significant)
- Weapons: Weapon table (organized by firing arc: Front/Turret/Rear)
- Special rules: Motion-type rules + equipment rules
- Footer: Vehicle class (Light/Medium/Heavy/Assault), tonnage, motion type

### Aerospace Fighter
- Header: Fighter name + variant + Safe Thrust
- Image zone: Fighter silhouette
- Stat bar: Thrust, Armour, Wounds, Structural Integrity
- Weapons: Weapon table (Nose/Wing/Aft arcs)
- Special rules: Aerospace-specific rules
- Footer: Fighter class, tonnage, tech base

### Infantry
- Header: Platoon designation + Motion Type
- Image zone: Infantry icon / faction emblem
- Stat bar: Move, Armour, Wounds, Squad Size, Squad Count
- Weapons: Primary weapon + secondary if present
- Special rules: Anti-Mek, Jump, Motorized, Battle Armour rules as applicable
- Footer: Platoon type, total trooper count, tech base

---

## 5. Weapon Table Layout [COMPLETE]

### Columns

| Column | Width | Alignment | Content |
|---|---|---|---|
| Name | ~50% | Left | Weapon name (abbreviated if >20 chars) |
| Atk | ~15% | Center | Attack dice count |
| Rng | ~20% | Center | Range (e.g., `12"`) |
| AP | ~15% | Center | Armour Penetration (e.g., `-2`) |

### Overflow Handling
- Up to 4 weapons: normal row height (7.5pt text, 4mm row height)
- 5–6 weapons: condensed rows (6.5pt text, 3.5mm row height)
- 7+ weapons: split into two columns side by side (3.5pt minimum; flag for review)
- Omni-configured units (OmniMechs): show primary configuration only; note "OmniMech — alt configs available" in special rules

### Heat Column (optional)
If the Heat mechanic is finalized, a 5th column `Heat` is added between `Atk` and `Rng`. The column is present only if any weapon on the card generates heat > 0.

---

## 6. Special Rules Block [COMPLETE]

### Layout
Special rules are displayed as inline pill-style badges:

```
┌──────────────────┐  ┌───────┐  ┌──────────┐
│ Heat Sink (20)   │  │ CASE  │  │ ECM Suite│
└──────────────────┘  └───────┘  └──────────┘
```

- Each rule name is a dark pill (`--colour-rule-pill-bg` background, white text)
- Rules wrap to a second line if needed
- Maximum 3 lines; if more rules exist, overflow to "… +N rules" indicator
- Rules are sorted: mech-structural rules first, then weapon-derived, then quirk-derived

### Rule Name Abbreviation
Long rule names are abbreviated on the card. The full name appears in the rules document.

| Full Name | Card Abbreviation |
|---|---|
| Heat Sink (N) | `HS(N)` |
| Triple Strength Myomer | `TSM` |
| Anti-Missile System | `AMS` |
| Targeting Computer | `TC` |
| Guardian ECM Suite | `ECM` |

---

## 7. Faction & Era Badge [COMPLETE]

### Faction Badge
Located in the top-left of the header bar.

- Contains: faction abbreviation (2–4 chars) in a bordered box
- Border colour: faction accent colour
- Background: transparent (shows header bar colour through)
- Example: `[ DC ]` for Draconis Combine

### Era Badge
Located in the top-right of the header bar.

- Contains: era year (e.g., `3039`) or era name abbreviation
- Style: small caps, no border, muted against header
- Example: `SW` (Succession Wars), `CI` (Clan Invasion), `DA` (Dark Age)

---

## 8. CSS Architecture [COMPLETE]

### File Structure

```
templates/
├── cards/
│   ├── base_card.css              ← design tokens, reset, shared layout
│   ├── mech_card.html.j2          ← BattleMech card template
│   ├── vehicle_card.html.j2       ← Combat vehicle card template
│   ├── aerospace_card.html.j2     ← Aerospace fighter card template
│   ├── infantry_card.html.j2      ← Infantry platoon card template
│   └── card_components.html.j2    ← Reusable macros/partials
└── rules/
    ├── rules.css                  ← Print-optimized rules document CSS
    ├── rules_document.html.j2     ← Full rules document template
    └── unit_entry.html.j2         ← Per-unit entry partial
```

### CSS Naming Convention
BEM-style class names scoped to card components:

```
.card                     ← root card element
.card__header             ← header zone
.card__header--mech       ← unit-type modifier
.card__faction-badge      ← faction badge element
.card__era-badge          ← era badge element
.card__unit-name          ← chassis name
.card__variant            ← variant designation
.card__image-zone         ← image container
.card__stat-bar           ← primary stats strip
.card__stat               ← individual stat cell
.card__stat-label         ← stat abbreviation label
.card__stat-value         ← stat numeric value
.card__weapons            ← weapons section
.card__weapon-table       ← weapon table element
.card__weapon-row         ← individual weapon row
.card__weapon-row--alt    ← alternate row background
.card__special-rules      ← special rules section
.card__rule-pill          ← individual rule pill
.card__footer             ← footer zone
```

### CSS Custom Properties (defined in `base_card.css`)
All design tokens from Section 3 are defined as CSS custom properties on `:root`. Card type variants override only the faction-specific token (`--colour-header-bg`) via a data attribute:

```css
[data-faction="DC"]  { --colour-header-bg: #8B0000; }
[data-faction="FS"]  { --colour-header-bg: #B8860B; }
[data-faction="LA"]  { --colour-header-bg: #1C3A6B; }
/* etc. */
```

---

## 9. Jinja2 Template Structure [COMPLETE]

### `card_components.html.j2` — Shared Macros

```jinja
{% macro stat_bar(unit) %}              ← renders the primary stats strip
{% macro weapon_table(weapons) %}       ← renders the weapon table
{% macro special_rules(rules) %}        ← renders rule pills
{% macro faction_badge(faction_id) %}   ← renders faction badge
{% macro era_badge(era) %}              ← renders era badge
{% macro footer_bar(unit) %}            ← renders card footer
```

### `mech_card.html.j2` — BattleMech Card

```jinja
{% from "card_components.html.j2" import stat_bar, weapon_table, special_rules, faction_badge, era_badge, footer_bar %}
<html>
<head>
  <link rel="stylesheet" href="base_card.css">
  <style>
    /* card-size constraints for this render target */
    .card { width: 63mm; height: 88mm; }
  </style>
</head>
<body>
  <div class="card card--mech" data-faction="{{ unit.faction_id }}">
    <div class="card__header">
      {{ faction_badge(unit.faction_id) }}
      <span class="card__unit-name">{{ unit.chassis }}</span>
      <span class="card__variant">{{ unit.model }}</span>
      {{ era_badge(unit.era) }}
    </div>
    <div class="card__image-zone">
      <!-- silhouette image based on tonnage class -->
    </div>
    {{ stat_bar(unit) }}
    <div class="card__weapons">
      <h3 class="card__section-header">WEAPONS</h3>
      {{ weapon_table(unit.weapons) }}
    </div>
    <div class="card__special-rules">
      <h3 class="card__section-header">SPECIAL RULES</h3>
      {{ special_rules(unit.special_rules) }}
    </div>
    {{ footer_bar(unit) }}
  </div>
</body>
</html>
```

Vehicle, aerospace, and infantry templates follow the same macro-import pattern with unit-type-specific fields substituted.

### Template Data Contract
Each template receives an `LIUnitCard` object with these fields:

```python
@dataclass
class LIUnitCard:
    # Identity
    name: str                   # e.g., "Atlas AS7-D"
    chassis: str                # e.g., "Atlas"
    model: str                  # e.g., "AS7-D"
    unit_type: str              # "mech" | "vehicle" | "aerospace" | "infantry"
    faction_id: str             # e.g., "DC"
    era: str                    # e.g., "3039u"
    era_year: int               # e.g., 3039
    tonnage: int                # e.g., 100
    tech_base: str              # "Inner Sphere" | "Clan" | "Mixed"
    rules_level: int            # 1 | 2 | 3

    # LI Stats
    move: str                   # e.g., '6"'
    run: str                    # e.g., '9"'
    jump: str | None            # e.g., '6"' or None
    armour_save: str            # e.g., "4+"
    wounds: int                 # e.g., 3

    # Weapons
    weapons: list[LIWeaponProfile]

    # Special Rules
    special_rules: list[str]    # e.g., ["Heat Sink (20)", "CASE", "Command Node"]

    # Metadata
    tier: str                   # "Light" | "Medium" | "Heavy" | "Assault"
    points: int | None          # None until point cost formula is finalized
    source_file: str            # path to originating BT data file

@dataclass
class LIWeaponProfile:
    name: str                   # e.g., "AC/20"
    attack: int                 # attack dice
    range_inches: int           # primary range in LI inches
    ap: int                     # armour penetration (negative = better)
    heat: int | None            # heat generated (None if heat mechanic not active)
```

---

## 10. Rendering Pipeline [COMPLETE]

### PNG Card Images (Playwright)

```bash
# Install dependencies
pip install playwright jinja2
playwright install chromium

# Usage (via pipeline.py)
python src/pipeline.py --unit-type mech --era 3039u --format png
```

**Playwright renderer logic (`src/renderers/image_renderer.py`):**
1. Render Jinja2 template to HTML string
2. Launch headless Chromium via Playwright
3. Set viewport to card dimensions (744 × 1039 px @ 300 DPI equivalent)
4. Load HTML
5. Screenshot to PNG at specified path

**Key Playwright settings:**
```python
page.set_viewport_size({"width": 744, "height": 1039})
page.emulate_media(media="print")
page.screenshot(path=output_path, full_page=False)
```

### PDF Rules Document (Weasyprint)

```bash
# Install
pip install weasyprint jinja2

# Usage
python src/pipeline.py --unit-type all --format pdf
```

**Weasyprint renderer logic (`src/renderers/pdf_renderer.py`):**
1. Render Jinja2 `rules_document.html.j2` to HTML string (iterates all translated units)
2. Pass HTML string to `weasyprint.HTML(string=...).write_pdf(output_path)`
3. CSS `@media print` rules handle page breaks between unit entries

**Print CSS key rules (`templates/rules/rules.css`):**
```css
@page {
  size: A4;
  margin: 15mm 12mm;
}

.unit-entry {
  page-break-inside: avoid;
}

.chapter-heading {
  page-break-before: always;
}
```

### Markdown Output

Both card `.md` files and the rules `.md` file are rendered by `src/renderers/markdown_renderer.py` using a plain-text Jinja2 template (no HTML). The markdown card format is a simple table + bullet list layout for readability in GitHub / Obsidian.

---

## 11. Output File Naming Conventions [COMPLETE]

### Card Files
Pattern: `output/cards/{unit_type}/{era}/{chassis}_{model}.{ext}`

- Spaces replaced with underscores
- Special characters stripped (e.g., `/` in tonnage class removed)
- All lowercase

Examples:
```
output/cards/mechs/3039u/atlas_as7-d.png
output/cards/mechs/3039u/atlas_as7-d.md
output/cards/vehicles/3050u/manticore_heavy_tank.png
output/cards/infantry/tw/foot_platoon_laser.png
```

### Rules Document
```
output/rules/battletech-legions-imperialis-rules.pdf
output/rules/battletech-legions-imperialis-rules.md
```

---

## 12. Accessibility & Print Considerations [COMPLETE]

### Greyscale Fallback
All faction colours must map to distinct grey values. Minimum separation: 20% luminance difference between adjacent accent colours. Verify using CSS `filter: grayscale(1)` in browser before finalising palette.

### Font Embedding
Weasyprint and Playwright both embed fonts in output. Use Google Fonts or system fonts only; avoid proprietary fonts that cannot be embedded. Barlow (Google Font) is freely licensed (OFL).

### Print Resolution
- PNG export at 300 DPI minimum for physical card printing
- PDF export uses vector CSS rendering (Weasyprint); no rasterization of text

### Overflow Safety
All zones have `overflow: hidden` in CSS. If content overflows (e.g., too many weapons), the renderer logs a warning with the unit name. The card is still written but flagged for manual review in a `output/overflow_report.txt` file.

### Colour-Blind Safety
Avoid relying solely on red/green distinction. Faction colours that are adjacent in the table should differ in hue and luminance. Rules level dots use filled (●) vs empty (○) distinction (shape, not colour).
