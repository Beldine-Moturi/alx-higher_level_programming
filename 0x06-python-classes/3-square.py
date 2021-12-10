#!/usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    """ A class Square with size and area instance attributes"""
    def __init__(self, size=0):
        """Initializes a new Square

        Args:
            size: the size of the instance square
        """
        if not isintance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """calculates and return the area of the instance square"""
        return (self.__size * self.__size)
