#!/usr/bin/python3
"""7-base_geometry & 8-rectangle.py"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""

    def area(self):
        """raises exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer and greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    """A class that inherits for BaseGeometry"""

    def __init__(self, width, height):
        """Instantiating the class with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates area of a Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Rectangle description"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
