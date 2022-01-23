#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Description for the class"""

    def __init__(self, first_name, last_name, age):
        """Initializes instances of the class

        Args:
            first_name: first name of the Student instance
            last_name: last name of the Student instance
            age: the age of the Student instance
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""

        return self.__dict__
