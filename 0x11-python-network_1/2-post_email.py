#!/usr/bin/python3
"""
sends a POST request to the passed URL(command-line argument) with
an email as a parameter, and displays body of the response(decoded in utf-8)
"""
if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        res = response.read()
        print(res.decode('utf-8'))
