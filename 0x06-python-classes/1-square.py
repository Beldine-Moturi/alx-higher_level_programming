#!/usr/bin/python3
"""
This module defines a class Square, with a private attribute size
The objects of this class are also instantiated with the value size
"""


class Square:
    """ A class Square, whose objects are instantiated with the private value
    size"""
    def __init__(self, size):
        self.__size = size
