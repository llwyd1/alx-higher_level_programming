#!/usr/bin/python3
"""Takes in a URL, sends a request and displays the value of a
variable in the header of the response"""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        header = response.headers.get('X-Request-Id')
        print(header)
