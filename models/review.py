#!/usr/bin/python3
"""
Review module for AirBnB clone project.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class for representing a review.
    """
    def _init_(self):
        """Initialize Review instance."""
        pass


if _name_ == '_main_':
    my_review = Review()
    print(my_review)
