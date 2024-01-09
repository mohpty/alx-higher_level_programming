#!/usr/bin/bash
"""
a module that provide a function to serialize
python code to JSON string
"""
import json


def to_json_string(my_obj):
    """
    represent python object in a str
    """

    return json.dumps(my_obj)
