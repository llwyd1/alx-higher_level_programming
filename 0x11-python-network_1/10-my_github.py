#!/usr/bin/python3
"""Takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id"""

if __name__ == "__main__":

    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(username, password))

    if r.status_code >= 400:
        print("None")
    else:
        print(r.json().get('id'))
