#!/usr/bin/python3
"""Includes a function that store its args in a file"""
import json
import sys


if __name__ == '__main__':
    args = sys.argv[1:]
    with open('add_item.json', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(args))
