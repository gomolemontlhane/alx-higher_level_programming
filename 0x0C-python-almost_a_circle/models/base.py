#!/usr/bin/python3
"""Module for the Base class."""
class Base:
    """The Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
