import unittest
import requests
import os

HOST = os.getenv('HOST', 'test')
BASE_URL = f"http://{HOST}:5500"

class TestApp(unittest.TestCase):
    def test_app_response(self):
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn('JenkinsKubernetes', response.text)

unittest.main()