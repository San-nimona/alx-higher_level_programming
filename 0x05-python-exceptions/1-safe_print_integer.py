#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer
    Args:
        value (int): The int to print
    Returns:
        If a TypeError - False else  True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
