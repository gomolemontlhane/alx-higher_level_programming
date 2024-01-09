#!/usr/bin/python3
"""
Module that defines the Rectangle class, which inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with a given width and height.
        Validates width and height using integer_validator from the parent class.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes and returns the area of the rectangle.
        """
        return self.__width * self.__height


    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
