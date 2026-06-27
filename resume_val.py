"""Pure utility for Phase 3 resume-on-crash validation.

Every function here is pure: no I/O, no network, no global state.
"""


def clamp(value, low, high):
    """Return value bounded to the inclusive [low, high] range.

    Raises ValueError if low > high.
    """
    if low > high:
        raise ValueError(f"low ({low}) must not be greater than high ({high})")
    if value < low:
        return low
    if value > high:
        return high
    return value


def double(x):
    """Return x * 2."""
    return x * 2
