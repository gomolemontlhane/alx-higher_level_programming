#!/usr/bin/python3
"""
Function to replace all occurrences of an element in a new list
"""


def search_replace(my_list, search, replace):
    """Return a new list with replaced elements"""
    new_list = [replace if elem == search else elem for elem in my_list]
    return new_list
