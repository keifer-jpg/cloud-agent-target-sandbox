"""Tests for sandbox_glm_validation — Phase 1 clamp() function."""

import pytest
from sandbox_glm_validation import clamp


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
