"""Render detachment JSON records into stylized HTML cards.

Card layout follows the example in ``examples/Legions-Imperialis-Kratos-Squad.jpg``:
  Front: header band, sub-band (unit-type/scale + detachment size), stat row,
         weapon bullet list, weapon profile table, special rules.
  Back:  header band, points value, description, upgrades (size + special ammo).

Weapon profiles are joined from ``data/WeaponRules.csv`` at render time
(the detachment JSON only carries weapon links).
"""
from __future__ import annotations

import html
from typing import Iterable, Optional

from src.detachments.weapons import AmmoOption, WeaponProfile


# ---------------------------------------------------------------------------
# CSS  (single embedded stylesheet shared by every card on a page)
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Card size definitions
# ---------------------------------------------------------------------------

# Each entry: (card_width, card_height, body_font_px)
CARD_SIZES: dict[str, tuple[str, str, int]] = {
    "6x4": ("6in",  "4in",  11),
    "5x3": ("5in",  "3in",  9),
}
_DEFAULT_SIZE = "6x4"


# ---------------------------------------------------------------------------
# CSS  (generated per size so card dimensions are baked in)
# ---------------------------------------------------------------------------

def card_css(size: str = _DEFAULT_SIZE) -> str:
    w, h, font = CARD_SIZES.get(size, CARD_SIZES[_DEFAULT_SIZE])
    # Scale minor measurements proportionally to font size (base = 11px at 6x4).
    ratio = font / 11
    band_px      = round(14 * ratio)
    sub_px       = round(10 * ratio)
    section_px   = round(11 * ratio)
    title_px     = round(14 * ratio)
    pad          = f"{round(8 * ratio)}px {round(10 * ratio)}px"
    pad_subband  = f"{round(4 * ratio)}px {round(10 * ratio)}px"
    return f"""
:root {{
  --band: #1f3a4d;
  --band-text: #ffffff;
  --rule: #cfd6db;
  --row-alt: #f3f5f7;
  --ink: #1a1a1a;
  --muted: #5b6b75;
  --card-w: {w};
  --card-h: {h};
}}
* {{ box-sizing: border-box; }}
body {{
  font-family: 'Georgia', 'Times New Roman', serif;
  background: #e7eaed;
  margin: 0;
  padding: 0.375in;
  color: var(--ink);
}}
h1.page-title {{
  font-family: 'Georgia', serif;
  font-size: {round(22 * ratio)}px;
  margin: 0 0 0.2in 0;
  color: var(--band);
}}
/* Screen: wrap pairs in rows */
.cards {{
  display: flex;
  flex-direction: column;
  gap: 0.15in;
}}
.pair {{
  display: flex;
  flex-direction: row;
  gap: 0.1in;
  break-inside: avoid;
  page-break-inside: avoid;
}}
.card {{
  background: #fdfdfd;
  border: 1px solid #b9c2c8;
  border-radius: 4px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.08);
  font-size: {font}px;
  line-height: 1.3;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  width: var(--card-w);
  height: var(--card-h);
  flex-shrink: 0;
}}
.card .band {{
  background: var(--band);
  color: var(--band-text);
  text-align: center;
  padding: {pad_subband};
  font-variant: small-caps;
  letter-spacing: 0.04em;
  flex-shrink: 0;
}}
.card .band .title {{
  font-size: {title_px}px;
  font-weight: bold;
}}
.card .band .sub {{
  font-size: {sub_px}px;
  opacity: 0.92;
  margin-top: 1px;
}}
.card .subband {{
  background: #e9eef2;
  border-bottom: 1px solid var(--rule);
  display: flex;
  justify-content: space-between;
  padding: {pad_subband};
  font-variant: small-caps;
  font-size: {sub_px}px;
  color: var(--muted);
  letter-spacing: 0.05em;
  flex-shrink: 0;
}}
.card .body {{
  padding: {pad};
  flex: 1;
  overflow: hidden;
}}
.card table {{
  border-collapse: collapse;
  width: 100%;
  margin: 2px 0 5px 0;
}}
.card th, .card td {{
  text-align: left;
  padding: 2px 4px;
  border-bottom: 1px solid var(--rule);
  vertical-align: top;
}}
.card th {{
  font-weight: bold;
  font-size: {sub_px}px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  background: #eef2f5;
}}
.card tbody tr:nth-child(even) td {{ background: var(--row-alt); }}
.card .weapons-bullets {{
  margin: 2px 0 4px 14px;
  padding: 0;
}}
.card .weapons-bullets li {{ margin: 1px 0; }}
.card .section-h {{
  background: var(--band);
  color: var(--band-text);
  padding: 2px 7px;
  font-variant: small-caps;
  letter-spacing: 0.05em;
  font-size: {section_px}px;
  font-weight: bold;
  margin: 5px -{round(10 * ratio)}px 3px -{round(10 * ratio)}px;
}}
.card .body > .section-h:first-child {{ margin-top: 0; }}
.card .special-rules {{
  font-size: {sub_px}px;
  margin-top: 3px;
}}
.card .special-rules .label {{
  font-variant: small-caps;
  font-weight: bold;
  letter-spacing: 0.05em;
}}
.card .upgrade-line {{
  display: flex;
  align-items: baseline;
  gap: 4px;
  margin: 2px 0;
}}
.card .upgrade-line .desc {{ white-space: nowrap; }}
.card .upgrade-line .dots {{
  flex: 1;
  border-bottom: 2px dotted var(--muted);
  transform: translateY(-3px);
  margin: 0 3px;
}}
.card .upgrade-line .cost {{
  font-weight: bold;
  white-space: nowrap;
}}
.card .description {{
  margin: 4px 0 6px 0;
  font-style: italic;
  color: var(--muted);
}}
.card .points-line {{
  text-align: center;
  font-size: {section_px}px;
  font-variant: small-caps;
  letter-spacing: 0.06em;
  background: #e9eef2;
  border-bottom: 1px solid var(--rule);
  padding: 3px 0;
  flex-shrink: 0;
}}
.card .points-line strong {{ font-size: {band_px}px; }}
.empty {{ color: var(--muted); font-style: italic; }}
@media print {{
  @page {{ margin: 0.375in; }}
  body {{ background: white; padding: 0; }}
  h1.page-title {{ display: none; }}
  .pair {{
    break-after: always;
    page-break-after: always;
  }}
  .pair:last-child {{
    break-after: avoid;
    page-break-after: avoid;
  }}
  .card {{ box-shadow: none; border-color: #999; }}
}}
""".strip()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _h(s: object) -> str:
    return html.escape("" if s is None else str(s))


