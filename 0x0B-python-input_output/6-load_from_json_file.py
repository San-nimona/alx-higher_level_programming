#!/usr/bin/python3
"""6-load_from_json_file.py"""


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”
    Args:
        filename
    """
    import json
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
