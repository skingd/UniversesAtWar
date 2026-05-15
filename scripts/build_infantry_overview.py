"""Generate a markdown overview of infantry data for the design folder.

Reads infantry_overview.json (produced by scan_infantry.py) and
battlearmor_overview.json (produced by scan_battlearmor.py) and writes
design/infantryandbattlearmor.md.
"""
import json, collections, pathlib, textwrap

OVERVIEW = pathlib.Path("infantry_overview.json")
BA_OVERVIEW = pathlib.Path("battlearmor_overview.json")
OUT = pathlib.Path("design/infantryandbattlearmor.md")

d = json.loads(OVERVIEW.read_text())
ba = json.loads(BA_OVERVIEW.read_text()) if BA_OVERVIEW.exists() else None

def fmt_table(rows, headers):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)

# Group squad summaries by chassis to keep tables readable.
def group_chassis(units):
    g = collections.defaultdict(list)
    for u in units:
        g[u["chassis"]].append(u)
    return g

def chassis_rows(units):
    grouped = group_chassis(units)
    rows = []
    for chassis, variants in sorted(grouped.items()):
        u = variants[0]
        p = u.get("platoon", {}) or {}
        squad = f'{p.get("Squad Size","?")}x{p.get("Squad Count","?")}={p.get("Total Troopers","?")}'
        weapons = u.get("primary") or "-"
        if u.get("secondary"):
            weapons += f' / {u["secondary"]}'
        if u.get("field_guns"):
            fgs = sorted({fg for fg in u["field_guns"] if not fg.endswith(" Ammo")})
            if fgs:
                weapons += f' (Field: {", ".join(fgs)})'
        rows.append([
            chassis,
            len(variants),
            u.get("motion") or "-",
            squad,
            u.get("armor_kit") or "-",
            weapons,
        ])
    return rows

# Build the markdown.
parts = []
parts.append("# Infantry & Battle Armor Overview")
parts.append("")
ba_total = ba['totals']['files'] if ba else 0
parts.append(f"_Generated from MegaMek source data ({d['totals']['files']} conventional infantry units, {ba_total} battle armor units)._")
parts.append("")
parts.append("## Scope")
parts.append("")
parts.append(textwrap.dedent("""\
    This document captures everything currently available in the project's
    `infantry` source corpus and the upstream MegaMek `battlearmor` corpus
    so the next two website sections (**Infantry** and **Battle Armor**)
    can be designed from a single source of truth.

    > **Battle Armor source:** the BA `.blk` files are sourced from the
    > upstream `MegaMek/mm-data` repository under
    > `data/mekfiles/battlearmor/` (sparse-cloned to `.cache/mm-data/`,
    > which is git-ignored). To refresh the dataset, run
    > `git -C .cache/mm-data pull` and re-run
    > `scripts/scan_battlearmor.py` followed by
    > `scripts/build_infantry_overview.py`.
    """))

# --- Platoon / Squad sizing --------------------------------------------------
parts.append("## Platoon / Squad Sizes")
parts.append("")
rows = []
for label, group in [("Clan", "Clan"), ("Inner Sphere", "IS")]:
    pr = d["platoon_ranges"][group]
    rows.append([
        label,
        f'{pr["Squad Size"]["min"]}–{pr["Squad Size"]["max"]}',
        f'{pr["Squad Count"]["min"]}–{pr["Squad Count"]["max"]}',
        f'{pr["Total Troopers"]["min"]}–{pr["Total Troopers"]["max"]}',
        (f'{pr["Secondary Weapons per Squad"]["min"]}–{pr["Secondary Weapons per Squad"]["max"]} '
         f'({pr["Secondary Weapons per Squad"]["n"]}/{pr["Squad Size"]["n"]} units)'),
    ])
parts.append(fmt_table(rows, ["Tech Base", "Squad Size", "Squad Count",
                              "Total Troopers", "Secondary Wpns / Squad"]))
parts.append("")

# --- Movement ---------------------------------------------------------------
parts.append("## Movement Scale")
parts.append("")
parts.append("MegaMek records a `Motion Type` per platoon; `movement_points` (MP) "
             "in the project's `infantry_index.json` is the per-turn move from "
             "*Total Warfare* p.149. Translation suggestion: 1 MP = 2\" at the "
             "Legions Imperialis scale used elsewhere in this project.")
