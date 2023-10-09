#!/usr/bin/python3
"""My list module"""


class MyList(list):
    """Inherits from list\
        Prints a list in a sorted ascending order"""
    def print_sorted(self):
        """Prints the list in a sorte order"""
        new_list = sorted(self)
        print(new_list)
    def __str__(self):
        return super().__str__()
