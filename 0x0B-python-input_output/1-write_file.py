#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file

    Args:
        filename
        text
    Return:
        The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
