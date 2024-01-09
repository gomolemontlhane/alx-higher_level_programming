#!/usr/bin/python3
from 9-rectangle import Rectangle

class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initializes a Square instance with a specified size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)


    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
