#!/usr/bin/python3
"""Defines an addition integer function"""


def add_integer(a, b=98):
    """Returns the addition of a and b
    float integers are typecasted to an int before addition
    Raises:
        TypeError: if either a or b is not an integer or float
    """
    if(not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if(not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
