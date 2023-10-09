#!/usr/bin/python3
"""101-add_attribute.py"""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object

    Raises:
        A TypeError if the object can't have new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