def _ap_str(ap: int) -> str:
    if ap == 0:
        return "0"
    return f"{ap:+d}"


def _profile_for(name: str, profiles: dict[str, WeaponProfile]) -> Optional[WeaponProfile]:
    return profiles.get(name)


def _aggregate_weapons(weapons: list[dict]) -> list[tuple[str, int]]:
    """Aggregate weapons by display name preserving first-occurrence order."""
    counts: dict[str, int] = {}
    order: list[str] = []
    for w in weapons:
        n = w.get("name") or ""
        if n not in counts:
            counts[n] = 0
            order.append(n)
        counts[n] += 1
    return [(n, counts[n]) for n in order]


def _merged_traits(profile_traits: list[str], added: list[str]) -> str:
    seen: list[str] = []
    for t in list(profile_traits) + list(added or []):
        if t and t not in seen:
            seen.append(t)
    return ", ".join(seen)


# ---------------------------------------------------------------------------
# Front / back rendering
# ---------------------------------------------------------------------------

def _render_weapon_table(
    weapons: list[dict],
    profiles: dict[str, WeaponProfile],
) -> str:
    """Render the weapon-profile table.

    Each unique (name, traits_added) combination renders as one row. We do
    NOT collapse to ``x2`` per the spec.
    """
    if not weapons:
        return '<p class="empty">No weapons.</p>'
    rows: list[str] = []
    seen: set[tuple[str, tuple[str, ...]]] = set()
    for w in weapons:
        name = w.get("name") or ""
        added = tuple(w.get("traits_added") or [])
        key = (name, added)
        if key in seen:
            continue
        seen.add(key)
        prof = _profile_for(name, profiles)
        if prof is None:
            rows.append(
                f"<tr><td>{_h(name)}</td>"
                f"<td colspan='6' class='empty'>profile missing in WeaponRules.csv</td>"
                f"<td>{_h(', '.join(added))}</td></tr>"
            )
            continue
        traits_str = _merged_traits(prof.traits, list(added))
        rows.append(
            "<tr>"
            f"<td>{_h(prof.name)}</td>"
            f"<td>{_h(prof.range)}</td>"
            f"<td>{_h(prof.heat)}</td>"
            f"<td>{_h(prof.dice)}</td>"
            f"<td>{_h(prof.to_hit)}</td>"
            f"<td>{_h(_ap_str(prof.ap))}</td>"
            f"<td>{_h(prof.type)}</td>"
            f"<td>{_h(traits_str)}</td>"
            "</tr>"
        )
    return (
        "<table class='weapons'>"
        "<thead><tr>"
        "<th>Weapon</th><th>Range</th><th>Heat</th><th>Dice</th>"
        "<th>To-Hit</th><th>AP</th><th>Type</th><th>Traits</th>"
        "</tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table>"
    )


