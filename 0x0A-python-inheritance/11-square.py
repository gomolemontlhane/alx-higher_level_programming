#!/usr/bin/python3
"""
Module that defines the Square class, which inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.
        Validates size using integer_validator from the parent class.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
