#!/usr/bin/python3
"""
Module for FileStorage class
"""
import json
from os.path import exists
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serialized_objs, file)
    def reload(self):
        """Deserializes the JSON file to __objects if the file exists"""
        if exists(self.__file_path) and not exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                try:
                    loaded_objs = json.load(file)
                except json.JSONDecodeError:
                    return
                for key, value in loaded_objs.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj


# Create a unique FileStorage instance for the application
storage = FileStorage()
storage.reload(i)
