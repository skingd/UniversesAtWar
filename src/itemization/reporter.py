"""Markdown + JSON report writers for the itemization pipeline."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from .common import write_json


# --- helpers --------------------------------------------------------------

def _md_table(headers: list[str], rows: list[list[Any]]) -> str:
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join("" if c is None else str(c) for c in r) + " |")
    return "\n".join(out)


def _fmt(v: Any) -> str:
    if v is None:
        return ""
    if isinstance(v, float):
        return f"{v:.2f}".rstrip("0").rstrip(".")
    return str(v)


def _summary_row(name: str, block: dict) -> list[Any]:
    if not block or block.get("count", 0) == 0:
        return [name, 0, "—", "—", "—", "—", "—", "—", "—"]
    return [
        name,
        block.get("count"),
        _fmt(block.get("min")),
        _fmt(block.get("max")),
        _fmt(block.get("mean")),
        _fmt(block.get("median")),
        _fmt(block.get("std")),
        _fmt(block.get("p25")),
        _fmt(block.get("p75")),
    ]


# --- per-catalogue markdown -----------------------------------------------
#
# Itemization markdown files are intentionally minimal: a checklist of unique
# item names. They serve as a "things to port" worklist for the rules
# translation. Detailed stats live in the sibling `*.json` files.

def _checklist_md(title: str, records: list[dict]) -> str:
    names = sorted({(r.get("display_name") or "").strip()
                    for r in records if r.get("display_name")})
    lines = [f"# {title}", "", f"_{len(names)} unique items_", ""]
    lines += [f"- [ ] {n}" for n in names]
    return "\n".join(lines) + "\n"


def _weapons_md(weapons: list[dict]) -> str:
    return _checklist_md("Weapons", weapons)


def _ammo_md(ammo: list[dict]) -> str:
    return _checklist_md("Ammunition", ammo)


def _equipment_md(equipment: list[dict]) -> str:
    return _checklist_md("Equipment", equipment)


def _upgrades_md(upgrades: list[dict]) -> str:
    return _checklist_md("Upgrades", upgrades)


def _capabilities_units_md(unit_aggregations: dict) -> str:
    sections = ["# Unit Capabilities\n"]
    for ut, block in unit_aggregations.items():
        sections.append(f"## {ut.title()} ({block.get('count', 0)} units)\n")
        rows = []
        for field, payload in block.items():
            if not isinstance(payload, dict) or "count" not in payload:
                continue
            rows.append(_summary_row(field, payload))
        sections.append(_md_table(
            ["Field", "N", "Min", "Max", "Mean", "Median", "Std", "p25", "p75"],
            rows,
        ))
        # categorical breakdowns
        for field, payload in block.items():
            if isinstance(payload, dict) and "count" not in payload and payload:
                if field in ("by_tier_tonnage",):
                    continue
                top = list(payload.items())[:10]
                sections.append(f"\n_Top {field}_: " + ", ".join(
                    f"{k}={v}" for k, v in top
                ))
        sections.append("\n")
    return "\n".join(sections)


def _capabilities_weapons_md(weapon_aggregations: dict) -> str:
    out = [f"# Weapon Capabilities ({weapon_aggregations.get('count', 0)} weapons)\n"]
    out.append("## Overall\n")
    rows = [_summary_row(name, blk) for name, blk in (weapon_aggregations.get("overall") or {}).items()]
    out.append(_md_table(
        ["Field", "N", "Min", "Max", "Mean", "Median", "Std", "p25", "p75"], rows,
    ))
    out.append("\n## Derived\n")
    rows = [_summary_row(name, blk) for name, blk in (weapon_aggregations.get("derived") or {}).items()]
    out.append(_md_table(
        ["Field", "N", "Min", "Max", "Mean", "Median", "Std", "p25", "p75"], rows,
    ))
    out.append("\n## By Category — Damage Distribution\n")
    rows = []
    for cat, blk in (weapon_aggregations.get("by_category") or {}).items():
        rows.append([cat, blk.get("count")] + _summary_row("", blk.get("damage") or {})[2:])
    out.append(_md_table(
        ["Category", "N", "Min", "Max", "Mean", "Median", "Std", "p25", "p75"], rows,
    ))
    out.append("\n## By Subcategory — Long Range\n")
    rows = []
    for sub, blk in (weapon_aggregations.get("by_subcategory") or {}).items():
        rows.append([sub, blk.get("count")] + _summary_row("", blk.get("long_range") or {})[2:])
    out.append(_md_table(
        ["Subcategory", "N", "Min", "Max", "Mean", "Median", "Std", "p25", "p75"], rows,
    ))
    return "\n".join(out) + "\n"


def _bands_md(bands: dict) -> str:
    out = ["# Translation Bands (P2.3)\n"]
    for stat, payload in bands.items():
        out.append(f"## {stat}\n")
        if "error" in payload:
            out.append(f"_skipped: {payload['error']}_\n")
            continue
        for k, v in payload.items():
            if k == "validation_misses":
                continue
            if isinstance(v, dict):
                out.append(f"- **{k}**: " + ", ".join(f"{kk}={vv}" for kk, vv in v.items()))
            elif isinstance(v, list):
                out.append(f"- **{k}**: {v}")
            else:
                out.append(f"- **{k}**: {v}")
        misses = payload.get("validation_misses")
        if misses:
            out.append("\n_Validation misses_:")
            out.append(_md_table(
                ["Item", "Expected", "Actual", "Detail"],
                [[m.get("name"), m.get("expected"), m.get("actual"),
                  ", ".join(f"{k}={v}" for k, v in m.items() if k not in ("name", "expected", "actual"))]
                 for m in misses],
            ))
        out.append("")
    return "\n".join(out) + "\n"


# --- top-level driver -----------------------------------------------------

def write_all(
    output_dir: Path,
    catalogues: dict,
    unit_aggregations: dict,
    weapon_aggregations: dict,
    bands: dict,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    write_json(output_dir / "weapons.json", catalogues["weapons"])
    write_json(output_dir / "ammunition.json", catalogues["ammunition"])
    write_json(output_dir / "equipment.json", catalogues["equipment"])
    write_json(output_dir / "upgrades.json", catalogues["upgrades"])
    write_json(output_dir / "coverage.json", catalogues["coverage"])
    write_json(output_dir / "capabilities_units.json", unit_aggregations)
    write_json(output_dir / "capabilities_weapons.json", weapon_aggregations)
    write_json(output_dir / "translation_bands.json", bands)

    (output_dir / "weapons.md").write_text(_weapons_md(catalogues["weapons"]), encoding="utf-8")
    (output_dir / "ammunition.md").write_text(_ammo_md(catalogues["ammunition"]), encoding="utf-8")
    (output_dir / "equipment.md").write_text(_equipment_md(catalogues["equipment"]), encoding="utf-8")
    (output_dir / "upgrades.md").write_text(_upgrades_md(catalogues["upgrades"]), encoding="utf-8")
    (output_dir / "capabilities_units.md").write_text(_capabilities_units_md(unit_aggregations), encoding="utf-8")
    (output_dir / "capabilities_weapons.md").write_text(_capabilities_weapons_md(weapon_aggregations), encoding="utf-8")
    (output_dir / "translation_bands.md").write_text(_bands_md(bands), encoding="utf-8")

    cov = catalogues["coverage"]
    report = [
        "# Itemization Report\n",
        "## Catalogue Sizes\n",
        _md_table(
            ["Catalogue", "Entries"],
            [
                ["Weapons",     len(catalogues["weapons"])],
                ["Ammunition",  len(catalogues["ammunition"])],
                ["Equipment",   len(catalogues["equipment"])],
                ["Upgrades",    len(catalogues["upgrades"])],
            ],
        ),
        "\n## Coverage\n",
        f"- by_catalogue: {cov.get('by_catalogue')}",
        f"- missing_classification: {len(cov.get('missing_classification') or [])}",
        f"- uncatalogued_count: {cov.get('uncatalogued_count')}",
        f"- orphan_count: {cov.get('orphan_count')}",
        f"- **blocking: {cov.get('blocking')}**",
        "\n## Unit Counts\n",
        _md_table(
            ["Unit Type", "Count"],
            [[ut, blk.get("count", 0)] for ut, blk in unit_aggregations.items()],
        ),
        "\n## Weapon Distribution Summary\n",
        f"- weapons: {weapon_aggregations.get('count')}",
        f"- categories: {weapon_aggregations.get('category_counts')}",
        f"- tech_base: {weapon_aggregations.get('tech_base_counts')}",
        "\n## Translation Bands (proposal)\n",
    ]
    for stat, payload in bands.items():
        if "error" in payload:
            report.append(f"- **{stat}**: skipped ({payload['error']})")
            continue
        cps = payload.get("cut_points") or {}
        rate = payload.get("validation_hit_rate")
        rate_s = f" — validation {rate*100:.0f}%" if rate is not None else ""
        report.append(f"- **{stat}**: cuts={cps}{rate_s}")
    (output_dir / "REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
