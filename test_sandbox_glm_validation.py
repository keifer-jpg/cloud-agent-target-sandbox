"""Tests for sandbox_glm_validation — Phase 1 clamp() and Phase 2 chunk() functions."""

import pytest
from sandbox_glm_validation import clamp, chunk


def test_clamp_value_within_range():
    """Value already inside the range is returned unchanged."""
    assert clamp(5, 0, 10) == 5


def test_clamp_value_below_range():
    """Value below the low bound is clamped up to low."""
    assert clamp(-1, 0, 10) == 0


def test_clamp_value_above_range():
    """Value above the high bound is clamped down to high."""
    assert clamp(99, 0, 10) == 10


def test_clamp_value_at_low_bound():
    """Value equal to low bound is returned unchanged."""
    assert clamp(0, 0, 10) == 0


def test_clamp_value_at_high_bound():
    """Value equal to high bound is returned unchanged."""
    assert clamp(10, 0, 10) == 10


def test_clamp_low_greater_than_high_raises_value_error():
    """When low > high, a ValueError is raised."""
    with pytest.raises(ValueError):
        clamp(5, 10, 0)


# ---------------------------------------------------------------------------
# Phase 2 — chunk()
# ---------------------------------------------------------------------------


def test_chunk_standard_list():
    """A non-empty list is split into consecutive sublists of the given size."""
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunk_empty_list():
    """An empty list produces an empty list."""
    assert chunk([], 3) == []


def test_chunk_size_lt_one_raises_value_error():
    """chunk raises ValueError when size < 1."""
    with pytest.raises(ValueError):
        chunk([1, 2, 3], 0)
    with pytest.raises(ValueError):
        chunk([1, 2, 3], -1)
