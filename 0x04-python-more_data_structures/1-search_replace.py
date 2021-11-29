#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replace occurrences of search element in my_list by replace"""
    return [i if i != search else replace for i in my_list]
