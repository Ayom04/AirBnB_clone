#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_user(test_basemodel):
    """ """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test(self):
        """ """
        return self.value

    def test_first_name(self):
        """ """
        fname = self.value()
        self.assertEqual(type(fname.first_name), str)

    def test_last_name(self):
        """ """
        lname = self.value()
        self.assertEqual(type(lname.last_name), str)

    def test_email(self):
        """ """
        email = self.value()
        self.assertEqual(type(email.email), str)

    def test_password(self):
        """ """
        password = self.value()
        self.assertEqual(type(password.password), str)

    def first_name_string(self):
        """ """
        fname = self.value()
        return fname.first_name

    def last_name_string(self):
        """ """
        lname = self.value()
        return lname.last_name
