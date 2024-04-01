#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter
 and displays the body of the response
"""
from sys import argv
import urllib.parse as parser
import urllib.request as req

if __name__ == '__main__':
    val = {'email': argv[2]}
    data = parser.urlencode(val).encode("ascii")
    request = req.Request(argv[1],data)
    with req.urlopen(request) as res:
        print(res.read().decode('utf-8'))
