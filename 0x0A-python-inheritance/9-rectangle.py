#!/usr/bin/python3
from 8-rectangle import Rectangle

class Rectangle(Rectangle):
    """A class representing a rectangle."""

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height


    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
