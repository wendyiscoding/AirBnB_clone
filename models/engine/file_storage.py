#!/usr/bin/env python3
"""
module for serializing and deserializing object to file storage
"""


import os
from models.base_model import BaseModel
from models.state import State
from models.user import User


class FileStorage():
    """
    FileStorage class for serialzing and deserializing objects
    into and from files respectively
    """
    engine_directory = ""
    parent_directory = ""

    def __init__(self):
        """instantiation method for class
        """
        self.engine_directory = os.path.dirname(os.path.abspath(__file__))
        self.parent_directory = os.getcwd()
        self.__file_path = self.parent_directory + '/file.json'
        self.__objects = dict()

    def all(self):
        """returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        # TODO not sure if this check is needed for holberton checker
        try:
            obj_d = obj.to_dict()
        except:
            raise TypeError('object passed to filestorage has no to_dict()')
        key = obj_d['__class__'] + '.' + str(obj_d['id'])
        self.__objects[key] = obj

    def delete(self, obj):
        """deletes obj from __objects
        """
        key = obj.__class__.__name__ + '.' + str(obj.id)
        try:
            del self.__objects[key]
            return True
        except:
            return False

    def save(self):
        """serializes the __objects to the JSON file
            -> path (__file_path)
        """
        json_dump = str({k: v.to_dict() for (k, v) in self.__objects.items()})
        with open(self.__file_path, 'w', encoding='utf-8') as myFile:
            myFile.write(json_dump)

    def reload(self):
        """deserializes the JSON file to __objects
            -> path (__file_path)
           ONLY if it exists, no exceptions are raised
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as myFile:
                my_obj_dump = myFile.read()
        except:
            return
        objects = eval(my_obj_dump)
        for (k, v) in objects.items():
            objects[k] = eval(k.split('.')[0] + '(**v)')
        self.__objects = objects
