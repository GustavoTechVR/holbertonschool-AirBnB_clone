#!/usr/bin/python3
"""
BaseModel module for AirBnB clone project.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class for representing the base model.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel instance.

        Args:
        - id (str): unique id for each BaseModel
        - created_at (datetime): current datetime when an instance is created
        - updated_at (datetime): current datetime when an instance is created and updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ of the instance.

        Keys:
        - __class__: class name of the object
        - created_at and updated_at: converted to string object in ISO format

        Returns:
        - dict: dictionary representation of the BaseModel instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


if __name__ == '__main__':
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
