#!/usr/bin/python3
"""Defines a class MyList that inherits from List"""


class MyList(list):
    """Description for the class MyList"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        assuming all elements of the list are of type int"""
        my_list = self[:]
        x = len(my_list)
        for i in range(x):
            for n in range(0, x-i-1):
                if (my_list[n] > my_list[n+1]):
                    my_list[n], my_list[n+1] = my_list[n+1], my_list[n]
        print(my_list)
