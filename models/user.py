#!/usr/bin/python3
"""
User module for AirBnB clone project.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class for representing a user.
    """
    def __init__(self):
        """Initialize User instance."""
        pass


if __name__ == '__main__':
    my_user = User()
    print(my_user)
