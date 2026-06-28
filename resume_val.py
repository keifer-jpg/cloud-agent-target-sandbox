"""Pure utility functions for resume validation (Phase 1).

This module is part of the resume-on-crash live-testing infrastructure.
Every function must be pure: no I/O, network, or global state.
"""


def clamp(value, low, high):
    """Return `value` bounded to the inclusive [low, high] range.

    Raises ValueError if low > high.
    """
    if low > high:
        raise ValueError(f"low ({low}) must be <= high ({high})")
    return max(low, min(value, high))
