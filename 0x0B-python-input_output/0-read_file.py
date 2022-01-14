#!/usr/bin/python3
"""Defines a function ``read_file()``"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): the name of the file to read from
    """

    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end='')
