#!/usr/bin/python3
"""9-student.py"""


class Student:
    """
    A class that defines a student by: firts and last name and age
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation with name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of a Student
        """
        return self.__dict__
