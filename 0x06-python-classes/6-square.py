#!/usr/bin/python3
"""
This module describes a class Square
"""


class Square:
    """description for the class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes instances of the class square
        Args:
            size (int): the size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """prints the squarw instance to stdout"""
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()
