#!/usr/bin/python3
"""
Unit tests for State class
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_instance_creation(self):
        my_state = State()
        self.assertIsInstance(my_state, State)

    def test_attributes(self):
        my_state = State()
        self.assertTrue(hasattr(my_state, 'id'))
        self.assertTrue(hasattr(my_state, 'created_at'))
        self.assertTrue(hasattr(my_state, 'updated_at'))

    def test_str_method(self):
        my_state = State()
        self.assertIsInstance(str(my_state), str)

    def test_save_method(self):
        my_state = State()
        old_updated_at = my_state.updated_at
        my_state.save()
        self.assertNotEqual(old_updated_at, my_state.updated_at)

    def test_capital_attribute(self):
        my_state = State()
        my_state.capital = "Albany"
        self.assertEqual(my_state.capital, "Albany")

    def test_population_attribute(self):
        # Add a new test for the population attribute.
        my_state = State()
        my_state.population = 1000000
        self.assertEqual(my_state.population, 1000000)


if __name__ == '__main__':
    unittest.main()