parts.append("")
parts.append(fmt_table(
    [["Foot (Leg)", 1, "Slowest, all tech bases"],
     ["Jump",       1, "Same MP as Foot but ignores terrain costs"],
     ["Tracked",    2, "Most common Clan & IS heavy support"],
     ["Wheeled",    3, "Faster ground"],
     ["Motorized",  3, "Trucks / jeeps"],
     ["Hover",      5, "Hovercraft platoons"],
     ["VTOL",       6, "Single example in dataset"],
     ["Submarine",  2, "Naval / SCUBA"],
     ["Beast:*",    1, "Cavalry / pack mounts (10 distinct mounts, IS only)"]],
    ["Motion Type", "Typical MP", "Notes"]))
parts.append("")

# --- Tech base totals -------------------------------------------------------
parts.append("## Tech Base Totals")
parts.append("")
parts.append(fmt_table(
    [["Clan",         d["totals"]["Clan"]],
     ["Inner Sphere", d["totals"]["IS"]],
     ["**Total**",    d["totals"]["files"]]],
    ["Tech Base", "Units"]))
parts.append("")

# --- Roles ------------------------------------------------------------------
parts.append("## Roles (Special Rule Hooks)")
parts.append("")
parts.append("These map directly onto the role-based traits already in use on")
parts.append("vehicle / mech detachments and should drive trait assignments.")
parts.append("")
for label, key in [("Clan", "roles_clan"), ("Inner Sphere", "roles_is")]:
    parts.append(f"**{label}**")
    parts.append("")
    rows = [[r, n] for r, n in d[key]]
    parts.append(fmt_table(rows, ["Role", "Count"]))
    parts.append("")

# --- Armor kits / equipment -------------------------------------------------
parts.append("## Armor Kits / Equipment")
parts.append("")
parts.append("Each platoon carries one armor kit; this is the closest analogue")
parts.append("in the source data to a per-detachment equipment list.")
parts.append("")
for label, key in [("Clan", "armor_kits_clan"), ("Inner Sphere", "armor_kits_is")]:
    parts.append(f"**{label}**")
    parts.append("")
    rows = [[k or "(none)", n] for k, n in d[key]]
    parts.append(fmt_table(rows, ["Armor Kit", "Count"]))
    parts.append("")

# --- Field Guns -------------------------------------------------------------
parts.append("## Field Guns (Equipment Mounts)")
parts.append("")
parts.append(f"{len(d['field_guns_seen'])} distinct field-gun entries (incl. ammo lines). "
             "These are full-scale weapons crewed by infantry — they should map to "
             "existing `WeaponRules.csv` rows, not to `InfantryWeaponRules.csv`.")
parts.append("")
fg_clean = sorted({g for g in d["field_guns_seen"] if not g.endswith("Ammo")})
parts.append("<details><summary>Field gun list (deduped, ammo lines removed)</summary>")
parts.append("")
for g in fg_clean:
    parts.append(f"- `{g}`")
parts.append("")
parts.append("</details>")
parts.append("")

# --- BV scale ---------------------------------------------------------------
parts.append("## BV Scale (Pricing)")
parts.append("")
parts.append(textwrap.dedent("""\
    The infantry source `.yml` files **do not carry a Battle Value field** —
    BV must be sourced from the MUL (Master Unit List) lookup keyed by
    `mul id`, the same way it's done for mechs / vehicles elsewhere.

    Working assumption for the points scale on the website (consistent with
    existing detachments):

    | Tech Base | BV Range (per-platoon, observed) | Recommended LI Points |
    |---|---|---|
    | Inner Sphere conventional infantry | ~30 – 200 BV | round(BV / 10) |
    | Clan conventional infantry         | ~50 – 280 BV | round(BV / 10) |
    | Battle Armor (when added)          | ~100 – 600 BV | round(BV / 10) |

    These ranges should be re-validated once the MUL lookup is wired in;
    the conversion ratio above mirrors what the mech / vehicle pages use.
    """))

