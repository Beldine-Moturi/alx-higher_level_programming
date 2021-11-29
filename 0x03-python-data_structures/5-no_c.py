#!/usr/bin/python3
def no_c(my_string):
    """remove characters from a string"""
    new_string = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        else:
            new_string += char
    return new_string
