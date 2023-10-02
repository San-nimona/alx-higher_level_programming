#!/usr/bin/python3

''' A Module that creates a Square object '''


class Square:
    ''' Creating an Object template '''

    def __init__(self, size=0):
        """
            The init method initializes class instance

        @self:
            A parameter referring the class instance

        @size:
            size of square - a +ve integer
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
