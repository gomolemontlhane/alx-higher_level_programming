#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size
and size validation.
"""


class Square:
    """
    Square class with a private instance attribute size and size validation.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
