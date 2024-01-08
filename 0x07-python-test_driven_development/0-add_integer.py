#!/usr/bin/python3
"""Defines a function that adds two numbers"""

def add_integer(a, b=98):
    """
    Returns a combination of the two numbers a and b (default=98)

    Raises:
        TypeError if one of the arguments is not a number (Float or Int)
    """
    if not isinstance(a, int) or isinstance(a, float):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, int) or isinstance(b, float):
        raise TypeError("b must be an integer of float")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
