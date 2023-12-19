#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size,
size validation, and a public instance method area.
"""


class Square:
    """
    Square class with a private instance attribute size, size validation,
    and a public instance method area.
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

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
