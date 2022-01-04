#!/usr/bin/python3
"""Defines a function ``is_same_class()``"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class
    ; otherwise False.

    Args:
        obj: an object whose class is to be verifed
        a_class: a class to chech whether obj is a member of
    """

    if type(obj) == a_class:
        return True
    return False
