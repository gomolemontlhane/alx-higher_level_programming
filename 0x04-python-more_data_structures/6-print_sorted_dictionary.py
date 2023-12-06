#!/usr/bin/python3
"""
Function to print a dictionary by ordered keys
"""


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys"""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
