#!/usr/bin/python3
"""State module for HBnB project"""


from models import BaseModel


class Amenity(BaseModel):
    """amenity class that contains name"""
    name = ''
