#!/usr/bin/env python

import unittest
import requests

# Base URL for your API
base_url = 'http://localhost:5000'

# Test data
test_data = {
    'name': 'John',
}

class TestAPI(unittest.TestCase):

    def setUp(self):
        # Optional: You can perform setup actions here before each test method runs.
        pass

    def tearDown(self):
        # Optional: You can perform cleanup actions here after each test method runs.
        pass

    def test_create_person(self):
        response = create_person(test_data['name'])
        self.assertEqual(response.status_code, 201)

    def test_get_person(self):
        response = get_person(test_data['name'])
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed to check the response data

    def test_update_person(self):
        new_name = 'Updated Name'
        response = update_person(test_data['name'], new_name)
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed to check the response data

    def test_delete_person(self):
        response = delete_person(test_data['name'])
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    # Define the functions for CRUD operations (create_person, get_person, etc.) here

    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAPI)

    # Run the tests
    unittest.TextTestRunner(verbosity=2).run(suite)
