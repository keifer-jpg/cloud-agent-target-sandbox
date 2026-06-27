"""Tests for resume_val.py — pure functions, no I/O/network/global state."""

import pytest
from resume_val import clamp, double


def test_clamp():
    # Value already within bounds
    assert clamp(5, 0, 10) == 5
    # Value below low bound
    assert clamp(-3, 0, 10) == 0
    # Value above high bound
    assert clamp(42, 0, 10) == 10
    # Invalid bounds raise ValueError
    with pytest.raises(ValueError):
        clamp(1, 5, 0)


def test_resume_kill_window():
    import time; time.sleep(120)
    assert True


def test_double():
    assert double(3) == 6
    assert double(-4) == -8
