#!/usr/bin/env python3
"""
module for serializing and deserializing object to file storage
"""


import os


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
        self.__file_path = self.engine_directory + '/objects.json'
        print(self.__file_path)
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects
        """

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """

    def save(self):
        """serializes the __objects to the JSON file
            -> path (__file_path)
        """

    def reload(self):
        """deserializes the JSON file to __objects
            -> path (__file_path)
           ONLY if it exists, no exceptions are raised
        """
