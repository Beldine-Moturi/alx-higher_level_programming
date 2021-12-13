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
    my_list = [a, b]
    result = 0
    for i in my_list:
        if type(i) not in [int, float]:
            raise TypeError("{} must be an integer".format(i))
        if type(i) == float:
            i = int(i)
        result += i
    return result
