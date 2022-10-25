#!/usr/bin/python3
"""Defines a file storage class."""
import json


class FileStorage:
    """
    file storage class
    Attributes:
        __file_path (str): The file path
        __objects (dict):  will store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __object
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        :param obj: object to be set in
        """
        obj_class_name = obj.__class__.__name__
        obj_id = obj.id
        key_name = obj_class_name + "." + obj_id

        FileStorage.__objects[key_name] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        with open(FileStorage.__file_path, "w") as FILE:
            json.dump(FileStorage.__objects, FILE)

    def reload(self):
        """
        deserializes the JSON file to __objects
        does nothing if file is not found
        """
        try:
            with open(FileStorage.__file_path, "r") as read_file:
                FileStorage.__objects = json.load(read_file)
        except FileNotFoundError:
            pass
