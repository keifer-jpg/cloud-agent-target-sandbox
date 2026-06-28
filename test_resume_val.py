"""Tests for resume_val module (Phase 1 reset validation)."""

import pytest
from resume_val import clamp, double


def test_clamp():
    # value inside range
    assert clamp(5, 0, 10) == 5
    # value below range — clamped to low
    assert clamp(-3, 0, 10) == 0
    # value above range — clamped to high
    assert clamp(42, 0, 10) == 10
    # invalid range raises ValueError
    with pytest.raises(ValueError):
        clamp(1, 5, 0)


def test_resume_kill_window():
    import time; time.sleep(120)
    assert True


def test_double():
    assert double(3) == 6
    assert double(-4) == -8