# --- Weapons in WeaponRules.csv shape --------------------------------------
parts.append("## Infantry Weapons → `data/InfantryWeaponRules.csv`")
parts.append("")
parts.append(textwrap.dedent("""\
    `data/InfantryWeaponRules.csv` does not exist yet. It should follow the
    exact column layout of `data/WeaponRules.csv`:

    ```
    Weapon Name,Range,Heat,Dice,To-Hit,AP,Type,Traits
    ```

    The unique weapon names referenced by the corpus, grouped by tech base,
    are listed below — these are the rows that need filling in (ranges /
    dice / AP / traits to be derived from *Total Warfare* p.215–219 and
    *Tactical Operations* infantry weapons tables).
    """))

for label, key in [("Clan", "weapons_clan"), ("Inner Sphere", "weapons_is")]:
    parts.append(f"### {label} ({len(d[key])} unique weapons)")
    parts.append("")
    parts.append(fmt_table(
        [[w, n] for w, n in d[key]],
        ["Weapon Name", "Used By N Platoons"]))
    parts.append("")

# --- Squads / chassis listing ----------------------------------------------
parts.append("## Squads (chassis × variants × loadout)")
parts.append("")
parts.append("Grouped by chassis to keep the table readable; the **Variants**")
parts.append("column counts the number of platoon models sharing that chassis.")
parts.append("")
for label, key in [("Clan", "squads_clan"), ("Inner Sphere", "squads_is")]:
    parts.append(f"### {label} chassis")
    parts.append("")
    rows = chassis_rows(d[key])
    parts.append(fmt_table(rows,
        ["Chassis", "Variants", "Motion", "Squad x Count = Total",
         "Armor Kit", "Weapons (P / S / Field)"]))
    parts.append("")

# --- Special rules / traits TODO list --------------------------------------
parts.append("## Special Rules / Traits (Site Glossary Hooks)")
parts.append("")
parts.append(textwrap.dedent("""\
    The infantry source data has no explicit `quirks` or `augmentations`
    blocks populated, so the special rules surface for these detachments
    must be derived from:

    1. **Role** — drives the headline trait (e.g. *Ambusher* → Stealth /
       *Sniper* → Marksman / *Scout* → Infiltrator).
    2. **Motion Type** — determines movement keywords
       (Jump → *Jump Pack*, Beast:* → *Cavalry*, Hover → *Fast*).
    3. **Armor Kit** — determines defensive traits
       (Sneak Suit → *Stealth*, Environment Suit → *Sealed*,
        DEST Infiltration Suit → *Infiltrator + Stealth*,
        Ballistic Plate / Flak → *Armoured (3+)*).
    4. **Primary Weapon traits** — pulled from the new
       `InfantryWeaponRules.csv` once authored.

    These should each become a `data-rule="…"` glossary entry so the
    existing tooltip system already in `app.js` lights them up everywhere
    they appear.
    """))

