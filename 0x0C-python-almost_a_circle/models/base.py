#!/usr/bin/python3
"""Module for the Base class."""
class Base:
    """The Base class.

    Attributes:
        __nb_objects (int): A class attribute to keep track of the number
            of instances created.

    Args:
        id (int): An optional parameter to set the instance id. If not provided,
            a unique id is assigned.

    Methods:
        __init__(self, id=None): Initializes a Base instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
