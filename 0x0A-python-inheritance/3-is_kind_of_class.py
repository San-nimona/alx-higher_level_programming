#!/usr/bin/python3
"""3-is_kind_of_class.py"""
def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of,\
            or if the object is an instance of a class that inherited from,\
            the specified class 
    Args:
        @obj (object): The object
        @a_class (class): The class
    Return:
        True if the object is an instance
        Otherwise False
    """
    return isinstance(obj, a_class)
