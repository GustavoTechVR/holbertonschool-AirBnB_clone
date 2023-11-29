# test_city.py

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_instance_creation(self):
        my_city = City()
        self.assertIsInstance(my_city, City)

    def test_attributes(self):
        my_city = City()
        self.assertTrue(hasattr(my_city, 'id'))
        self.assertTrue(hasattr(my_city, 'created_at'))
        self.assertTrue(hasattr(my_city, 'updated_at'))
        self.assertIsInstance(my_city.id, str)
        self.assertIsInstance(my_city.created_at, datetime.datetime)
        self.assertIsInstance(my_city.updated_at, datetime.datetime)

    def test_str_method(self):
        my_city = City()
        str_representation = str(my_city)
        self.assertIn('City', str_representation)
        self.assertIn('id', str_representation)
        self.assertIn('created_at', str_representation)
        self.assertIn('updated_at', str_representation)

    def test_save_method(self):
        my_city = City()
        old_updated_at = my_city.updated_at
        my_city.save()
        self.assertNotEqual(old_updated_at, my_city.updated_at)

    def test_custom_functionality(self):
        my_city = City()
        my_city.set_custom_property("Custom Value")
        self.assertEqual(my_city.get_custom_property(), "Custom Value")

    def test_edge_case(self):
        my_city = City(name="")
        self.assertEqual(my_city.name, "")
        # Add more assertions for other attributes if needed


if __name__ == '__main__':
    unittest.main()
