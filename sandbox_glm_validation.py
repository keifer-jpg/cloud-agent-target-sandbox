"""Pure functions for the GLM cross-model reviewer validation.

This module contains self-contained, pure functions with no I/O, no network,
and no global state — used to exercise the new review architecture.
"""


def clamp(value, low, high):
    """Return value bounded to the inclusive [low, high] range.

    Args:
        value: The value to clamp.
        low: The lower bound (inclusive).
        high: The upper bound (inclusive).

    Returns:
        value clamped to [low, high].

    Raises:
        ValueError: If low > high.
    """
    if low > high:
        raise ValueError(
            f"low ({low}) must not be greater than high ({high})"
        )
    if value < low:
        return low
    if value > high:
        return high
    return value
