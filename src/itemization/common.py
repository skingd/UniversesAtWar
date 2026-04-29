"""Shared helpers: numeric coercion and statistical summaries."""
from __future__ import annotations

import json
import math
import re
import statistics
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Sequence


# --- Numeric coercion ------------------------------------------------------

_NUM_RE = re.compile(r"-?\d+(?:\.\d+)?")


def to_float(value: Any) -> float | None:
    """Best-effort numeric coercion. Returns None for missing / non-numeric."""
    if value is None:
        return None
    if isinstance(value, bool):  # bools are ints in Python; reject
        return None
    if isinstance(value, (int, float)):
        if isinstance(value, float) and math.isnan(value):
            return None
        return float(value)
    if isinstance(value, str):
        s = value.strip()
        if not s or s.upper() in ("NA", "N/A", "VARIABLE", "SPECIAL", "-"):
            return None
        try:
            return float(s)
        except ValueError:
            m = _NUM_RE.search(s)
            return float(m.group(0)) if m else None
    return None


def to_int(value: Any) -> int | None:
    f = to_float(value)
    return int(f) if f is not None else None


# --- Statistical summary ---------------------------------------------------

def percentile(sorted_values: Sequence[float], pct: float) -> float:
    """Linear-interpolation percentile (matches numpy default).

    `sorted_values` MUST already be sorted ascending. `pct` in [0, 100].
    """
    n = len(sorted_values)
    if n == 0:
        return float("nan")
    if n == 1:
        return float(sorted_values[0])
    rank = (pct / 100.0) * (n - 1)
    lo = int(math.floor(rank))
    hi = int(math.ceil(rank))
    if lo == hi:
        return float(sorted_values[lo])
    frac = rank - lo
    return float(sorted_values[lo] + (sorted_values[hi] - sorted_values[lo]) * frac)


def histogram(values: Iterable[float], bin_width: float) -> list[dict]:
    """Bucket values into uniform-width bins. Returns list of
    `{lo, hi, count}` ascending by `lo`."""
    if bin_width <= 0:
        raise ValueError("bin_width must be > 0")
    buckets: Counter[int] = Counter()
    for v in values:
        idx = int(math.floor(v / bin_width))
        buckets[idx] += 1
    if not buckets:
        return []
    lo_idx = min(buckets)
    hi_idx = max(buckets)
    return [
        {
            "lo": round(i * bin_width, 6),
            "hi": round((i + 1) * bin_width, 6),
            "count": buckets.get(i, 0),
        }
        for i in range(lo_idx, hi_idx + 1)
    ]


def summarize(
    raw_values: Iterable[Any],
    *,
    bin_width: float | None = None,
) -> dict:
    """Build the standard distribution block used everywhere in Part 2.

    Returns `{count, min, max, mean, median, std, p10, p25, p50, p75, p90,
              p95, p99, histogram?}`. Non-numeric / None values are skipped.
    Returns an empty `{count: 0}` block when no numeric values are present.
    """
    coerced: list[float] = []
    for v in raw_values:
        f = to_float(v)
        if f is not None:
            coerced.append(f)
    n = len(coerced)
    if n == 0:
        return {"count": 0}
    coerced.sort()
    out = {
        "count": n,
        "min": coerced[0],
        "max": coerced[-1],
        "mean": round(statistics.fmean(coerced), 4),
        "median": round(statistics.median(coerced), 4),
        "std": round(statistics.pstdev(coerced), 4) if n > 1 else 0.0,
        "p10": round(percentile(coerced, 10), 4),
        "p25": round(percentile(coerced, 25), 4),
        "p50": round(percentile(coerced, 50), 4),
        "p75": round(percentile(coerced, 75), 4),
        "p90": round(percentile(coerced, 90), 4),
        "p95": round(percentile(coerced, 95), 4),
        "p99": round(percentile(coerced, 99), 4),
    }
    if bin_width:
        out["histogram"] = histogram(coerced, bin_width)
    return out


def categorical_counts(values: Iterable[Any]) -> dict[str, int]:
    """Return a sorted-by-count dict of value -> occurrences. None is dropped."""
    c: Counter[str] = Counter()
    for v in values:
        if v is None or v == "":
            continue
        c[str(v)] += 1
    return dict(c.most_common())


# --- IO --------------------------------------------------------------------

def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False),
        encoding="utf-8",
    )


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))
