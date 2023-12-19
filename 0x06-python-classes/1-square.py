#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size.
"""


class Square:
    """
    Square class with a private instance attribute size.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
