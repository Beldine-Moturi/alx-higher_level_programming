#!/usr/bin/python3
def safe_print_integer_err(value):
    """prints error messages to stderr"""
    import sys
    try:
        print("{:d}".format(value))
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False
    else:
        return True
