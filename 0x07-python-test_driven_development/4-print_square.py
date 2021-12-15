#!/usr/bin/python3
"""
This module describes a function ``print_square()`` that
prints a square with the character #
"""


def print_square(size):
    """
    prints a square with the character #

    Args:
       size (int): the size of the square to be printed
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for n in range(size):
            print('#', end='')
        print()
