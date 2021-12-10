#!/usr/bin/python3
"""
This module describes a class Square
"""


class Square:
    """description for the class Square"""

    def __init__(self, size=0):
        """initializes instances of the class square

        Args:
            size (int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """retrieves the size of the square instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square
        ensures the correct value is entered"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """returns the area of the square instance"""
        return (self.__size ** 2)

    def my_print(self):
        """print the square instance with the character # to stdout"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for n in range(self.__size):
                print('#', end='')
            print()
