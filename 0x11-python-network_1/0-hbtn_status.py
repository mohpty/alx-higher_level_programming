#!/usr/bin/python3
"""
    This module contains a function that fetches a website
    and returns response.
"""
import urllib.request as req

with req.urlopen('https://alx-intranet.hbtn.io/status') as res:
    content_type = res.info().get_content_type()
    content = res.read()
    utf8 = content.decode('utf-8')

print("Body response:")
print("\t- type: {}".format(type(content)))
print("\t- content: {}".format(content))
print("\t- utf8 content: {}".format(utf8))
