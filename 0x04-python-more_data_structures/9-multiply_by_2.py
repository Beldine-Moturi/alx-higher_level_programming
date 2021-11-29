#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """return dict with all values * 2"""
    return {key: a_dictionary[key]*2 for key in a_dictionary}
