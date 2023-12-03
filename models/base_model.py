#!/usr/bin/python3
"""
Module for BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class with attributes and methods for other classes to inherit
    """
    def __init__(self, *args, **kwargs):
        """Initializes BaseModel instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            storage.new(self)
    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    def save(self):
        """Updates the updated_at attribute and saves to storage"""
        self.updated_at = datetime.now()
        storage.save()


if __name__ == '__main__':
    my_model = BaseModel()
    print(my_model)
