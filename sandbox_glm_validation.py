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


def chunk(items, size):
    """Split a list into consecutive sublists of ``size`` length.

    The final sublist may be shorter than ``size``.  The input list is never
    mutated — a new list of sublists is always returned.

    Args:
        items: The list to split.
        size: The maximum length of each sublist.

    Returns:
        A list of consecutive sublists, each of length ``size`` except for
        possibly the last.

    Raises:
        ValueError: If ``size`` is less than 1.
    """
    if size < 1:
        raise ValueError(
            f"size must be >= 1, got {size}"
        )
    return [items[i:i + size] for i in range(0, len(items), size)]


def dedupe_preserve_order(items):
    """Return the input list with duplicates removed, preserving first-seen order.

    The input list is never mutated — a new list is always returned.

    Args:
        items: The list to deduplicate.

    Returns:
        A new list with duplicates removed, keeping only the first occurrence
        of each value.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
