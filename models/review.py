#!/usr/bin/python3
"""place module for HBnB project"""


from models.base_model import BaseModel


class Review(BaseModel):
    """review class storing users review"""
    place_id = ""
    user_id = ""
    text = ""
