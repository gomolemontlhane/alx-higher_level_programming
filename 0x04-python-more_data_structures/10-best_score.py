#!/usr/bin/python3
"""
Function to return a key with the biggest integer value
"""


def best_score(a_dictionary):
    """Return a key with the biggest integer value"""
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
