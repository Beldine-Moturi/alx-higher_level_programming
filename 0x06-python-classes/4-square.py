#!/usr/bin/python3
"""
This module describes a class Square
"""


class Square:
    """Description of the class Square"""
    def __init__(self, size=0):
        """initializes instances of Square with optional size attribute"""
        self.size = size

    @property
    def size(self):
        """retrieves the attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ensures the correct value for the attribute size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """returns the area of Square instances"""
        return (self.__size ** 2)
