"""Pure utility functions for the GLM validation sandbox."""


def clamp(value, low, high):
    """Return value bounded to the inclusive [low, high] range.

    Args:
        value: The number to clamp.
        low: Lower bound (inclusive).
        high: Upper bound (inclusive).

    Returns:
        The clamped value.

    Raises:
        ValueError: If low > high.
    """
    if low > high:
        raise ValueError(f"low ({low}) > high ({high})")
    return max(low, min(value, high))
