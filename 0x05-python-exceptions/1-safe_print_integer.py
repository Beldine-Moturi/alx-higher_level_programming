#!/usr/bin/python3
def safe_print_integer(value):
    """prints value"""
    try:
        print("{:d}".format(value))
    except:
        return False
    else:
        return True
