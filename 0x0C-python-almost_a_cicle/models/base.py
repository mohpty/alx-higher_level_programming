#!/usr/bin/python3
"""Contains declaration of class Base"""
import json
from . import rectangle
class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON representation of list_objs to a file"""
        filename = cls.__name__ + '.json'
        content = []
        if list_objs is not None:
            for obj in list_objs:
                obj = obj.to_dictionary()
                obj_dict = json.loads(cls.to_json_string(obj))
                content.append(obj_dict)

        with open(filename, 'w') as f:
            json.dump(content, f)
