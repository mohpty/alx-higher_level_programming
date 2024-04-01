#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request
    and displays the value of the X-Request-Id variable
    found in the header of the response
"""
import urllib.request as req
from  sys import argv

with req.urlopen(argv[1]) as res:
    print(res.getHeader('X-Request-Id'))
