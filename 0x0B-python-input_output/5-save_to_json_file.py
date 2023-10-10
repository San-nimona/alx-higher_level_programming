#!/usr/bin/python3
"""5-save_to_json_file.py"""


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,\
            using a JSON representation

    Args:
        my_obj
        filenname
    """
    import json
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
