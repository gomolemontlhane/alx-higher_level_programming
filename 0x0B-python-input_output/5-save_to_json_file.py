#!/usr/bin/python3
"""Save Object to a file module"""

import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using its JSON representation"""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
