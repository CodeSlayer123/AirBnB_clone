#!/usr/bin/python3
"""Doc stuff"""
import json
import models


class FileStorage():
    """Doc"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        tmpdict = {}
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                tmpdict[key] = value.to_dict()
            json.dump(tmpdict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    self.__objects[key] = value['__class__'](**value)
                    print("in the loop")
                    print(self.__objects)
        except:
            pass
