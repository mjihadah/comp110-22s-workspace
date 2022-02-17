"""Tests for the sum function."""


from lessons.sum import sum


def test_sum_empty() -> None:
    """Testing the sum function."""
    xs: list[float] = []
    assert sum(xs) == 0.0

def test_sum_single_item() -> None:
    """Testing the sum functino with one item."""
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0

def test_sum_many_items() -> None:
    """Testing the sum functions with many items."""
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0