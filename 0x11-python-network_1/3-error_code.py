#!/usr/bin/python3
"""
sends a request to the URL and displays body of the response(decoded in utf-8)
handles HTTPError exceptions
"""
if __name__ == "__main__":
    import sys
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError

    req = Request(sys.argv[1])

    try:
        with urlopen(req) as res:
            res = res.read()
            print(res.decode("utf-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")
