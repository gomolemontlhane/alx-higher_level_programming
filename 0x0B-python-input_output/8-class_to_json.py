#!/usr/bin/python3
"""Class to JSON module"""


def class_to_json(obj):
    """Retrns dictionry dscriptn /w simple data strctre for JSON serilizatin"""
    return obj.__dict__
