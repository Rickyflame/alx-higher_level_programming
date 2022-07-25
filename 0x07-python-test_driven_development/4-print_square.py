#!/usr/bin/python3
"""defines a square printing function"""


def print_square(size):
    """Print a square with the # character
    Args:
    size (int): the height and width of the square
    Raises:
    TypeError: if size is not an int
    ValueError: is size a float and < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
