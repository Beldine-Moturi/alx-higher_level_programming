#!/usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    """Describes a class Square"""

    def __init__(self, size=0):
        """Initialize a new square instance

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Returns the current area of the square instance"""
            return (self.__size ** 2)