"""CLI for `uaw-base-ranges`."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .compute import UNIT_TYPE_CONFIG, compute_all, required_field_counts
from .reporter import write_report


def _load_index(index_dir: Path, unit_type: str) -> list[dict] | None:
    p = index_dir / f"{unit_type}_index.json"
    if not p.exists():
        return None
    with p.open(encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get("records"), list):
        return data["records"]
    raise ValueError(f"unrecognised index format: {p}")


def _check_strict(indices: dict[str, list[dict]]) -> list[str]:
    """Return error messages for unit types where required fields are
    completely absent (signals the index pre-dates Phase 1)."""
    problems: list[str] = []
    for ut, records in indices.items():
        if not records:
            continue
        counts = required_field_counts(records, ut)
        for field, c in counts.items():
            if c == 0:
                problems.append(
                    f"{ut}: field '{field}' is missing from every record "
                    f"({len(records)} records). Re-run `uaw-datacheck` to "
                    f"rebuild the index with base stats."
                )
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="uaw-base-ranges",
        description=(
            "Distill per-unit-type base movement and armor ranges from the "
            "canonical indices. Read-only."
        ),
    )
    parser.add_argument("--index-dir", type=Path, default=Path("data/index"))
    parser.add_argument("--output-dir", type=Path, default=Path("output/base-value-ranges"))
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if any unit type has zero records with the required fields.",
    )
    args = parser.parse_args(argv)

    indices: dict[str, list[dict]] = {}
    for ut in UNIT_TYPE_CONFIG:
        recs = _load_index(args.index_dir, ut)
        if recs is not None:
            indices[ut] = recs

    if not indices:
        print(f"error: no indices found under {args.index_dir}", file=sys.stderr)
        return 2

    if args.strict:
        problems = _check_strict(indices)
        if problems:
            for msg in problems:
                print(f"strict: {msg}", file=sys.stderr)
            return 3

    report = compute_all(indices)
    json_path, md_path = write_report(report, args.output_dir)

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    for ut, block in sorted(report.items()):
        n = block["overall"].get("n", 0)
        print(f"  {ut}: {n} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
