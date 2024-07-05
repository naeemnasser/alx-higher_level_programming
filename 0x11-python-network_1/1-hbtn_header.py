#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a request to the URL
    with urllib.request.urlopen(url) as response:
        # Get the headers from the response
        headers = response.getheaders()
        # Find and print the value of X-Request-Id
        for header in headers:
            if header[0] == "X-Request-Id":
                print(header[1])
                break

