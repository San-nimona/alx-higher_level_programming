#!/usr/bin/python3
"""100-my_int.py"""


class MyInt(int):
    """Has == and != inverted"""
    def __init__(self, value):
        """Instantiation with value"""
        self.value = value
    def __eq__(self, value):
        """Reimplimenting equality"""
        return self.value != value
    def __ne__(self, value):
        """Reimplimenting equality"""
        return self.value == value
