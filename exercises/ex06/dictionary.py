"""Creating dictionaries for exercise 06."""

__author__ = "730307805"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, returns a dictionary where the keys and values are inverted."""
    result: dict[str, str] = {}
    for key in a:
        new_key: str = a[key]
        result[new_key] = key
    return result
    # How do I assert a KeyError??


def favorite_color(a: dict[str, str]) -> str:
    """This function will return the color that appears most frequently in the dictionary."""
    # need to create a dictionary that has [color: # of times]
    score: dict[str, int] = {}
    for key in a:
        color: str = a[key]
        score[color] = 1
        if color in score:
            score[color] += 1
        # need to insert some kind of if-else statement that makes sure if there's a tie, the value printed is the one that showed up first in the dictionary
    popular: str = f'{max(score)}'
    return popular  # to return the color that shows up the most


def count(a: list[str]) -> dict[str, int]:
    """This function will take a list of items and tell us how many times an item shows up in the function."""
    dictionary: dict[str, int] = {}

    return dictionary