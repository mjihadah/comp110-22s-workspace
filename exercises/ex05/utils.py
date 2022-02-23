"""Making functions for ex05."""

__author__ = "730307805"


def only_evens(numbers: list[int]) -> list[int]:
    """This function will return a list of even items."""
    evens: list[int] = list()
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens