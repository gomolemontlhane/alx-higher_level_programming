#!/usr/bin/python3
"""
Module for text indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']

    start = 0
    for i, char in enumerate(text):
        if char in separators:
            print(text[start:i + 1].strip() + "\n")
            start = i + 1

    if start < len(text):
        print(text[start:].strip())
