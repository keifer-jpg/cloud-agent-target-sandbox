"""Tests for sandbox_glm_validation — pure clamp and chunk functions."""

import pytest

from sandbox_glm_validation import chunk, clamp, dedupe_preserve_order


def test_clamp_within_range():
    """Value already in range returns unchanged."""
    assert clamp(5, 0, 10) == 5


def test_clamp_below_range():
    """Value below low returns low."""
    assert clamp(-1, 0, 10) == 0


def test_clamp_above_range():
    """Value above high returns high."""
    assert clamp(99, 0, 10) == 10


def test_clamp_at_low_boundary():
    """Value exactly at low returns low."""
    assert clamp(0, 0, 10) == 0


def test_clamp_at_high_boundary():
    """Value exactly at high returns high."""
    assert clamp(10, 0, 10) == 10


def test_clamp_low_greater_than_high_raises():
    """ValueError is raised when low > high."""
    with pytest.raises(ValueError):
        clamp(5, 10, 0)


# --- chunk tests ---------------------------------------------------------


def test_chunk_exact_division():
    """List evenly divisible by size returns equal sublists."""
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunk_empty_list():
    """Empty list returns an empty list of sublists."""
    assert chunk([], 3) == []


def test_chunk_size_lt_1_raises():
    """ValueError is raised when size < 1."""
    with pytest.raises(ValueError):
        chunk([1, 2], 0)

    with pytest.raises(ValueError):
        chunk([1, 2], -1)


# --- dedupe_preserve_order tests ------------------------------------------


def test_dedupe_preserve_order_basic():
    """Duplicates are removed while preserving first-seen order."""
    assert dedupe_preserve_order([3, 1, 3, 2, 1]) == [3, 1, 2]


def test_dedupe_preserve_order_empty():
    """Empty list returns an empty list."""
    assert dedupe_preserve_order([]) == []


def test_dedupe_preserve_order_no_mutation():
    """The original input list is not mutated."""
    original = [3, 1, 3, 2, 1]
    copy = list(original)
    dedupe_preserve_order(original)
    assert original == copy
