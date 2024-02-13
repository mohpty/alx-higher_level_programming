#!/usr/bin/python3
"""Includes a function that store its args in a file"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    arr = load_from_json_file(filename)
except FileNotFoundError:
    arr = []

for i in sys.argv[1:]:
    arr.append(i)

save_to_json_file(arr, filename)
