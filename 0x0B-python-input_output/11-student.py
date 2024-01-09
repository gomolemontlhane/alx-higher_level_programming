#!/usr/bin/python3
"""Student module"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialization method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__
        return {attr: getattr(self, attr, None) for attr in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
