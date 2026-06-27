"""Tests for sandbox_glm_validation module."""

import pytest

from sandbox_glm_validation import chunk, clamp


def test_clamp_within_range():
    """Value within [low, high] is returned unchanged."""
    assert clamp(5, 0, 10) == 5


def test_clamp_below_range():
    """Value below low is raised to low."""
    assert clamp(-1, 0, 10) == 0


def test_clamp_above_range():
    """Value above high is lowered to high."""
    assert clamp(99, 0, 10) == 10


def test_clamp_invalid_range_raises():
    """low > high raises ValueError."""
    with pytest.raises(ValueError):
        clamp(5, 10, 0)


def test_chunk_even_split():
    """Even split: [1,2,3,4,5] with size 2 -> [[1,2],[3,4],[5]]."""
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunk_empty_list():
    """Empty list returns empty list for any valid size."""
    assert chunk([], 3) == []


def test_chunk_size_lt_1_raises():
    """size < 1 raises ValueError."""
    with pytest.raises(ValueError):
        chunk([1, 2, 3], 0)
