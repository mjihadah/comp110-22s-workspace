"""Union type give flexibility to single vars."""

from typing import Union


def log(info: Union[str, int]) -> None:
    """Info can be str or int."""
    if isinstance(info, str):
        print(f'str: {info}')
    else:
        print(f'int: {info}')


log("hello")
log(110)