"""Tests for sandbox_glm_validation — pure clamp function."""

import pytest

from sandbox_glm_validation import clamp


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
