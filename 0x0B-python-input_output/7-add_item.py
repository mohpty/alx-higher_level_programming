#!/usr/bin/python3
"""Includes a function that store its args in a file"""
import json
import sys


if __name__ == '__main__':
    args = sys.argv[1:]
    with open('add_item.json', 'r+', encoding='utf-8') as f:
        obj = json.loads(f.readline())
        for i in args:
            if i in obj:
                pass
            else:
                obj.append(i)
        f.write(json.dumps(args))
