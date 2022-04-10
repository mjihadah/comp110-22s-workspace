from __future__ import annotations

from typing import Union

class StrArray: 
    items: list[str]

    def __init__(self, items):
        """Self constructor."""
        self.items = items

    def __repr__(self) -> str:
        """Magic method, not really sure what the purpose is..."""
        return f'StrArray({self.items})'

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Add is a vectorized operation that applies to all items.
        When rhs is a str, it is concatonated to every iteme in a new StrArray.
        """
        result: list[str] = []

        if isinstance(rhs, str):
            for item in self.items:
                result.append(item + rhs)
            return StrArray(result)
        else:
            result: list[str] = []
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])

        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
print(first + "!")
print(first + " " + last)
print(first + "//" + last)