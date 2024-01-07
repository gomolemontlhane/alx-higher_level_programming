#!/usr/bin/python3
"""
Module for adding two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
        a (int): The first integer.
        b (int): The second integer (default is 98).

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
