#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL, and displays the body
of the response (decoded in utf-8). Manages urllib.error.HTTPError exceptions.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
