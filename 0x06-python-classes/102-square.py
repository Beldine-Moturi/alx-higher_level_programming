#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Description for a square."""

    def __init__(self, size=0):
        """Initialize new square objects.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Returns the size of the square instance."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the value of the square instance"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square instance."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Defines the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= compmarison to a Square."""
        return self.area() >= other.area()
