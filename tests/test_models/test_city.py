#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """class to test for City"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_init(self):
        """ """
        pass

    def test_get_name(self):
        """ """
        pass

    def test_set_name(self):
        """ """
        pass

    def test_get_value(self):
        """ """
        pass

    def test_get_value(self):
        """ """
        pass

    def test_set_value(self):
        """ """
        pass

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_state_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_name), str)

    def test_state_id(self):
        """ to test for state_id """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_instance(self):
        """Test that an instance of City can be created"""
        city = City()
        self.assertIsInstance(city, City)

    def test_state_id_attribute(self):
        """Test that City has a state_id attribute"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))

    def test_state_id_type(self):
        """Test that the state_id attribute of City is a string"""
        city = City()
        self.assertIsInstance(city.state_id, str)

    def test_name_attribute(self):
        """Test that City has a name attribute"""
        city = City()
        self.assertTrue(hasattr(city, 'name'))

    def test_name_type(self):
        """Test that the name attribute of City is a string"""
        city = City()
        self.assertIsInstance(city.name, str)

    def test_name_default_value(self):
        """Test default value of name attribute of City is an empty string"""
        city = City()
        self.assertEqual(city.name, '')

    def test_str_representation(self):
        """Test that the __str__ method of City returns the expected string"""
        city = City(state_id='CA', name='San Francisco')
        self.assertEqual(str(city), "[City] (id: {}) {} {}"
                         .format(city.id, city.state_id, city.name))

    def test_repr_representation(self):
        """Test that the __repr__ method of City returns the expected string"""
        city = City(state_id='CA', name='San Francisco')
        self.assertEqual(repr(city), "[City] (id: {}) {} {}"
                         .format(city.id, city.state_id, city.name))

    def test_hash_representation(self):
        """Test that the __hash__ method of City returns the expected string"""
        city = City(state_id='CA', name='San Francisco')
        self.assertEqual(hash(city), hash(city.state_id) + hash(city.name))

    def test_eq_representation(self):
        """Test that the __eq__ method of City returns the expected string"""
        city1 = City(state_id='CA', name='San Francisco')
        city2 = City(state_id='CA', name='San Francisco')
        self.assertEqual(city1, city2)

    def test_ne_representation(self):
        """Test that the __ne__ method of City returns the expected string"""
        city1 = City(state_id='CA', name='San Francisco')
        city2 = City(state_id='CA', name='San Francisco')
        self.assertNotEqual(city1, city2)

    def test_lt_representation(self):
        """Test that the __lt__ method of City returns the expected string"""
        city1 = City(state_id='CA', name='San Francisco')
        city2 = City(state_id='CA', name='San Francisco')
        self.assertLess(city1, city2)

    def test_le_representation(self):
        """Test that the __le__ method of City returns the expected string"""
        city1 = City(state_id='CA', name='San Francisco')
        city2 = City(state_id='CA', name='San Francisco')
        self.assertLessEqual(city1, city2)

    def test_gt_representation(self):
        """Test that the __gt__ method of City returns the expected string"""
        city1 = City(state_id='CA', name='San Francisco')
        city2 = City(state_id='CA', name='San Francisco')
        self.assertGreater(city1, city2)

    def test_ge_representation(self):
        """Test that the __ge__ method of City returns the expected string"""
        city1 = City(state_id='CA', name='San Francisco')
        city2 = City(state_id='CA', name='San Francisco')
        self.assertGreaterEqual(city1, city2)

    def test_basemodel_name_isCorrect(self):
        """Test that the name attribute of City is correct"""
        city = City(state_id='CA', name='San Francisco')
        self.assertEqual(city.name, 'San Francisco')

    def test_basemodel_id_isCorrect(self):
        """Test that the id attribute of City is correct"""
        city = City(state_id='CA', name='San Francisco')
        self.assertEqual(city.id, 'CA')

    def test_basemodel_state_id_isCorrect(self):
        """Test that the state_id attribute of City is correct"""
        city = City(state_id='CA', name='San Francisco')
        self.assertEqual(city.state_id, 'CA')

    def test_basemodel_state_name_isCorrect(self):
        """Test that the state_name attribute of City is correct"""
        city = City(state_id='CA', name='San Francisco')
        self.assertEqual(city.state_name, 'San Francisco')

    def test_basemodel_city_id_isCorrect(self):
        """Test that the city_id attribute of City is correct"""
        city = City(state_id='CA', name='San Francisco')
        self.assertEqual(city.city_id, '')

    def test_basemodel_city_name_isCorrect(self):
        """Test that the city_name attribute of City is correct"""
        city = City(state_id='CA', name='San Francisco')
        self.assertEqual(city.city_name, '')
