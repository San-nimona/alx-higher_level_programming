#!/usr/bin/python3
"""4-from_json_string.py"""


def from_json_string(my_str):
    """a function that returns an object (Python data structure)\
            represented by a JSON string

    Args:
        my_str: a string
    """
    import json
    return json.loads(my_str)
