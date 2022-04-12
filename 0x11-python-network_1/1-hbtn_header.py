#!/usr/bin/python3
"""
sends a request to the URL(command-line argument)and displays
the value of the X-Request-Id variable found in the header of the response.
"""
if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as res:
        res = res.info()
        print(res.get('X-Request-Id'))
