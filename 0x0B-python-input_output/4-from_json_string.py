#!/usr/bin/python3
"""
a module that provide a function to deserialize
python code to JSON string
"""
import json


def to_json_string(my_obj):
    """
    convert serialized object to python object
    """

    return json.loads(my_obj)
