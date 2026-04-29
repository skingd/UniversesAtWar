"""Export the distilled weapons table to a CSV with the columns needed for
generating Legions Imperialis rules.

Output columns: Weapon Name, Min, Short, Medium, Long, Heat, Damage
"""
from __future__ import annotations

import csv
import json
from pathlib import Path


SOURCE = Path(
    r"C:\Users\sking\OneDrive\Gaming\battletech\Data Files\distilled\weapons.json"
)
DEST = Path(__file__).resolve().parents[1] / "output" / "distilled" / "weapons.csv"


def _fmt(v) -> str:
    if v is None:
        return ""
    if isinstance(v, float) and v.is_integer():
        return str(int(v))
    return str(v)


def main() -> None:
    weapons = json.loads(SOURCE.read_text(encoding="utf-8-sig"))
    DEST.parent.mkdir(parents=True, exist_ok=True)

    with DEST.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Weapon Name", "Min", "Short", "Medium", "Long", "Heat", "Damage"])
        for w in sorted(weapons, key=lambda r: r.get("display_name", "")):
            writer.writerow([
                w.get("display_name", ""),
                _fmt(w.get("min_range")),
                _fmt(w.get("short_range")),
                _fmt(w.get("medium_range")),
                _fmt(w.get("long_range")),
                _fmt(w.get("heat")),
                _fmt(w.get("damage")),
            ])
    print(f"wrote {len(weapons)} rows -> {DEST}")


if __name__ == "__main__":
    main()
