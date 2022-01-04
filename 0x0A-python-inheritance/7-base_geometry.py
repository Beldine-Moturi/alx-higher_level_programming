#!/usr/bin/python3
"""Defines a class ``BaseGeometry``"""


class BaseGeometry:
    """Description for the class BaseGeometry"""

    def area(self):
        """raises an exception"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the argument ``value``

        Args:
            name: a string
            value (int): an int
        """

        if type(value) != int:
            raise TypeError('<name> must be an integer')
        if value <= 0:
            raise ValueError('<name> must be greater than 0')
