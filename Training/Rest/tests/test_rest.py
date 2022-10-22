"""Test for rest api."""
import unittest

from flask import Flask

from main import configure_routes


class TestCalc(unittest.TestCase):
    """Class for testing REST API."""

    def setUp(self):
        """Set dictionary for testing and start router."""
        self.info = {}
        self.info['app_name'] = "Test"
        self.info['version'] = "v1-test"
        self.info['namespace'] = "TestNS"
        self.info['pod'] = "TestPOD"
        self.info['node'] = "TestNODE"
        self.app = Flask(__name__)
        configure_routes(self.app, self.info)
        self.client = self.app.test_client()
        self.url = '/'
        self.response = self.client.get(self.url)

    def test_should_return_hello(self):
        """Test for testing base route"""
        self.assertEqual(b'Hello from Test', self.response.get_data())
        self.assertEqual(200, self.response.status_code)


if __name__ == '__main__':
    unittest.main()
