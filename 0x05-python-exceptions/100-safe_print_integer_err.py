#!/usr/bin/python3
def safe_print_integer_err(value):
    """prints error messages to stderr"""
    try:
        print("{:d}".format(value))
    except Exception as ex:
        print("Exception: ", ex)
        return False
    else:
        return True
