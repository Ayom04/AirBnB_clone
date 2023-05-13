#!/usr/bin/python3
""" test for place.py"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ class to test for place models """

    def __init__(self, *args, **kwargs):
        """test initialization """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test case for city_id """
        cityid = self.value()
        self.assertEqual(type(cityid.city_id), str)

    def test_user_id(self):
        """test case for user_id """
        userid = self.value()
        self.assertEqual(type(userid.user_id), str)

    def test_name(self):
        """test case for name """
        name = self.value()
        self.assertEqual(type(name.name), str)

    def test_description(self):
        """test case for description """
        description = self.value()
        self.assertEqual(type(description.description), str)

    def test_number_rooms(self):
        """test case for number_rooms """
        number_rooms = self.value()
        self.assertEqual(type(number_rooms.number_rooms), int)

    def test_number_bathrooms(self):
        """test case for number_bathrooms """
        number_bathrooms = self.value()
        self.assertEqual(type(number_bathrooms.number_bathrooms), int)

    def test_max_guest(self):
        """test case for max_guest """
        max_guest = self.value()
        self.assertEqual(type(max_guest.max_guest), int)

    def test_price_by_night(self):
        """test case for price_by_night """
        price_by_night = self.value()
        self.assertEqual(type(price_by_night.price_by_night), float)

    def test_latitude(self):
        """test case for latitude """
        latitude = self.value()
        self.assertEqual(type(latitude.latitude), float)

    def test_longitude(self):
        """test case for longitude """
        longitude = self.value()
        self.assertEqual(type(longitude.longitude), float)

    def test_amenity_ids(self):
        """test case for amenity_ids """
        amenity_ids = self.value()
        self.assertEqual(type(amenity_ids.amenity_ids), list)
        for amenity_id in amenity_ids.amenity_ids:
            self.assertEqual(type(amenity_id), str)
            self.assertTrue(len(amenity_id) > 0)
