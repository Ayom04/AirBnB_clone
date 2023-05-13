#!/usr/bin/python3
"""This module defines a class User and inherits from baseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various public attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
