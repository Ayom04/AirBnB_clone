#!/usr/bin/python3
"""State module for HBnB project"""


from models import BaseModel


class City(BaseModel):
    """city class that contains state_id and name"""
    state_id = ''
    name = ''
