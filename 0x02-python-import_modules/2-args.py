#!/usr/bin/python3
if __name__ == "__main__":
    """print command line arguments"""
    import sys
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:", "1: {}".format(sys.argv[1]), sep='\n')
    else:
        print("{} arguments:".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))
