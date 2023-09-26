#!/usr/bin/python3

"""Defines a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """Represents a circle."""

    def __init__(self, radius=0):
        """Initializes MagicClass.
        Arg:
            radius (float or int): radius of new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of Magic Class."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of Magic Class."""
        return (2 * math.pi * self.__radius)
