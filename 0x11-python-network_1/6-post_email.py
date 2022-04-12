#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
and finally displays the body of the response.
"""
if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    r = requests.post(url, data=values)
    print(r.text)
