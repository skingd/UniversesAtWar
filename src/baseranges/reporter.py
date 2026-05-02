"""Render `base_ranges.json` and `base_ranges.md`."""
from __future__ import annotations

import json
from pathlib import Path


def write_json(report: dict, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    p = out_dir / "base_ranges.json"
    p.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    return p


def _fmt(value) -> str:
    if value is None:
        return "—"
    if isinstance(value, float):
        # Drop trailing zeros for clean tables.
        return f"{value:g}"
    return str(value)


def _summary_cells(s: dict | None) -> tuple[str, str, str]:
    if not s or s.get("count", 0) == 0:
        return ("—", "—", "—")
    return (_fmt(s.get("min")), _fmt(s.get("max")), _fmt(s.get("median")))


def _render_unit_section(unit_type: str, block: dict) -> str:
    movement_label = block["movement_field"]
    tier_label = block["tier_label"]
    overall = block["overall"]
    by_tier = block["by_tier"]

    lines: list[str] = []
    lines.append(f"## {unit_type}")
    lines.append("")
    lines.append(f"_Movement field: `{movement_label}`. Tier dimension: `{tier_label}`._")
    lines.append("")

    has_armor = "armor" in overall

    # Overall row.
    mv = overall.get("movement", {})
    n = overall.get("n", 0)
    mv_min, mv_max, mv_med = _summary_cells(mv)
    if has_armor:
        ar = overall.get("armor", {})
        ar_min, ar_max, ar_med = _summary_cells(ar)
        lines.append("### Overall")
        lines.append("")
        lines.append("| N | Movement min | Movement max | Movement median | Armor min | Armor max | Armor median |")
        lines.append("|---|---|---|---|---|---|---|")
        lines.append(f"| {n} | {mv_min} | {mv_max} | {mv_med} | {ar_min} | {ar_max} | {ar_med} |")
    else:
        lines.append("### Overall")
        lines.append("")
        lines.append("| N | Movement min | Movement max | Movement median |")
        lines.append("|---|---|---|---|")
        lines.append(f"| {n} | {mv_min} | {mv_max} | {mv_med} |")
    lines.append("")

    # Per-tier breakdown.
    if by_tier:
        lines.append(f"### By {tier_label}")
        lines.append("")
        if has_armor:
            lines.append(f"| {tier_label} | N | Movement min | Movement max | Movement median | Armor min | Armor max | Armor median |")
            lines.append("|---|---|---|---|---|---|---|---|")
        else:
            lines.append(f"| {tier_label} | N | Movement min | Movement max | Movement median |")
            lines.append("|---|---|---|---|---|")
        for tier in sorted(by_tier):
            blk = by_tier[tier]
            tn = blk.get("n", 0)
            mv_min, mv_max, mv_med = _summary_cells(blk.get("movement"))
            if has_armor:
                ar_min, ar_max, ar_med = _summary_cells(blk.get("armor"))
                lines.append(f"| {tier} | {tn} | {mv_min} | {mv_max} | {mv_med} | {ar_min} | {ar_max} | {ar_med} |")
            else:
                lines.append(f"| {tier} | {tn} | {mv_min} | {mv_max} | {mv_med} |")
        lines.append("")

    return "\n".join(lines)


def write_markdown(report: dict, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    p = out_dir / "base_ranges.md"

    parts: list[str] = [
        "# Base Value Ranges",
        "",
        "Distilled per-unit-type base movement and armor ranges from the "
        "canonical `data/index/*` files. **Read-only**: no unit files are "
        "modified by this report. MASC, jump, and other rule-driven "
        "modifiers are intentionally excluded.",
        "",
    ]
    for unit_type in sorted(report):
        parts.append(_render_unit_section(unit_type, report[unit_type]))

    p.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    return p


def write_report(report: dict, out_dir: Path) -> tuple[Path, Path]:
    return write_json(report, out_dir), write_markdown(report, out_dir)
