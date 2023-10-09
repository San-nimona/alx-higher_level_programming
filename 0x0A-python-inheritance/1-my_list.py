#!/usr/bin/python3
"""My list module"""
class MyList(list):
    """Inherits from list\
        Prints a list in a sorted ascending order"""
    def print_sorted(self):
        print(sorted(self))
