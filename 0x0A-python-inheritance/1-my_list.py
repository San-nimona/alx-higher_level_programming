#!/usr/bin/python3
"""My list module"""


class MyList(list):
    """Inherits from list\
        Prints a list in a sorted ascending order"""
    def print_sorted(self):
        """Prints the list in a sorte order"""
        if not isinstance (self, list):
            raise TypeError('Must be a list')
        for i in self:
            if not isinstance(i, int):
                raise TypeError('element must be int')
        print(sorted(self))
