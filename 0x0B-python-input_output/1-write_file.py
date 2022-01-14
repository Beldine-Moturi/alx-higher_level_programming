#!/usr/bin/python3
"""Deifnes a function```write_file()``"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written:

    Args:
        filename (str): the name of the file to write to
        text (str): the text that will be written to file 'filename'
    """

    with open(filename, "w", encoding='utf-8') as my_file:
        return (my_file.write(text))
