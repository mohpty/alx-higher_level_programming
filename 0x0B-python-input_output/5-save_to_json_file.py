#!/usr/bin/python3
"""Include function to save json object"""
import json


def save_to_json_file(my_obj, filename):
    """
    Used to serialize a python object and
    save it in a file
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
