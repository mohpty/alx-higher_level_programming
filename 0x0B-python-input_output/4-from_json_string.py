#!/usr/bin/python3
"""
a module that provide a function to deserialize
python code to JSON string
"""
import json


def from_json_string(my_str):
    """
    convert serialized object to python object
    """

    return json.loads(my_str)
