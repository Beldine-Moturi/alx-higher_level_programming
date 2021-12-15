#!/usr/bin/python3
"""
This module contains description for a function ``say_my_name()``
that prints a string of users' first and last name
"""


def say_my_name(first_name, last_name=''):
    """
    Prints users' first and last name

    Args:
        first_name (str): first name of the user
        last_name (str): last name of the user (default empty string)
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
