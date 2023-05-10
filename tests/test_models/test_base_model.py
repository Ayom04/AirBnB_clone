#!/usr/bin/python3
""" Test model for base model. """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class TestModel(unittest.TestCase):
    """ Test model for base model. """
    def setUp(self):
        self.model = BaseModel()
        self.model.model_name = "test"
        self.model.model_version = 1
        self.model.model_description = "test model"
        self.model.model_author = "test author"
        self.model.model_date = datetime.datetime.now()
        self.model.model_uuid = UUID('00000000-0000-0000-0000-000000000000')
        self.model.save()
        self.model.delete()

    def tearDown(self):
        self.model.delete()
        self.model = None
        self.model = BaseModel()
        self.model.model_name = "test"
        self.model.model_version = 1
        self.model.model_description = "test model"
        self.model.model_author = "test author"
        self.model.model_date = datetime.datetime.now()
        self.model.model_uuid = UUID('00000000-0000-0000-0000-000000000000')
        self.model.save()
        self.model.delete()
        self.model = BaseModel()
        self.model.model_name = "test"

    def test_model_name(self):
        self.assertEqual(self.model.model_name, "test")
        self.model.model_name = "test2"
        self.assertEqual(self.model.model_name, "test2")
        self.model.delete()
        self.model = BaseModel()
        self.model.model_name = "test"
        self.assertEqual(self.model.model_name, "test")
        self.model.delete()
        self.model = BaseModel()
        self.model.model_name = "test"
        self.assertEqual(self.model.model_name, "test")

    def test_model_version(self):
        self.assertEqual(self.model.model_version, 1)
        self.model.model_version = 2
        self.assertEqual(self.model.model_version, 2)
        self.model.delete()
        self.model = BaseModel()
        self.model.model_version = 1
        self.assertEqual(self.model.model_version, 1)
        self.model.delete()
        self.model = BaseModel()
        self.model.model_version = 1
        self.assertEqual(self.model.model_version, 1)
        self.model.delete()
        self.model = BaseModel()
        self.model.model_version = 1
        self.assertEqual(self.model.model_version, 1)
        self.model.delete()

    def test_model_description(self):
        self.assertEqual(self.model.model_description, "test model")
        self.model.model_description = "test model2"
        self.assertEqual(self.model.model_description, "test model2")
        self.model.delete()
        self.model = BaseModel()
        self.model.model_description = "test model"
        self.assertEqual(self.model.model_description, "test model")
        self.model.delete()
        self.model = BaseModel()
        self.model.model_description = "test model"
        self.assertEqual(self.model.model_description, "test model")

    def test_model_date(self):
        self.assertEqual(self.model.model_date, datetime.datetime.now())
        self.model.model_date = datetime.datetime.now()
        self.assertEqual(self.model.model_date, datetime.datetime.now())
        self.model.delete()
        self.model = BaseModel()
        self.model.model_date = datetime.datetime.now()
        self.assertEqual(self.model.model_date, datetime.datetime.now())
        self.model.delete()
        self.model = BaseModel()
        self.model.model_date = datetime.datetime.now()
        self.assertEqual(self.model.model_date, datetime.datetime.now())
        self.model.delete()

    def test_model_uuid(self):
        self.assertEqual(self.model.model_uuid, UUID(
            '00000000-0000-0000-0000-000000000000'))
        self.model.model_uuid = UUID('00000000-0000-0000-0000-000000000001')
        self.assertEqual(self.model.model_uuid, UUID(
            '00000000-0000-0000-0000-000000000001'))
        self.model.delete()
        self.model = BaseModel()
        self.model.model_uuid = UUID('00000000-0000-0000-0000-000000000000')
        self.assertEqual(self.model.model_uuid, UUID(
            '00000000-0000-0000-0000-000000000000'))

    def test_save(self):
        self.assertEqual(self.model.model_uuid, UUID(
            '00000000-0000-0000-0000-000000000000'))
        self.model.save()
        self.assertEqual(self.model.model_uuid, UUID(
            '00000000-0000-0000-0000-000000000001'))
        self.model.delete()
        self.model = BaseModel()
        self.model.save()
        self.assertEqual(self.model.model_uuid, UUID(
            '00000000-0000-0000-0000-000000000000'))

    def test_delete(self):
        self.assertEqual(self.model.model_uuid, UUID(
            '00000000-0000-0000-0000-000000000000'))
        self.model.save()
        self.assertEqual(self.model.model_uuid, UUID(
            '00000000-0000-0000-0000-000000000001'))
        self.model.delete()
        self.model = BaseModel()
        self.model.save()
        self.assertEqual(self.model.model_uuid, UUID(
            '00000000-0000-0000-0000-000000000000'))

    def test_default(self):
        self.assertEqual(self.model.model_name, "test")
        self.assertEqual(self.model.model_version, 1)
        self.assertEqual(self.model.model_description, "test model")
        self.assertEqual(self.model.model_author, "test author")
        self.assertEqual(self.model.model_date, datetime.datetime.now())
        self.assertEqual(self.model.model_uuid, UUID(
            '00000000-0000-0000-0000-000000000000'))

    def test_kwargs(self):
        self.assertEqual(self.model.model_name, "test")
        self.assertEqual(self.model.model_version, 1)
        self.assertEqual(self.model.model_description, "test model")
        self.assertEqual(self.model.model_author, "test author")
        self.assertEqual(self.model.model_date, datetime.datetime.now())
        self.assertEqual(self.model.model_uuid, UUID(
            '00000000-0000-0000-0000-000000000000'))

    def test_updated_at(self):
        self.assertEqual(self.model.updated_at, datetime.datetime.now())
        self.model.updated_at = datetime.datetime.now()
        self.assertEqual(self.model.updated_at, datetime.datetime.now())
        self.model.delete()
        self.model = BaseModel()
        self.model.updated_at = datetime.datetime.now()
        self.assertEqual(self.model.updated_at, datetime.datetime.now())
        self.model.delete()
        self.model = BaseModel()
        self.model.updated_at = datetime.datetime.now()
        self.assertEqual(self.model.updated_at, datetime.datetime.now())
        self.model.delete()

    def test_created_at(self):
        self.assertEqual(self.model.created_at, datetime.datetime.now())
        self.model.created_at = datetime.datetime.now()
        self.assertEqual(self.model.created_at, datetime.datetime.now())
        self.model.delete()
        self.model = BaseModel()
        self.model.created_at = datetime.datetime.now()
        self.assertEqual(self.model.created_at, datetime.datetime.now())
        self.model.delete()
        self.model = BaseModel()
        self.model.created_at = datetime.datetime.now()
        self.assertEqual(self.model.created_at, datetime.datetime.now())
        self.model.delete()

    def test_kwargs_int(self):
        """ """
        int = self.value()
        copy = int.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_kwargs_float(self):
        """"""
        float = self.value()
        copy = float.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_list(self):
        """ """
        _list = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**_list)

    def test_kwargs_dict(self):
        """ """
        d = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**d)

    def test_kwargs_str(self):
        """ """
        s = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**s)

    def test_kwargs_bool(self):
        """ """
        b = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**b)

    def test_kwargs_tuple(self):
        """ """
        t = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**t)

    def test_kwargs_set(self):
        """ """
        s = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**s)

    def test_kwargs_frozenset(self):
        """ """
        f = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**f)

    def test_kwargs_dict_int(self):
        """ """
        d = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**d)

    def test_kwargs_dict_float(self):
        """ """
        d = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**d)

    def test_kwargs_dict_none(self):
        """ """
        d = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**d)

    def test_id(self):
        self.assertEqual(self.model.id, 1)
        self.model.id = 2
        self.assertEqual(self.model.id, 2)
        self.model.delete()
        self.model = BaseModel()
        self.model.id = 1
        self.assertEqual(self.model.id, 1)
        self.model.delete()

    def test_todict(self):
        self.assertEqual(self.model.todict(), {
           'model_name': 'test',
           'model_version': 1,
           'model_description': 'test model',
           'model_author': 'test author',
           'model_date': datetime.datetime.now(),
           'model_uuid': UUID('00000000-0000-0000-0000-000000000000'),
           'updated_at': datetime.datetime.now(),
           'created_at': datetime.datetime.now(),
           'id': 1
        })
        self.model.delete()
        self.model = BaseModel()
        self.model.id = 1
