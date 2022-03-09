"""Exercise 06: Testing the dictionary functions."""

__author__ = "703307805"

from dictionary import invert, favorite_color, count


def test_invert_basic() -> None:
    """Testing the inverse function with a basic dict."""
    basic_dict: dict[str, str]
    basic_dict = {}
    basic_dict["Melia"] = "Okay"
    basic_dict["Jalen"] = "Hey"
    assert invert(basic_dict) == {"Okay": "Melia", "Hey": "Jalen"}


def test_invert_keyerror() -> None:
    """Testing to see if the invert function with a dictionary with multiple of the same values will return a key error."""
    exdict: dict[str, str] = {"Go": 'Heels!', "Tar": 'Heels!'}
    assert invert(exdict) == KeyError


def test_invert_short() -> None:
    """Testing another dctionary."""
    exdict: dict[str, str] = {"ten": "TEN"}
    assert invert(exdict) == {"TEN": "ten"}


def test_favorite_color_classex() -> None:
    """Testing the fav color function with the example from class."""
    colors: dict[str, str] = {"Melia": "yellow", "Jalen": "yellow", "Alynn": "Pink"}
    assert favorite_color(colors) == "yellow"


def test_favorite_color_none() -> None:
    """Testing the fav color function when there is no favorite. The first value in the dictionary should be returned."""
    colors: dict[str, str] = {"Melia": 'yellow', "Alynn": 'pink'}
    assert favorite_color(colors) == "yellow"


def test_favorite_color_one() -> None:
    """Testing the fav color function when there's only one color."""
    colors: dict[str, str] = {"Melia": 'yellow'}
    assert favorite_color(colors) == "yellow"


def test_count_empty() -> None:
    """Testing count function with an empty list."""
    exlist: list[str] = []
    assert count(exlist) == {}


def test_count_same_item() -> None:
    """Testing the count function with a list containing the same item repeatedly."""
    exlist: list[str] = ['comp', 'comp', 'comp']
    assert count(exlist) == {'comp': 3}


def test_count_multiple_items() -> None:
    """Testing the count function with a list of different items."""
    exlist: list[str] = ['comp', 'psyc', 'arth', 'reli', 'comp']
    assert count(exlist) == {'comp': 2, 'psyc': 1, 'arth': 1, 'reli': 1}