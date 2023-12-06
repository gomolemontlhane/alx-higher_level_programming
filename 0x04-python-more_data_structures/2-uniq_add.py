#!/usr/bin/python3
"""
Function to add all unique integers in a list
"""


def uniq_add(my_list=[]):
    """Return the sum of unique integers in the list"""
    return sum(set(my_list))
