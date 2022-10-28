#!/usr/bin/python3
"""Defines a file storage class."""
import json
from models.base_model import BaseModel
from models.user import User

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
        obj_dict = {}
        for k, v in FileStorage.__objects.items():
            obj_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as FILE:
            json.dump(obj_dict, FILE)

    def reload(self):
        """
        deserializes the JSON file to __objects
        does nothing if file is not found
        """
        try:
            with open(FileStorage.__file_path, "r") as read_file:
                dummy_dict = json.load(read_file)
                for k, v in dummy_dict.items():
                    FileStorage.__objects[k] = eval(v['__class__'])(**v)
        except FileNotFoundError:
            pass