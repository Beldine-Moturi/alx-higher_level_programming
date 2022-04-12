#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response.
"""
if __name__ == "__main__":
    import sys
    import requests

    bad_r = requests.get(sys.argv[1])
    code = bad_r.status_code
    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(bad_r.text)
