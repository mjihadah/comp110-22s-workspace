"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730307805"


class Simpy:
    """Simpy!"""
    values: list[float]

    def __init__(self, input: list[float]):
        """Constructor for Simpy."""
        self.values = input
    
    def __str__(self) -> str:
        """A str representation of the values list."""
        result: str = f'Simpy({self.values})'
        return result

    def fill(self, fill_value: float, reps: int) -> None:
        """Fill a simpy's values with a specific number of repeating values."""
        i: int = 0
        self.values = []
        while i < reps:
            self.values.append(fill_value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill the values attribute with a range of values, in terms of floats."""
        assert step != 0.0
        i: float = start
        self.values = [start]
        while i != (stop - step):
            i += step
            self.values.append(i)
        # if step > 0:
        #     while i < (stop - step):
        #         self.values.append(i + step)
        #         i += step
        # else:
        #     while i > (stop + step):
        #         self.values.append(i + step)
        #         i += step

    def sum(self) -> float:
        """Compute and reutrn sum of all items in values."""
        result: float = 0.0
        for item in self.values:
            result += item
        return result

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """When rhs is Simpy, will create new Simpy where each item at same index is added together. When lhs is float, will create new Simpy where float value has been added to each item."""
        end: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                end.values.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(rhs.values):
                end.values.append((self.values[i] + (rhs.values[i])))
                i += 1
        return end

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Like add, but with exponentiation."""
        end: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                end.values.append(item ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(rhs.values):
                end.values.append((self.values[i] ** rhs.values[i]))
                i += 1
        return end

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Produce a mask, based on the equality of each item in the values attribute with some other Simpy object or float value."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(rhs.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1

        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Produce a mask, based on the greater than relationship between each item in the values attribute with some other Simpy object or float value."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(rhs.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows us to use subscription notation with Simpy objects."""
        if isinstance(rhs, int):
            result: float = self.values[rhs]
            return result
        else:
            other_result: Simpy = Simpy([])
            for item in range(len(rhs)):
                if rhs[item] is True:
                    other_result.values.append(self.values[item])
            return other_result