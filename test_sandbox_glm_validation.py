"""Tests for sandbox_glm_validation module."""

import pytest

from sandbox_glm_validation import clamp


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
