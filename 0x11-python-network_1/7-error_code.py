#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the body of the response.
If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code
"""
import requests
import sys


def fetch_url(url):
    """
    Fetches the content of a given URL and prints it.

    Args:
        url (str): The URL to fetch content from.
    """
    response = requests.get(url)
    print(response.text)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)