# ---------------------------------------------------------------------------
# BATTLE ARMOR section
# ---------------------------------------------------------------------------
if ba:
    parts.append("---")
    parts.append("")
    parts.append("# Battle Armor")
    parts.append("")
    parts.append(f"_Sourced from `MegaMek/mm-data` `data/mekfiles/battlearmor/` ({ba['totals']['files']} `.blk` files)._")
    parts.append("")

    # Tech base totals
    parts.append("## BA Tech Base Totals")
    parts.append("")
    parts.append(fmt_table(
        [["Clan", ba['totals']['Clan']],
         ["Inner Sphere", ba['totals']['IS']],
         ["**Total**", ba['totals']['files']]],
        ["Tech Base", "Units"]))
    parts.append("")

    # Squad / Point sizes
    parts.append("## BA Squad / Point Sizes")
    parts.append("")
    parts.append("Inner Sphere fields **Squads** (typically 4 troopers); Clan fields **Points** (5 troopers). The dataset shows:")
    parts.append("")
    rows = []
    for label, key in [("Clan", "Clan"), ("Inner Sphere", "IS")]:
        pr = ba["platoon_ranges"][key]
        tc = pr["Trooper Count"]
        rows.append([label, f'{tc["min"]}\u2013{tc["max"]}', tc["n"]])
    parts.append(fmt_table(rows, ["Tech Base", "Trooper Count Range", "# Units"]))
    parts.append("")

    # Movement
    parts.append("## BA Movement Scale")
    parts.append("")
    parts.append("BA `motion_type` corresponds to ground (`Leg`), jump-jet (`Jump`), VTOL (`Jump booster + rotors`), and underwater (`UMU`).")
    parts.append("")
    for label, key in [("Clan", "motion_clan"), ("Inner Sphere", "motion_is")]:
        parts.append(f"**{label}**")
        parts.append("")
        parts.append(fmt_table([[m, n] for m, n in ba[key]], ["Motion", "Count"]))
        parts.append("")
    parts.append("MP ranges by tech base (`cruiseMP` = walking, `jumpingMP` = jump or UMU):")
    parts.append("")
    rows = []
    for label, key in [("Clan", "Clan"), ("Inner Sphere", "IS")]:
        pr = ba["platoon_ranges"][key]
        c = pr["cruiseMP"]; j = pr["jumpingMP"]
        rows.append([label, f'{c["min"]}\u2013{c["max"]}', f'{j["min"]}\u2013{j["max"]}'])
    parts.append(fmt_table(rows, ["Tech Base", "Walk MP", "Jump / UMU MP"]))
    parts.append("")

    # Weight classes
    parts.append("## BA Weight Classes")
    parts.append("")
    parts.append("Weight class drives armour, manipulator options, and movement floor (per *Tactical Operations* p.318).")
    parts.append("")
    for label, key in [("Clan", "weightclass_clan"), ("Inner Sphere", "weightclass_is")]:
        parts.append(f"**{label}**")
        parts.append("")
        parts.append(fmt_table([[wc, n] for wc, n in ba[key]], ["Weight Class", "Count"]))
        parts.append("")

    # Roles
    parts.append("## BA Roles (Special Rule Hooks)")
    parts.append("")
    for label, key in [("Clan", "roles_clan"), ("Inner Sphere", "roles_is")]:
        parts.append(f"**{label}**")
        parts.append("")
        parts.append(fmt_table([[r, n] for r, n in ba[key]], ["Role", "Count"]))
        parts.append("")

    # Weapons -> CSV recommendation
    parts.append("## BA Weapons \u2192 `data/BattleArmorWeaponRules.csv`")
    parts.append("")
    parts.append(textwrap.dedent("""\
        Battle armor weapons mount differently from conventional infantry
        weapons (per-trooper, with `:Location` slots such as `LA`, `RA`,
        `Body`, `APM`). They warrant their own CSV mirroring the columns
        in `data/WeaponRules.csv`:

        ```
        Weapon Name,Range,Heat,Dice,To-Hit,AP,Type,Traits
        ```

        Names prefixed `BA*`, `CLBA*`, `ISBA*` are BA-specific mounts;
        names like `InfantryAssaultRifle` carried by BA represent
        anti-personnel hand weapons mounted via `BAAPMount` (`:APM`).
        """))
    for label, key in [("Clan", "weapons_clan"), ("Inner Sphere", "weapons_is")]:
        parts.append(f"### {label} BA Weapons ({len(ba[key])} unique)")
        parts.append("")
        parts.append("<details><summary>Weapon list</summary>")
        parts.append("")
        parts.append(fmt_table([[w, n] for w, n in ba[key]],
                               ["Weapon Name", "Used By N Units"]))
        parts.append("")
        parts.append("</details>")
        parts.append("")

    # Gear / equipment
    parts.append("## BA Equipment, Manipulators & Armour Mods")
    parts.append("")
    parts.append(textwrap.dedent("""\
        Non-weapon equipment maps to **Special Rules / Traits** rather than
        weapon rows. Common categories:

        - **Manipulators** (`BABasicManipulator`, `BABattleClaw`,
          `BAArmoredGlove`, `BASalvageArm`, `*MineClearance`,
          `*Vibro`) \u2192 grants `Anti-'Mech` attack capability and
          field-repair traits.
        - **Armour mods** (`*Stealth (Basic/Standard/Improved)`, `*Mimetic`,
          `*Reflective`, `*Reactive`, `*Fire Resistant`) \u2192 defensive
          traits (Stealth, Cover, Resistant: Energy / Ballistic / Fire).
        - **Mounts** (`BAAPMount`) \u2192 lets a trooper carry an
          anti-personnel hand weapon.
        - **Mobility** (`BAJumpJet`, `BAJumpBooster`, `BAVTOL`, `BAUMU`,
          `BAPartialWing`, `BAMyomerBooster`) \u2192 movement keywords.
        - **Utility** (`BASearchlight`, `BACuttingTorch`, `BARemoteSensor`,
          `BAMagneticClamp`, `BAParaFoil`, `BACargo`,
          `BAMineDispenser`) \u2192 special action hooks.
        """))
    for label, key in [("Clan", "gear_clan"), ("Inner Sphere", "gear_is")]:
        parts.append(f"### {label} BA Equipment ({len(ba[key])} unique)")
        parts.append("")
        parts.append("<details><summary>Equipment list</summary>")
        parts.append("")
        parts.append(fmt_table([[g, n] for g, n in ba[key]],
                               ["Equipment", "Used By N Units"]))
        parts.append("")
        parts.append("</details>")
        parts.append("")

    # Squad loadout sample - group by name (chassis-equivalent)
    parts.append("## BA Chassis (sample loadouts)")
    parts.append("")
    parts.append("Grouped by `Name` (chassis); the **Variants** column counts how many `Model` entries share that chassis.")
    parts.append("")
    def ba_chassis_rows(units):
        g = collections.defaultdict(list)
        for u in units:
            g[u["name"] or "(unnamed)"].append(u)
        rows = []
        for chassis, variants in sorted(g.items()):
            u = variants[0]
            wpns = ", ".join(u["weapons"][:4]) or "-"
            if len(u["weapons"]) > 4:
                wpns += f" \u2026 (+{len(u['weapons'])-4} more)"
            gear = ", ".join(u["gear"][:3]) or "-"
            if len(u["gear"]) > 3:
                gear += f" \u2026 (+{len(u['gear'])-3} more)"
            rows.append([
                chassis,
                len(variants),
                u.get("motion") or "-",
                f'{u.get("trooper_count","?")}',
                f'{u.get("cruise_mp","?")}/{u.get("jump_mp","?")}',
                u.get("role") or "-",
                wpns,
                gear,
            ])
        return rows
    for label, key in [("Clan", "squads_clan"), ("Inner Sphere", "squads_is")]:
        parts.append(f"### {label} BA chassis")
        parts.append("")
        parts.append("<details><summary>Full chassis table</summary>")
        parts.append("")
        parts.append(fmt_table(ba_chassis_rows(ba[key]),
            ["Chassis", "Variants", "Motion", "Troopers", "Walk/Jump MP",
             "Role", "Weapons", "Gear"]))
        parts.append("")
        parts.append("</details>")
        parts.append("")

    # Special rules / traits hooks for BA
    parts.append("## BA Special Rules / Traits (Site Glossary Hooks)")
    parts.append("")
    parts.append(textwrap.dedent("""\
        BA traits should hang off the same `data-rule="\u2026"` glossary
        plumbing already used elsewhere. Suggested derivations:

        1. **Role** \u2192 headline trait (Ambusher \u2192 *Stealth*,
           Juggernaut \u2192 *Brute*, Scout \u2192 *Infiltrator*,
           Missile Boat \u2192 *Indirect Fire*).
        2. **Motion Type** \u2192 movement keywords
           (Jump \u2192 *Jump Pack*, UMU \u2192 *Submersible*,
           VTOL \u2192 *Hover*).
        3. **Weight Class** \u2192 baseline armour / `Anti-'Mech` rules
           (PA(L) cannot leg/swarm; Heavy/Assault cannot jump as far).
        4. **Equipment** \u2192 the gear lists above each map to one trait
           (Stealth/Mimetic \u2192 *Stealth (X)*; Manipulators \u2192
           *Anti-'Mech*; AP Mount \u2192 *AP Weapon Slot*; Magnetic
           Clamps \u2192 *Mech Rider*).
        5. **Weapons** \u2192 traits authored once in
           `data/BattleArmorWeaponRules.csv` flow back here.
        """))
    parts.append("")

OUT.write_text("\n".join(parts), encoding="utf-8")
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
