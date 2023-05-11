#!/usr/bin/python3
"""tests for stte.py"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ class testing the state model"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """ test the name"""
        Name = self.value
        self.assertEqual(type(Name.name), str)
