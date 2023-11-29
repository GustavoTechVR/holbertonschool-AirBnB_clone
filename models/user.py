#!/usr/bin/python3
"""
User module for AirBnB clone project.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class for representing a user.
    """
    def _init_(self):
        """Initialize User instance."""
        pass


if _name_ == '_main_':
    my_user = User()
    print(my_user)
