"""Phase D — report generation."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from typing import Iterable

from .common import Issue, write_json


def write_issues_jsonl(path: Path, issues: Iterable[Issue]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        import json
        for i in issues:
            f.write(json.dumps(i.to_dict(), ensure_ascii=False) + "\n")


def write_csv(path: Path, rows: list[dict], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for r in rows:
            writer.writerow({c: _csv_value(r.get(c, "")) for c in columns})


def _csv_value(v) -> str:
    if isinstance(v, (list, dict)):
        import json
        return json.dumps(v, ensure_ascii=False)
    return "" if v is None else str(v)


def write_reports(
    output_dir: Path,
    inventory: dict,
    index_summary: dict,
    resolution_report: dict,
    quirk_report: dict,
    era_report: dict,
    ammo_report: dict,
    field_report: dict,
    range_report: dict,
    duplicate_report: dict,
    orphan_report: dict,
    all_issues: list[Issue],
    *,
    fail_threshold_pct: float,
    gate_types: tuple[str, ...],
    strict: bool,
) -> tuple[bool, str]:
    """Write every report file. Returns (passed, status_message)."""
    output_dir.mkdir(parents=True, exist_ok=True)

    write_json(output_dir / "inventory.json", inventory)
    write_json(output_dir / "equipment_resolution.json", resolution_report)
    write_issues_jsonl(output_dir / "issues.jsonl", all_issues)

    # CSV breakdowns
    unresolved_rows = []
    for u in resolution_report.get("per_unit", []):
        for unr in u.get("unresolved", []):
            unresolved_rows.append({
                "unit_type": u["unit_type"],
                "unit_key": u["key"],
                "chassis": u.get("chassis"),
                "model": u.get("model"),
                "source_path": u["source_path"],
                "raw": unr["raw"],
                "normalized": unr["normalized"],
                "tech_base": unr.get("tech_base"),
                "fuzzy_suggestions": unr.get("fuzzy_suggestions"),
            })
    write_csv(
        output_dir / "unresolved_equipment.csv",
        unresolved_rows,
        ["unit_type", "unit_key", "chassis", "model", "source_path",
         "raw", "normalized", "tech_base", "fuzzy_suggestions"],
    )

    malformed = [i.to_dict() for i in all_issues if i.category == "parse"]
    write_csv(
        output_dir / "malformed_files.csv",
        malformed,
        ["severity", "category", "path", "message", "detail"],
    )

    duplicates = [i.to_dict() for i in all_issues if i.category in (
        "duplicate-unit", "duplicate-equipment-id", "duplicate-canonical-id", "duplicate-numeric-id"
    )]
    write_csv(
        output_dir / "duplicates.csv",
        duplicates,
        ["severity", "category", "path", "message", "detail"],
    )

    missing = [i.to_dict() for i in all_issues if i.category == "missing-field"]
    write_csv(
        output_dir / "missing_fields.csv",
        missing,
        ["severity", "category", "path", "message", "detail"],
    )

    range_violations = [i.to_dict() for i in all_issues if i.category in ("out-of-range", "non-numeric")]
    write_csv(
        output_dir / "range_violations.csv",
        range_violations,
        ["severity", "category", "path", "message", "detail"],
    )

    write_csv(
        output_dir / "orphan_equipment.csv",
        orphan_report.get("orphans", []),
        ["canonical_id", "display_name", "category", "tech_base"],
    )

    # --- Master REPORT.md
    issue_counts = Counter((i.severity, i.category) for i in all_issues)
    error_total = sum(n for (sev, _), n in issue_counts.items() if sev == "error")
    warning_total = sum(n for (sev, _), n in issue_counts.items() if sev == "warning")

    res = resolution_report["totals"]
    rate = resolution_report["resolution_rate"]
    by_type = resolution_report.get("by_type", {})
    unresolved_pct = 100.0 - rate if res["total_refs"] > 0 else 0.0

    # Compute the gated unresolved % across only the gate-types
    gate_total = sum(
        max(0, by_type.get(ut, {}).get("total_refs", 0)
            - by_type.get(ut, {}).get("structural", 0))
        for ut in gate_types
    )
    gate_unresolved = sum(by_type.get(ut, {}).get("unresolved", 0) for ut in gate_types)
    gated_pct = round(100.0 * gate_unresolved / gate_total, 3) if gate_total else 0.0

    blocking_issues: list[str] = []
    if inventory["totals"]["parse_failures"] > 0:
        blocking_issues.append(f"{inventory['totals']['parse_failures']} parse failure(s)")
    if duplicate_report.get("equipment_duplicate_numeric_ids", 0) > 0:
        blocking_issues.append(f"{duplicate_report['equipment_duplicate_numeric_ids']} duplicate equipment ID(s)")
    if gated_pct > fail_threshold_pct:
        blocking_issues.append(
            f"gated unresolved equipment {gated_pct:.3f}% > threshold {fail_threshold_pct}% "
            f"(gate types: {','.join(gate_types)})"
        )
    if strict and warning_total > 0:
        blocking_issues.append(f"strict mode: {warning_total} warning(s)")

    passed = not blocking_issues
    status = "PASS" if passed else "FAIL"
    status_line = f"STATUS: {status}"

    md = _render_master_report(
        status_line=status_line,
        blocking_issues=blocking_issues,
        inventory=inventory,
        index_summary=index_summary,
        resolution=res,
        rate=rate,
        by_type=by_type,
        gate_types=gate_types,
        gated_pct=gated_pct,
        unresolved_pct=unresolved_pct,
        top_unresolved=resolution_report.get("top_unresolved", []),
        quirk_report=quirk_report,
        era_report=era_report,
        ammo_report=ammo_report,
        field_report=field_report,
        range_report=range_report,
        duplicate_report=duplicate_report,
        orphan_report=orphan_report,
        error_total=error_total,
        warning_total=warning_total,
    )
    (output_dir / "REPORT.md").write_text(md, encoding="utf-8")

    summary_msg = f"{status} — {len(all_issues)} issue(s) ({error_total} error / {warning_total} warning)"
    if blocking_issues:
        summary_msg += " | blockers: " + "; ".join(blocking_issues)
    return passed, summary_msg


def _render_master_report(**kw) -> str:
    inv = kw["inventory"]
    rs = kw["resolution"]
    field_r = kw["field_report"]

    units_table = "\n".join(
        f"| {ut} | {meta['count']} |" for ut, meta in inv["units"].items()
    )
    weapons_table = "\n".join(
        f"| {cat} | {meta['count']} |" for cat, meta in inv["weapons"].items()
    )
    by_type = kw["by_type"]
    gate_set = set(kw["gate_types"])
    by_type_table = "\n".join(
        f"| {ut}{' ✓' if ut in gate_set else ''} | {t['total_refs']} | {t['structural']} | "
        f"{t['exact'] + t['tech_disambiguated']} | {t['unresolved']} | "
        f"{t['resolution_rate']}% | {t['unresolved_pct']}% |"
        for ut, t in sorted(by_type.items())
    )
    top_unr = "\n".join(
        f"| `{ref}` | {n} |" for ref, n in (kw["top_unresolved"] or [])[:20]
    ) or "| _(none)_ | |"

    blockers = "\n".join(f"- {b}" for b in kw["blocking_issues"]) or "_(none)_"

    field_table = "\n".join(
        f"| {ut} | {summary['files_checked'] if 'files_checked' in summary else summary.get('records_checked', 0)} | {summary['missing_field_count']} |"
        for ut, summary in field_r.items()
    )

    return f"""# BattleTech Data Check Report

