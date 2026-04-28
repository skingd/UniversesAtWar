"""Phase B — cross-reference validation.

Resolves every equipment, quirk, faction, and era reference in unit files
against the canonical indices. Produces both per-unit resolution detail and
a corpus-wide summary.
"""
from __future__ import annotations

from collections import Counter
from typing import Any

from .alias_resolver import AliasIndex, parse_reference, is_structural
from .common import Issue


def resolve_unit_equipment(
    unit_indices: dict[str, list[dict]],
    alias_index: AliasIndex,
    *,
    fuzzy_threshold: int = 85,
) -> tuple[dict, list[Issue]]:
    """Resolve every equipment reference in every indexed unit.

    Returns:
        report: nested dict with per-unit + global statistics
        issues: list of Issue objects for every unresolved reference
    """
    issues: list[Issue] = []
    per_unit: list[dict] = []
    unresolved_counter: Counter[str] = Counter()
    structural_counter: Counter[str] = Counter()

    totals = {
        "units_with_refs": 0,
        "total_refs": 0,
        "exact": 0,
        "tech_disambiguated": 0,
        "structural": 0,
        "unresolved": 0,
    }
    by_type: dict[str, dict[str, int]] = {}

    for unit_type, records in unit_indices.items():
        by_type.setdefault(unit_type, {
            "total_refs": 0, "exact": 0, "tech_disambiguated": 0,
            "structural": 0, "unresolved": 0,
        })
        for unit in records:
            refs = unit.get("raw_equipment_refs", [])
            if not refs:
                continue
            totals["units_with_refs"] += 1
            unresolved_here: list[dict] = []
            counts = {"exact": 0, "tech_disambiguated": 0, "structural": 0, "unresolved": 0}

            for raw in refs:
                parsed = parse_reference(raw)
                cid, kind = alias_index.lookup(parsed)
                totals["total_refs"] += 1
                by_type[unit_type]["total_refs"] += 1

                if kind == "structural":
                    counts["structural"] += 1
                    totals["structural"] += 1
                    by_type[unit_type]["structural"] += 1
                    structural_counter[parsed.normalized_key] += 1
                    continue

                if cid is not None:
                    key = kind.replace("-", "_")
                    counts[key] += 1
                    totals[key] += 1
                    by_type[unit_type][key] += 1
                    continue

                # unresolved -- gather fuzzy suggestions
                suggestions = alias_index.fuzzy_suggest(parsed, score_cutoff=fuzzy_threshold)
                counts["unresolved"] += 1
                totals["unresolved"] += 1
                by_type[unit_type]["unresolved"] += 1
                unresolved_counter[raw] += 1
                unresolved_here.append({
                    "raw": raw,
                    "normalized": parsed.normalized_key,
                    "tech_base": parsed.tech_base,
                    "fuzzy_suggestions": [
                        {"canonical_id": cid_, "matched_key": mk, "score": score}
                        for cid_, mk, score in suggestions
                    ],
                })
                issues.append(Issue(
                    "warning" if suggestions else "error",
                    "unresolved-equipment",
                    unit["source_path"],
                    f"unresolved equipment reference: {raw!r}",
                    {
                        "unit_key": unit["key"],
                        "unit_type": unit_type,
                        "raw": raw,
                        "fuzzy_suggestions": [
                            {"canonical_id": cid_, "matched_key": mk, "score": score}
                            for cid_, mk, score in suggestions
                        ],
                    },
                ))

            per_unit.append({
                "unit_type": unit_type,
                "key": unit["key"],
                "chassis": unit.get("chassis"),
                "model": unit.get("model"),
                "source_path": unit["source_path"],
                "counts": counts,
                "unresolved": unresolved_here,
            })

    by_type_report = {}
    for ut, t in by_type.items():
        by_type_report[ut] = {
            **t,
            "resolution_rate": _safe_pct(
                t["exact"] + t["tech_disambiguated"],
                t["total_refs"] - t["structural"],
            ),
            "unresolved_pct": round(
                100.0 * t["unresolved"] / max(1, t["total_refs"] - t["structural"]), 3
            ),
        }

    report = {
        "totals": totals,
        "resolution_rate": _safe_pct(
            totals["exact"] + totals["tech_disambiguated"],
            totals["total_refs"] - totals["structural"],
        ),
        "by_type": by_type_report,
        "top_unresolved": unresolved_counter.most_common(50),
        "top_structural": structural_counter.most_common(20),
        "per_unit": per_unit,
    }
    return report, issues


