#!/usr/bin/python3
"""
serialize/deserialize instance to JSON file
"""
import json
import os
from models.base_model import BaseModel


class FileStorage():
    '''
    serialize instances to JSON file, and
    deserialize JSON file to instances.
   '''

    __file_path = 'file.json'
    __objects = {}

    def new(self, obj):
        '''
        sets in __objects the obj with key <obj class name>.id
        '''
        object_class_name = obj.__class__.__name__
        key = '{}.{}'.format(object_class_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        '''
        Return: dictionary objects
        '''
        return FileStorage.__objects

    def save(self):
        '''
        serializes __objects to the JSON file path (path: __file_path)
        '''
        all_objs = FileStorage.__objects
        obj_dict = {}

        for key, obj in all_objs.items():
            if hasattr(obj, "to_dict") and callable(obj.to_dict):
                obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        '''
        deserializes JSON file to __objects (only if JSON file
        (__file_path) exist. otherwise do nothing.
        '''

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
