"""Making functions for ex05."""

__author__ = "730307805"


def only_evens(numbers: list[int]) -> list[int]:
    """This function will return a list of even items."""
    evens: list[int] = list()
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """This function will return a list within the given index, not including the last index."""
    product: list[int] = []
    if start < 0:
        start = 0
    
    i: int = start
    
    if a_list == []:
        return product
    
    if start > end:
        return product

    if end <= 0:
        return product
    
    while i <= end:
        index = a_list[i]
        product.append(index)
        i += 1
    product.pop(len(product) - 1)
    return product


def concat(a: list[int], b: list[int]) -> list[int]:
    """This function will combine two lists."""
    final_list: list[int] = a

    for item in b:
        final_list.append(item)
    
    return final_list
