#!/usr/bin/python3
"""0-read_file.py"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename
    """
    with open(filename, encoding="utf-8") as f:
        my_file = f.read()
        print(my_file)
