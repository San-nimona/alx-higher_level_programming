#!/usr/bin/python3
"""3-to_json_string.py"""


def to_json_string(my_obj):
    """a function that returns the JSON representation of an object (string)

    Args:
        my_obj
    """
    import json
    return json.dumps(my_obj)
