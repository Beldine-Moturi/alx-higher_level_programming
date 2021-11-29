#!/usr/bin/python3
def no_c(my_string):
    """remove characters from a string"""
    myList = [char for char in my_string if char != 'c' or char != 'C']
    return ("".join(myList))
