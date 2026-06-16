"""Tiny green test suite for the orchestrator's throwaway target repo.
Used to prove the build->test pipeline end to end. Keep the base GREEN.
"""

def add(a, b):
    return a + b


def count_vowels(s):
    return sum(1 for ch in s if ch in "aeiouAEIOU")


def test_add():
    assert add(2, 3) == 5


def test_strings():
    assert "cloud" + "-agent" == "cloud-agent"


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("") == 0
