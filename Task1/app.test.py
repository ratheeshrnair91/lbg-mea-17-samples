import unittest
import requests
import os

HOST = os.getenv('HOST', 'test')
PORT = os.getenv('PORT', 5500)
BASE_URL = f"http://{HOST}:{PORT}"

class TestApp(unittest.TestCase):
    def test_app_response(self):
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn('JenkinsKubernetes', response.text)

unittest.main()