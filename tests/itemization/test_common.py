"""Tests for itemization.common helpers."""
from __future__ import annotations

import math

from src.itemization.common import (
    categorical_counts,
    histogram,
    percentile,
    summarize,
    to_float,
    to_int,
)


class TestToFloat:
    def test_int(self):
        assert to_float(5) == 5.0

    def test_float(self):
        assert to_float(3.5) == 3.5

    def test_string_numeric(self):
        assert to_float("12.5") == 12.5

    def test_string_with_units(self):
        assert to_float("12 tons") == 12.0

    def test_na_strings(self):
        assert to_float("NA") is None
        assert to_float("N/A") is None
        assert to_float("variable") is None
        assert to_float("-") is None

    def test_none_and_empty(self):
        assert to_float(None) is None
        assert to_float("") is None

    def test_bool_rejected(self):
        assert to_float(True) is None
        assert to_float(False) is None

    def test_nan_rejected(self):
        assert to_float(float("nan")) is None

    def test_to_int_truncates(self):
        assert to_int("3.7") == 3
        assert to_int(None) is None


class TestPercentile:
    def test_empty(self):
        assert math.isnan(percentile([], 50))

    def test_single(self):
        assert percentile([4.0], 50) == 4.0

    def test_median(self):
        assert percentile([1.0, 2.0, 3.0], 50) == 2.0

    def test_min_max(self):
        v = sorted([1.0, 2.0, 3.0, 4.0, 5.0])
        assert percentile(v, 0) == 1.0
        assert percentile(v, 100) == 5.0


class TestHistogram:
    def test_basic(self):
        h = histogram([0.5, 1.5, 1.8, 2.5], bin_width=1.0)
        assert h[0] == {"lo": 0.0, "hi": 1.0, "count": 1}
        assert h[1] == {"lo": 1.0, "hi": 2.0, "count": 2}
        assert h[2] == {"lo": 2.0, "hi": 3.0, "count": 1}


class TestSummarize:
    def test_empty(self):
        assert summarize([]) == {"count": 0}
        assert summarize([None, "NA", ""]) == {"count": 0}

    def test_basic_stats(self):
        s = summarize([1, 2, 3, 4, 5])
        assert s["count"] == 5
        assert s["min"] == 1
        assert s["max"] == 5
        assert s["mean"] == 3.0
        assert s["median"] == 3.0

    def test_with_histogram(self):
        s = summarize([1, 2, 3, 4, 5], bin_width=2.0)
        assert "histogram" in s
        assert sum(b["count"] for b in s["histogram"]) == 5

    def test_mixed_types(self):
        s = summarize(["1", 2, "3.5", "NA", None])
        assert s["count"] == 3


class TestCategoricalCounts:
    def test_drops_empty(self):
        c = categorical_counts(["a", "b", "a", None, "", "b"])
        assert c == {"a": 2, "b": 2}

    def test_sorted_by_count(self):
        c = categorical_counts(["a", "b", "a", "a", "b", "c"])
        assert list(c.keys()) == ["a", "b", "c"]
