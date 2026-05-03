"""Generate data/reference/heat-dissipation.md from mech source files.

Heat dissipation = total declared heat sinks * (2 if double, 1 if single).
The declared count in the 'Heat Sinks' field already includes engine-embedded
heat sinks — no separate counting of crit slots is needed.

IMPORTANT: DO NOT count crit slots to derive heat sink count.
  IS Double Heat Sinks occupy 3 crit slots each.
  Clan Double Heat Sinks occupy 2 crit slots each.
  Counting slots would massively over-count.
  The source file 'Heat Sinks' field is the authoritative count.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
from collections import defaultdict
from typing import Optional

ROOT = pathlib.Path(__file__).parent.parent
MECH_INDEX = ROOT / "data" / "index" / "mech_index.json"
OUTPUT = ROOT / "data" / "reference" / "heat-dissipation.md"

HS_RE = re.compile(r"(\d+)\s+(single|double)", re.IGNORECASE)
CLASS_ORDER = ["Light", "Medium", "Heavy", "Assault"]
TECH_ORDER = ["Inner Sphere", "Clan"]


def classify(tonnage) -> Optional[str]:
    if tonnage is None:
        return None
    t = int(tonnage)
    if t <= 35:
        return "Light"
    if t <= 55:
        return "Medium"
    if t <= 75:
        return "Heavy"
    return "Assault"


def parse_mech(idx_record: dict) -> Optional[dict]:
    sp = idx_record.get("source_path")
    if not sp or not pathlib.Path(sp).exists():
        return None
    try:
        raw = json.load(open(sp, encoding="utf-8-sig"))
    except Exception:
        return None

    hs_str = str(raw.get("Heat Sinks") or "").strip()
    match = HS_RE.match(hs_str)
    if not match:
        return None

    count = int(match.group(1))
    hs_type = match.group(2).lower()
    if count == 0:
        return None  # bad/incomplete record

    dissipation = count * (2 if hs_type == "double" else 1)
    cls = classify(idx_record.get("tonnage"))
    if cls is None:
        return None

    return {
        "chassis": idx_record.get("chassis") or "",
        "model": idx_record.get("model") or "",
        "tonnage": idx_record.get("tonnage"),
        "class": cls,
        "tech_base": idx_record.get("tech_base") or "Unknown",
        "count": count,
        "type": hs_type,
        "dissipation": dissipation,
    }


def main() -> int:
    mechs_idx: list[dict] = json.load(open(MECH_INDEX, encoding="utf-8"))
    print(f"[heat-ref] reading {len(mechs_idx)} mech records…")

    records: list[dict] = []
    skipped = 0
    for m in mechs_idx:
        r = parse_mech(m)
        if r:
            records.append(r)
        else:
            skipped += 1

    print(f"[heat-ref] parsed {len(records)} mechs, skipped {skipped}")

    # Per (class, tech_base) stats
    stats: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in records:
        stats[(r["class"], r["tech_base"])].append(r)

    # Build markdown
    lines: list[str] = [
        "# Mech Heat Dissipation Reference",
        "",
        "Heat dissipation is the total number of heat points a mech can shed per turn.",
        "",
        "**Formula**: Total Heat Sinks × (2 if Double Heat Sinks, 1 if Single Heat Sinks)",
        "",
        "> **Note on counting**: The declared heat sink total in the source data includes",
        "> engine-embedded heat sinks. Crit slots are **not** counted — IS Double Heat Sinks",
        "> occupy 3 slots each; Clan Double Heat Sinks occupy 2 slots each. Using slot counts",
        "> would produce incorrect (inflated) totals.",
        "",
        "> Vehicles, Infantry, and Aerospace units do not generate heat and have no Heat Threshold.",
        "",
        "---",
        "",
        "## Summary by Class",
        "",
    ]

    # Summary table
    lines += [
        "| Class | Tech Base | Min Dissipation | Max Dissipation | Sample Size |",
        "| ----- | --------- | --------------: | --------------: | ----------: |",
    ]
    for cls in CLASS_ORDER:
        for tech in TECH_ORDER:
            group = stats.get((cls, tech), [])
            if not group:
                continue
            vals = [r["dissipation"] for r in group]
            min_val = min(vals)
            max_val = max(vals)
            lines.append(
                f"| {cls} | {tech} | {min_val} | {max_val} | {len(group)} |"
            )
    lines.append("")

    # Per-class detail with extremes
    lines += ["---", "", "## Detail by Class", ""]
    for cls in CLASS_ORDER:
        lines.append(f"### {cls}")
        lines.append("")
        for tech in TECH_ORDER:
            group = stats.get((cls, tech), [])
            if not group:
                continue
            vals = [r["dissipation"] for r in group]
            min_val = min(vals)
            max_val = max(vals)
            min_mechs = [r for r in group if r["dissipation"] == min_val]
            max_mechs = [r for r in group if r["dissipation"] == max_val]

            lines.append(f"#### {tech}")
            lines.append("")
            lines.append(f"- **Min dissipation**: {min_val}")
            lines.append(
                f"  - Example: {min_mechs[0]['chassis']} {min_mechs[0]['model']} "
                f"({min_mechs[0]['tonnage']}t, {min_mechs[0]['count']} "
                f"{min_mechs[0]['type'].title()} HS)"
            )
            lines.append(f"- **Max dissipation**: {max_val}")
            lines.append(
                f"  - Example: {max_mechs[0]['chassis']} {max_mechs[0]['model']} "
                f"({max_mechs[0]['tonnage']}t, {max_mechs[0]['count']} "
                f"{max_mechs[0]['type'].title()} HS)"
            )
            lines.append("")

    # Full sorted tables per class
    lines += ["---", "", "## Full Tables", ""]
    for cls in CLASS_ORDER:
        lines.append(f"### {cls} Mechs")
        lines.append("")
        lines.append(
            "| Chassis | Model | Tonnage | Tech Base | HS Count | Type | Dissipation |"
        )
        lines.append("| ------- | ----- | ------: | --------- | -------: | ---- | ----------: |")
        group_all = sorted(
            [r for r in records if r["class"] == cls],
            key=lambda x: (-x["dissipation"], x["tech_base"], x["chassis"], str(x["model"])),
        )
        for r in group_all:
            lines.append(
                f"| {r['chassis']} | {r['model']} | {r['tonnage']} "
                f"| {r['tech_base']} | {r['count']} | {r['type'].title()} "
                f"| {r['dissipation']} |"
            )
        lines.append("")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[heat-ref] wrote {OUTPUT} ({OUTPUT.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
