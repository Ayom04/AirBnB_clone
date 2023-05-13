#!/usr/bin/python3
""" test case for review.py"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """class testing review models"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """class tesing review model"""
        PlaceID = self.value()
        self.assertEqual(type(PlaceID.place_id), str)

    def test_user_id(self):
        """class testing review model"""
        UserID = self.value()
        self.assertEqual(type(UserID.user_id), str)

    def test_text(self):
        """class testing review model"""
        Text = self.value()
        self.assertEqual(type(Text.text), str)
