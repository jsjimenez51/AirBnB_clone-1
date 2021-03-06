#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        clsdic = {}
        if cls is None:
            return self.__objects
        else:
            if type(cls) is str:
                cls = eval(cls)
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    clsdic[key] = value
            return clsdic

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(FileStorage.__file_path, mode='r',
                      encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects in FileStorage
        """
        kys = []
        for key, value in FileStorage.__objects.items():
            if obj == value:
                kys.append(key)

        for item in kys:
            FileStorage.__objects.pop(item)

        FileStorage.save()

    def close(self):
        """closes the file storage and deserializes the JSON file to objects
        """
        self.reload()
