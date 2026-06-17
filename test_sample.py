"""Tiny green test suite for the orchestrator's throwaway target repo.
Used to prove the build->test pipeline end to end. Keep the base GREEN.
"""

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(2, 3) == 6


def test_strings():
    assert "cloud" + "-agent" == "cloud-agent"
