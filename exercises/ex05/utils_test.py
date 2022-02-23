"""Testing the functions defined for ex05."""

__author__ = "703037805"

from utils import only_evens


def test_only_evens_odds() -> None:
    """Testing only_evens with only odd numbers."""
    numbers: list[int] = [1, 3, 5, 7]
    assert only_evens(numbers) == []


def test_only_evens_mixed() -> None:
    """Testing the only evens function with a mix of even and odd numbers."""
    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(numbers) == [2, 4, 6]


def test_only_evens_bignums() -> None:
    """Testing the only even function with big numbers."""
    numbers: list[int] = [39023, 484090, 2103809, 934280]
    assert only_evens(numbers) == [484090, 934280]