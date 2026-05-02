"""CLI: render detachment JSON outputs into HTML cards.

Usage:
    python -m src.cards
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from src.cards.render import render_page, CARD_SIZES, _DEFAULT_SIZE
from src.detachments.weapons import (
    load_ammunition_rules,
    load_weapon_rules,
)


_DETACHMENT_FILES: dict[str, tuple[str, str]] = {
    # type-key -> (input filename, page title)
    "mech":      ("detachments_mech.json",      "BattleMech Detachments"),
    "vehicle":   ("detachments_vehicle.json",   "Vehicle Detachments"),
    "aerospace": ("detachments_aerospace.json", "Aerospace Detachments"),
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="uaw-cards",
        description="Render detachment JSONs into stylized HTML card pages.",
    )
    parser.add_argument("--detachments-dir", type=Path,
        default=Path("output/detachments"),
        help="Directory holding detachments_<type>.json (default: output/detachments).")
    parser.add_argument("--weapon-rules", type=Path,
        default=Path("data/WeaponRules.csv"),
        help="WeaponRules.csv path.")
    parser.add_argument("--ammo-rules", type=Path,
        default=Path("data/AmmunitionRules.csv"),
        help="AmmunitionRules.csv path.")
    parser.add_argument("--output-dir", type=Path,
        default=Path("output/cards"),
        help="Where to write cards_<type>.html (default: output/cards).")
    parser.add_argument("--types", nargs="+", default=["mech", "vehicle", "aerospace"],
        choices=["mech", "vehicle", "aerospace"],
        help="Which unit types to render.")
    parser.add_argument("--card-size", default=_DEFAULT_SIZE,
        choices=list(CARD_SIZES.keys()),
        help=f"Physical card size for printing (default: {_DEFAULT_SIZE}). "
             "Options: " + ", ".join(f"{k} ({v[0]}\u00d7{v[1]})" for k, v in CARD_SIZES.items()))
    parser.add_argument("--limit", type=int, default=None,
        help="Render only the first N detachments per type (smoke test).")
    args = parser.parse_args(argv)

    if not args.weapon_rules.exists():
        print(f"ERROR: {args.weapon_rules} not found", file=sys.stderr)
        return 2
    if not args.ammo_rules.exists():
        print(f"ERROR: {args.ammo_rules} not found", file=sys.stderr)
        return 2

    print(f"[cards] loading weapon profiles: {args.weapon_rules}")
    profiles = {p.name: p for p in load_weapon_rules(args.weapon_rules)}
    print(f"[cards]   {len(profiles)} weapon profiles")

    print(f"[cards] loading ammo: {args.ammo_rules}")
    ammo_index = load_ammunition_rules(args.ammo_rules)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    for utype in args.types:
        in_name, title = _DETACHMENT_FILES[utype]
        in_path = args.detachments_dir / in_name
        if not in_path.exists():
            print(f"[cards] SKIP {utype}: {in_path} not found", file=sys.stderr)
            continue
        with open(in_path, "r", encoding="utf-8") as f:
            detachments = json.load(f)
        if args.limit is not None:
            detachments = detachments[: args.limit]
        # Sort by tech_base then name for stable, browseable output.
        detachments.sort(key=lambda d: ((d.get("tech_base") or ""), (d.get("name") or "")))

        html_doc = render_page(title, detachments, profiles, ammo_index, args.card_size)
        out_file = args.output_dir / f"cards_{utype}.html"
        out_file.write_text(html_doc, encoding="utf-8")
        print(f"[cards] wrote {len(detachments):>4} cards -> {out_file} "
              f"({out_file.stat().st_size:,} bytes)")

    return 0
