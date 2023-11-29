#!/usr/bin/python3
"""
Review module for AirBnB clone project.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class for representing a review.
    """
    def __init__(self):
        """Initialize Review instance."""
        pass


if __name__ == '__main__':
    my_review = Review()
    print(my_review)
