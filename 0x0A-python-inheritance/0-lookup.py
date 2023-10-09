#!/usr/bin/python3
"""Lookup module"""


def lookup(obj):
    """A function that returns the list of available attributes \
            and methods of an object

        Args:
            @obj (object): The object received
        Return:
            A list object
    """
    return dir(obj)
