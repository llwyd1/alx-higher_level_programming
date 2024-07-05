#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter"""

if __name__ == '__main__':

    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post(url, data={'q': q})

    try:
        d = r.json()
        if d == {}:
            print('No result')
        else:
            print("[{}] {}".format(d.get('id'), d.get('name')))
    except ValueError:
        print('Not a valid JSON')
