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
