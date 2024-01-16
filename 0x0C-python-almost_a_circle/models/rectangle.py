#!/usr/bin/python3
"""Module for the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class, a subclass of Base.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): X-coordinate of the rectangle.
        __y (int): Y-coordinate of the rectangle.

    Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): X-coordinate of the rectangle.
        y (int): Y-coordinate of the rectangle.
        id (int): An optional parameter to set the instance id. If not provided,
            a unique id is assigned.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Initializes a Rectangle instance.
        __str__(self): Returns a string representation of the Rectangle.
        update(self, *args, **kwargs): Updates the attributes of the Rectangle.
        to_dictionary(self): Returns a dictionary representation of the Rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    @property
    def width
