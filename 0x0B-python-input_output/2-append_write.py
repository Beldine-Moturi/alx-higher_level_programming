#!/usr/bin/python3
"""Defines a function ``append_write()``"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and
    returns the number of characters added:

    Args:
        filename (str): the name of the file to append to
        text (str): the text to append to filename
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