def _safe_pct(num: int, denom: int) -> float:
    if denom <= 0:
        return 100.0
    return round(100.0 * num / denom, 3)


# --- Quirks / factions / eras ---------------------------------------------

def resolve_quirks(unit_indices: dict[str, list[dict]], reference: dict) -> tuple[dict, list[Issue]]:
    quirks_ref = reference.get("quirk_names", {}) or {}
    known: set[str] = set()
    for section in ("positive", "negative", "weapon_quirks"):
        section_data = quirks_ref.get(section) or {}
        if isinstance(section_data, dict):
            known.update(section_data.values())

    issues: list[Issue] = []
    unknown = Counter()
    total = 0
    for records in unit_indices.values():
        for unit in records:
            for q in unit.get("raw_quirks") or []:
                if not isinstance(q, str):
                    continue
                total += 1
                # quirks are sometimes "Battle Fists LA" while ref has "Battle Fists LA" -- exact match
                # Strip trailing location suffixes (LA/RA/LL/RL/LT/RT/CT/HD) when looking up
                bare = _strip_location_suffix(q)
                if q in known or bare in known:
                    continue
                # Some quirks include a numeric suffix matching the ref ("Weak Head Armor 1")
                unknown[q] += 1
                issues.append(Issue(
                    "warning", "unknown-quirk", unit["source_path"],
                    f"quirk not in reference: {q!r}",
                    {"unit_key": unit["key"], "quirk": q},
                ))
    return {"total": total, "unknown_count": sum(unknown.values()), "top_unknown": unknown.most_common(20)}, issues


def _strip_location_suffix(q: str) -> str:
    parts = q.rsplit(" ", 1)
    if len(parts) == 2 and parts[1] in {"LA", "RA", "LL", "RL", "LT", "RT", "CT", "HD"}:
        return parts[0]
    return q


def resolve_eras(unit_indices: dict[str, list[dict]], reference: dict) -> tuple[dict, list[Issue]]:
    eras = reference.get("eras") or []
    if not isinstance(eras, list) or not eras:
        return {"checked": False}, []
    spans = []
    for e in eras:
        if isinstance(e, dict) and "startYear" in e and "endYear" in e:
            spans.append((int(e["startYear"]), int(e["endYear"]), e.get("name", "")))
    issues: list[Issue] = []
    out_of_range = 0
    total = 0
    for records in unit_indices.values():
        for unit in records:
            yr = unit.get("era")
            if yr is None:
                continue
            try:
                yr = int(yr)
            except (TypeError, ValueError):
                continue
            total += 1
            if not any(s <= yr <= e for s, e, _ in spans):
                out_of_range += 1
                issues.append(Issue(
                    "info", "era-gap", unit["source_path"],
                    f"unit year {yr} falls outside known era spans",
                    {"unit_key": unit["key"], "year": yr},
                ))
    return {"checked": True, "total_with_year": total, "out_of_range": out_of_range}, issues


def resolve_ammo_links(equipment_records: list[dict]) -> tuple[dict, list[Issue]]:
    """Verify every ammo entry's `weapon_ref` matches some weapon's mtf_reference or display."""
    issues: list[Issue] = []
    weapon_keys: set[str] = set()
    for rec in equipment_records:
        if rec.get("category") in ("ballistic", "energy", "missile", "physical"):
            for fld in ("display_name", "mtf_reference"):
                v = rec.get(fld)
                if isinstance(v, str):
                    weapon_keys.add(v.casefold())
                    # also strip "Inner Sphere "/"Clan " prefix
                    for pfx in ("inner sphere ", "clan "):
                        if v.casefold().startswith(pfx):
                            weapon_keys.add(v.casefold()[len(pfx):])

    unmatched = 0
    matched = 0
    for rec in equipment_records:
        if rec.get("category") != "ammunition":
            continue
        wref = rec.get("weapon_ref")
        if not isinstance(wref, str):
            continue
        if wref.casefold() in weapon_keys:
            matched += 1
        else:
            unmatched += 1
            issues.append(Issue(
                "warning", "ammo-orphan", rec["source_path"],
                f"ammo {rec['display_name']!r} weapon_ref {wref!r} has no matching weapon",
                {"canonical_id": rec["canonical_id"], "weapon_ref": wref},
            ))
    return {"matched": matched, "unmatched": unmatched}, issues
