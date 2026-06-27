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


def chunk(items, size):
    """Split a list into consecutive sublists of length `size`.

    Args:
        items: The list to split.
        size: The chunk size (must be >= 1).

    Returns:
        A list of sublists, each of length `size` except possibly the last.

    Raises:
        ValueError: If size < 1.
    """
    if size < 1:
        raise ValueError(f"size must be >= 1, got {size}")
    return [items[i : i + size] for i in range(0, len(items), size)]
