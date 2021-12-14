#!/usr/bin/python3
"""
This module defines a class
that prevents users from dynamically creating new attributes
"""


class LockedClass:
    """
    class that allows only one attribute creation
    """
    __slot__ = 'first_name'

    def __init__(self, name=''):
        """
        Initializes new objects
        """
        self.first_name = name
