#!/usr/bin/python3
""" module for file_storage.py"""
import unittest
from models.base_model import BaseModel
from models import storage
import os

class test_fileStorage(unittest.TestCase):
    """class to test the file_storage stored"""

    def setUp(self):
        """set up test environment"""
        _del_list = []
        for key in storage._FileStorage__objects.keys():
            _del_list.append(key)
        for key in _del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """tear down test environment"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """test if the list is empty"""
        self.assertEqual(len(storage._FileStorage__objects), 0)

    def test_obj_list(self):
        """test if the list is not empty"""
        self.assertEqual(len(storage._FileStorage__objects), 1)

    def test_obj_get(self):
        """test if the object is not empty"""
        self.assertEqual(len(storage._FileStorage__objects), 1)

    def test_obj_add(self):
        """test if the object is not empty"""
        self.assertEqual(len(storage._FileStorage__objects), 1)

    def test_new(self):
        """ New object is correctly added to __objects """
        base = BaseModel()
        for obj in storage.all().values():
            _temp = obj
        self.assertTrue(_temp is obj)

    def test_all(self):
        """ test if all objects are in __objects """
        base = BaseModel()
        for obj in storage.all().values():
            _temp = storage.all()
        self.assertIsInstance(_temp, dict)


        


