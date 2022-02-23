"""Testing the functions defined for ex05."""

__author__ = "703037805"

from utils import only_evens, sub, concat


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


def test_sub_nolist() -> None:
    """Testing the sub function when there is no list given."""
    a_list: list[int] = []
    assert sub(a_list, 1, 3) == []


def test_sub_negative() -> None:
    """Testing the sub function when there is a negative start index given."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, -5, 3) == [10, 20, 30]


def test_sub_zero() -> None:
    """Testing the sub function when there is an end index of zero."""
    a_list: list = [10, 20, 30, 40]
    assert sub(a_list, 1, 0) == []


def test_concat_empty() -> None:
    """Testing the function concat when both lists are empty."""
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == []


def test_concat_duplicate() -> None:
    """Testing the concat function with duplicate list."""
    a: list[int] = [1, 2, 3, 4, 5]
    b: list[int] = [1, 2, 3, 4, 5]
    assert concat(a, b) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


def test_concat_random() -> None:
    """Testing the concat function with a singular item in one list."""
    a: list[int] = [1]
    b: list[int] = [40284, 203984, 3, 4, 3]
    assert concat(a, b) == [1, 40284, 203984, 3, 4, 3]