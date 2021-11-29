#!/usr/bin/python3
def  print_sorted_dictionary(a_dictionary):
    """print a dictionary by ordered keys"""
    my_list = list(a_dictionary.keys())
    for key in sorted(my_list):
        print('{}: {}'.format(key, a_dictionary[key]))