def render_front(detachment: dict, profiles: dict[str, WeaponProfile]) -> str:
    name = detachment.get("name") or ""
    det_label = detachment.get("detachment") or ""
    unit_type = detachment.get("unit_type") or ""
    scale = detachment.get("scale")
    save = detachment.get("armor_save") or ""
    movement = detachment.get("movement") or ""
    wounds = detachment.get("wounds")
    ds = detachment.get("detachment_size") or {}
    base_size = ds.get("base") or 1

    type_scale = f"{unit_type} ({scale})" if scale is not None else unit_type

    bullets = detachment.get("weapons_bulleted") or []
    bullet_html = "".join(f"<li>{_h(b)}</li>" for b in bullets)

    weapons_html = _render_weapon_table(detachment.get("weapons") or [], profiles)

    sr = detachment.get("special_rules") or []
    sr_html = (
        f"<div class='special-rules'><span class='label'>Special Rules:</span> {_h(', '.join(sr))}</div>"
        if sr else ""
    )

    return (
        "<div class='card front'>"
        "<div class='band'>"
        f"<div class='title'>{_h(name)}</div>"
        f"<div class='sub'>{_h(det_label)}</div>"
        "</div>"
        "<div class='subband'>"
        f"<span>{_h(type_scale)}</span>"
        f"<span>Detachment Size: {_h(base_size)}</span>"
        "</div>"
        "<div class='body'>"
        "<table class='stats'><thead><tr>"
        "<th>Name</th><th>Movement</th><th>Save</th><th>W</th>"
        "</tr></thead><tbody><tr>"
        f"<td>{_h(name)}</td><td>{_h(movement)}</td><td>{_h(save)}</td><td>{_h(wounds)}</td>"
        "</tr></tbody></table>"
        "<div class='section-h'>Weapons</div>"
        f"<ul class='weapons-bullets'>{bullet_html}</ul>"
        f"{weapons_html}"
        f"{sr_html}"
        "</div>"
        "</div>"
    )


def _unit_noun(detachment: dict) -> str:
    """Singular noun for the consists-of line, e.g. 'BattleMech', 'Vehicle'."""
    return detachment.get("unit_type") or "unit"


def _render_size_upgrades(
    detachment: dict,
) -> list[str]:
    """One <div class='upgrade-line'> per size step. Empty list if none."""
    upgrades = detachment.get("upgrade_options") or {}
    size_steps = upgrades.get("detachment_size") or []
    out: list[str] = []
    for step in size_steps:
        add = step.get("add")
        cost = step.get("cost")
        cost_str = f"+{cost} points" if cost is not None else "+? points"
        out.append(
            "<div class='upgrade-line'>"
            f"<span class='desc'>Increase the Detachment size by {_h(add)}</span>"
            "<span class='dots'></span>"
            f"<span class='cost'>{_h(cost_str)}</span>"
            "</div>"
        )
    return out


