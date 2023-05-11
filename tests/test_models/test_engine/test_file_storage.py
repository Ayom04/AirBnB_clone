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
        except ValueError:
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

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        base = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        base = BaseModel()
        _thing = base.to_dict()
        base.save()
        base2 = BaseModel(**_thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        base = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        base = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(base.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        base = BaseModel()
        base.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        base = BaseModel()
        _id = base.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)
