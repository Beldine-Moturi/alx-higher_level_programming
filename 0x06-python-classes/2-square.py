#!/usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    """
    Description of class square
    """
    def __init__(self, size=0):
        """sets the attributes for instances of the class Square
        Args:
            size: size of the square, which must be an integer
        greater than 0"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
