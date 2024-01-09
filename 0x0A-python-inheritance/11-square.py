#!/usr/bin/python3
from 10-square import Square

class Square(Square):
    """A class representing a square."""

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
