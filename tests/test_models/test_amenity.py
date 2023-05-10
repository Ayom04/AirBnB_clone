#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_amenity(test_basemodel):
    """ test cases for amenity"""
    def __init__(self, *args, **kwargs):
        """ test initialization """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_amenity_create(self):
        """test case for amenity create"""
        amenity = Amenity()
        amenity.name = "Test Amenity"
        amenity.save()
        self.assertEqual(amenity.name, "Test Amenity")
        amenity.delete()

    def test_amenity_update(self):
        """test case for amenity update"""
        amenity = Amenity()
        amenity.name = "Test Amenity"
        amenity.save()
        amenity.name = "Test Amenity Updated"
        amenity.save()
        self.assertEqual(amenity.name, "Test Amenity Updated")
        amenity.delete()

    def test_amenity_delete(self):
        """ test case for amenity delete"""
        amenity = Amenity()
        amenity.name = "Test Amenity"
        amenity.save()
        amenity.delete()
        self.assertEqual(len(Amenity.objects.all()), 0)
        amenity.delete()

    def test_amenity_list(self):
        """ test cases when a list is passed in"""
        amenity = Amenity()
        amenity.name = "Test Amenity"
        amenity.save()
        amenity2 = Amenity()
        amenity2.name = "Test Amenity2"
        amenity2.save()
        self.assertEqual(len(Amenity.objects.all()), 2)
        self.assertEqual(Amenity.objects.all()[0].name, "Test Amenity")
        self.assertEqual(Amenity.objects.all()[1].name, "Test Amenity2")
        amenity.delete()
        amenity2.delete()

    def test_amenity_get(self):
        """ test cases for get"""
        amenity = Amenity()
        amenity.name = "Test Amenity"
        amenity.save()
        amenity2 = Amenity()
        amenity2.name = "Test Amenity2"
        amenity2.save()
        self.assertEqual(Amenity.objects.all()[0].name, "Test Amenity")
        self.assertEqual(Amenity.objects.all()[1].name, "Test Amenity2")
        self.assertEqual(Amenity.objects.get(name="Test Amenity").name,
                         "Test Amenity")
        self.assertEqual(Amenity.objects.get(name="Test Amenity2").name,
                         "Test Amenity2")
        amenity.delete()
        amenity2.delete()
