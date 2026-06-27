"""Phase 1: cheap end-to-end validation — pure utility functions."""


def clamp(value, low, high):
    """Return *value* bounded to the inclusive [*low*, *high*] range.

    Raises ValueError if *low* > *high*.
    """
    if low > high:
        raise ValueError(f"low ({low}) must not be greater than high ({high})")
    if value < low:
        return low
    if value > high:
        return high
    return value


def chunk(items, size):
    """Split *items* into consecutive sublists of length *size*.

    The last chunk may be shorter than *size*.  Raises ValueError if
    *size* < 1.
    """
    if size < 1:
        raise ValueError(f"size ({size}) must be >= 1")
    return [items[i:i + size] for i in range(0, len(items), size)]


def dedupe_preserve_order(items):
    """Return *items* with duplicates removed, preserving first-seen order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
