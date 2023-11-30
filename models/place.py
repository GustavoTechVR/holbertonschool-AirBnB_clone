#!/usr/bin/python3
"""
Place module for AirBnB clone project.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class for representing a place.
    """
    def __init__(self, *args, **kwargs):
        """Initialize Place instance."""
         super().__init__(*args, **kwargs)

if __name__ == '__main__':
    my_place = Place()
    print(my_place)
