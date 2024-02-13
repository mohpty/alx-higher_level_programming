#!/usr/bin/python3
"""Include function to load python object"""
import json


def load_from_json_file(filename):
    """
    Used to deserialize a stored json object from a file
    """

    with open(filename, mode='r', encoding='utf-8') as f:
        obj = f.read()
        return json.loads(obj)
