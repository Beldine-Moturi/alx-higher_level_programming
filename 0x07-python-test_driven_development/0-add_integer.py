#!/usr/bin/python3
"""
This module defines a function add_integer() that adds two integers
"""


def add_integer(a, b=98):
    """
    returns the result of addition of two integers, a and b
    the result itself will be an integer
    For example:

    >>> add_integer(10, 15)
    25
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
