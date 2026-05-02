"""Generate output/point-assessment.md from cached BV data."""
import json
import math
import os
import sys

# ---- Load ----
bv_cache = json.load(open("output/bv_cache.json", encoding="utf-8"))
mech_idx = json.load(open("data/index/mech_index.json", encoding="utf-8"))
veh_idx  = json.load(open("data/index/vehicle_index.json", encoding="utf-8"))
aero_idx = json.load(open("data/index/aerospace_index.json", encoding="utf-8"))
dets_m   = json.load(open("output/detachments/detachments_mech.json", encoding="utf-8"))
dets_v   = json.load(open("output/detachments/detachments_vehicle.json", encoding="utf-8"))
dets_a   = json.load(open("output/detachments/detachments_aerospace.json", encoding="utf-8"))

# canonical_id -> mul_id
cid_to_mul: dict[str, str] = {}
for rec in mech_idx + veh_idx + aero_idx:
    cid = rec.get("canonical_id")
    mul = rec.get("mul_id")
    if cid and mul:
        cid_to_mul[cid] = str(mul)


def get_bv(cid: str) -> int | None:
    mul = cid_to_mul.get(cid)
    if not mul:
        return None
    v = bv_cache.get(mul)
    return v if v else None  # treat 0 / None as "not published"


def pct(bv: int | None, p: int) -> str:
    if bv is None:
        return "—"
    return str(math.floor(bv * p / 100))


def make_table(detachments: list, label: str) -> tuple[str, int | None, int | None, int, int]:
    rows = []
    for d in detachments:
        bv = get_bv(d["id"])
        rows.append({
            "affiliation": d["tech_base"],
            "name": d["name"],
            "bv": bv,
        })
    rows.sort(key=lambda r: (r["affiliation"], r["name"]))

    valid_bvs = [r["bv"] for r in rows if r["bv"]]
    mn = min(valid_bvs) if valid_bvs else None
    mx = max(valid_bvs) if valid_bvs else None
    n_valid = len(valid_bvs)
    n_total = len(rows)

    lines = [
        f"## {label}",
        "",
        f"**{n_total} units** | BV range: {mn} \u2013 {mx} "
        f"(units with published BV: {n_valid}/{n_total})",
        "",
        "| Affiliation | Name | BV | 75% BV | 50% BV | 25% BV |",
        "|-------------|------|----|--------|--------|--------|",
    ]
    for r in rows:
        bv = r["bv"]
        bv_s = str(bv) if bv else "\u2014"
        lines.append(
            f"| {r['affiliation']} | {r['name']} | {bv_s} "
            f"| {pct(bv, 75)} | {pct(bv, 50)} | {pct(bv, 25)} |"
        )
    return "\n".join(lines), mn, mx, n_valid, n_total


mech_md, mech_mn, mech_mx, mech_n, mech_t = make_table(dets_m, "BattleMechs")
veh_md,  veh_mn,  veh_mx,  veh_n,  veh_t  = make_table(dets_v, "Vehicles")
aero_md, aero_mn, aero_mx, aero_n, aero_t = make_table(dets_a, "Aerospace Fighters")

all_bvs = sorted(
    bv
    for ds in [dets_m, dets_v, dets_a]
    for d in ds
    for bv in [get_bv(d["id"])]
    if bv
)
overall_min = all_bvs[0]
overall_max = all_bvs[-1]
overall_med = all_bvs[len(all_bvs) // 2]
total_units = mech_t + veh_t + aero_t
total_valid = mech_n + veh_n + aero_n

sections = [
    "# Point Assessment \u2014 Battle Value Analysis",
    "",
    "> Generated from Master Unit List (masterunitlist.info).  ",
    "> Purpose: calibrate initial points values across all detachments.",
    "",
    "## Summary",
    "",
    "| Metric | Value |",
    "|--------|-------|",
    f"| Total units | {total_units:,} |",
    f"| Units with published BV | {total_valid:,} ({100 * total_valid // total_units}%) |",
    f"| **Minimum BV** | **{overall_min:,}** |",
    f"| **Maximum BV** | **{overall_max:,}** |",
    f"| Median BV | {overall_med:,} |",
    "",
    "| Unit Type | Units | Min BV | Max BV | With BV |",
    "|-----------|-------|--------|--------|---------|",
    f"| BattleMechs | {mech_t:,} | {mech_mn:,} | {mech_mx:,} | {mech_n:,} |",
    f"| Vehicles | {veh_t:,} | {veh_mn:,} | {veh_mx:,} | {veh_n:,} |",
    f"| Aerospace Fighters | {aero_t:,} | {aero_mn:,} | {aero_mx:,} | {aero_n:,} |",
    "",
    "---",
    "",
    mech_md,
    "",
    "---",
    "",
    veh_md,
    "",
    "---",
    "",
    aero_md,
]

md = "\n".join(sections)
out_path = "output/point-assessment.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(md)

print(f"Wrote {out_path}  ({len(md):,} chars, {len(md.splitlines()):,} lines)")
print(f"Overall: min={overall_min}  max={overall_max}  median={overall_med}")
