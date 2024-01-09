#!/usr/bin/python3
"""Includes a function that store its args in a file"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    arr = load_from_json_file('add_item.json')
except:
    arr = []

for i in sys.argv[1:]:
    arr.append(i)

save_to_json_file(arr, 'add_item.json')