{kw["status_line"]}

**Total issues:** {kw["error_total"]} error / {kw["warning_total"]} warning

## Blocking issues
{blockers}

---

## 1. Inventory

| Unit Type | Count |
|---|---|
{units_table}

| Weapon Category | Count |
|---|---|
{weapons_table}

- **Reference files:** {inv["reference"]["count"]}
- **Parse failures:** {inv["totals"]["parse_failures"]}

## 2. Canonical Indices Built

- equipment_index.json — **{kw["index_summary"]["equipment_count"]}** records (incl. **{kw["index_summary"].get("synthesized_count", 0)}** synthesized from unit references)
- equipment_aliases.json — **{kw["index_summary"]["alias_count"]}** alias keys
- reference_index.json — {len(kw["index_summary"]["reference_files"])} reference files indexed
- mech_index.json / vehicle_index.json / aerospace_index.json / infantry_index.json built

## 3. Equipment Reference Resolution

| Outcome | Count |
|---|---|
| Total references | {rs["total_refs"]} |
| Exact match | {rs["exact"]} |
| Tech-disambiguated match | {rs["tech_disambiguated"]} |
| Structural (skipped) | {rs["structural"]} |
| **Unresolved** | **{rs["unresolved"]}** |

**Resolution rate (excluding structural):** {kw["rate"]}%
**Overall unresolved percentage:** {kw["unresolved_pct"]:.3f}%
**Gated unresolved % (gate types: {','.join(kw["gate_types"])}):** **{kw["gated_pct"]:.3f}%**

### Per unit type

| Unit Type | Total Refs | Structural | Resolved | Unresolved | Resolution Rate | Unresolved % |
|---|---|---|---|---|---|---|
{by_type_table}

_✓ = counted toward FAIL gate_

### Top 20 unresolved references

| Reference | Frequency |
|---|---|
{top_unr}

## 4. Quirks
- Total: {kw["quirk_report"].get("total", 0)}
- Unknown quirks: {kw["quirk_report"].get("unknown_count", 0)}

## 5. Era Coverage
- Units with year field: {kw["era_report"].get("total_with_year", 0)}
- Years outside known era spans: {kw["era_report"].get("out_of_range", 0)}

## 6. Ammo → Weapon Linkage
- Matched: {kw["ammo_report"].get("matched", 0)}
- Unmatched (orphan ammo): {kw["ammo_report"].get("unmatched", 0)}

## 7. Required Fields

| Category | Files Checked | Missing Field Issues |
|---|---|---|
{field_table}

## 8. Range Validation
- Numeric / range violations: {kw["range_report"].get("violations", 0)}

## 9. Duplicates
{_dict_block(kw["duplicate_report"])}

## 10. Orphan Equipment (informational)
- Equipment never referenced by any unit: **{kw["orphan_report"].get("orphan_count", 0)}**

---

See `output/data-check/` for per-issue CSVs and `issues.jsonl` for the full machine-readable issue stream.
"""


def _dict_block(d: dict) -> str:
    if not d:
        return "_(none)_"
    return "\n".join(f"- {k}: {v}" for k, v in d.items())
