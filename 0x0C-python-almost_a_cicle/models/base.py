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
        """Converts list_dictionaries to json representations"""
        if len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representations"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)


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

    @classmethod
    def create(cls, **dictionary):
        '''
        Return a class instance with already set attributes
        '''
        from models import rectangle
        from models import square
        if cls.__name__ == 'Rectangle':
            x = rectangle.Rectangle(1, 2, 3)
        else:
            x = square.Square(1, 2, 3)

        x.update(**dictionary)
        return x

    @classmethod
    def load_from_file(cls):
        '''read list of instances from a file'''
        filename = cls.__name__ + '.json'
        output = []
        try:
            with open(filename, 'r', encoding = 'utf-8') as f:
                contents = f.readlines()
                for line in contents:
                    objstr = cls.from_json_string(line)
                    for item in objstr:
                        obj = cls.create(**item)
                        output.append(obj)
                return output
        except FileNotFoundError:
            return output