def _render_special_ammo(
    detachment: dict,
    ammo_index: dict[str, list[AmmoOption]],
) -> str:
    upgrades = detachment.get("upgrade_options") or {}
    ammo_links = upgrades.get("special_ammo") or []
    if not ammo_links:
        return ""
    # Group by weapon for readability
    by_weapon: dict[str, list[dict]] = {}
    order: list[str] = []
    for a in ammo_links:
        w = a.get("weapon_name") or ""
        if w not in by_weapon:
            by_weapon[w] = []
            order.append(w)
        by_weapon[w].append(a)

    rows: list[str] = []
    for wname in order:
        for a in by_weapon[wname]:
            cost = a.get("points")
            cost_str = f"+{cost} points" if cost is not None else "+? points"
            rows.append(
                "<div class='upgrade-line'>"
                f"<span class='desc'>{_h(a.get('ammo_name'))} ammo for {_h(wname)}</span>"
                "<span class='dots'></span>"
                f"<span class='cost'>{_h(cost_str)}</span>"
                "</div>"
            )
    note = (
        "<p style='margin:4px 0; font-size:10.5px;'>"
        "This detachment can take up to 3 Special Ammo choices from the "
        "Special Ammo list, provided all three are for one or more weapons "
        "listed in the Detachment&rsquo;s Weapons section.</p>"
    )
    return "<div class='section-h'>Special Ammunition</div>" + note + "".join(rows)


def render_back(
    detachment: dict,
    ammo_index: dict[str, list[AmmoOption]],
) -> str:
    name = detachment.get("name") or ""
    points = detachment.get("points")
    points_str = f"<strong>{points}</strong> Points" if points is not None else "<em>Points TBD</em>"

    ds = detachment.get("detachment_size") or {}
    base_size = ds.get("base") or 1
    max_size = ds.get("max") or base_size
    noun = _unit_noun(detachment)
    plural = noun if noun.endswith("s") else (noun + ("" if base_size == 1 else "s"))
    description = f"A {_h(name)} detachment consists of {base_size} {_h(plural)}."

    size_lines = _render_size_upgrades(detachment)
    ammo_html = _render_special_ammo(detachment, ammo_index)

    upgrade_intro = ""
    if size_lines:
        upgrade_intro = (
            f"<p style='margin:4px 0; font-size:10.5px;'>This detachment can purchase any of "
            f"the following upgrades. It may purchase the same upgrade multiple times, "
            f"to a maximum Detachment size of {max_size}:</p>"
        )

    upgrades_section = ""
    if size_lines or ammo_html:
        upgrades_section = (
            "<div class='section-h'>Upgrades</div>"
            f"{upgrade_intro}"
            f"{''.join(size_lines)}"
            f"{ammo_html}"
        )
    else:
        upgrades_section = (
            "<div class='section-h'>Upgrades</div>"
            "<p class='empty'>No upgrades available.</p>"
        )

    return (
        "<div class='card back'>"
        "<div class='band'>"
        f"<div class='title'>{_h(name)}</div>"
        "<div class='sub'>Detachment Card &mdash; Reverse</div>"
        "</div>"
        f"<div class='points-line'>{points_str}</div>"
        "<div class='body'>"
        f"<p class='description'>{description}</p>"
        f"{upgrades_section}"
        "</div>"
        "</div>"
    )


# ---------------------------------------------------------------------------
# Page assembly
# ---------------------------------------------------------------------------

def render_page(
    title: str,
    detachments: Iterable[dict],
    profiles: dict[str, WeaponProfile],
    ammo_index: dict[str, list[AmmoOption]],
    card_size: str = _DEFAULT_SIZE,
) -> str:
    pairs: list[str] = []
    for det in detachments:
        front = render_front(det, profiles)
        back = render_back(det, ammo_index)
        pairs.append(f"<div class='pair'>{front}{back}</div>")

    w, h, _ = CARD_SIZES.get(card_size, CARD_SIZES[_DEFAULT_SIZE])
    return (
        "<!doctype html>\n"
        "<html lang='en'>\n<head>\n"
        "<meta charset='utf-8'>\n"
        f"<title>{_h(title)}</title>\n"
        f"<style>{card_css(card_size)}</style>\n"
        "</head>\n<body>\n"
        f"<h1 class='page-title'>{_h(title)} "
        f"<small style='font-size:0.6em;color:#5b6b75;'>({w} &times; {h} cards)</small></h1>\n"
        f"<div class='cards'>{''.join(pairs)}</div>\n"
        "</body>\n</html>\n"
    )
