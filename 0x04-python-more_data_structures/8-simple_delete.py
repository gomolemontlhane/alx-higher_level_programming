#!/usr/bin/python3
"""
Function to delete a key in a dictionary
"""


def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary if it exists"""
    a_dictionary.pop(key, None)
    return a_dictionary
