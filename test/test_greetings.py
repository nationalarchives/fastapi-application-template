import json
import unittest

from fastapi.testclient import TestClient

from app import create_app


class HealthcheckBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("config.Test")
        self.client = TestClient(self.app)
        self.domain = "http://localhost"

    def test_hello(self):
        rv = self.client.get(
            f"{self.app.state.config.get('BASE_URI')}/greetings/hello/",
            params={"name": "John Smith"},
        )
        self.assertEqual(rv.status_code, 200)
        response_json = json.loads(rv.text)
        self.assertIn("message", response_json)
        self.assertEqual(response_json["message"], "Hello, John Smith")

    def test_custom_greeting(self):
        rv = self.client.get(
            f"{self.app.state.config.get('BASE_URI')}/greetings/Heya/",
            params={"name": "John Smith"},
        )
        self.assertEqual(rv.status_code, 200)
        response_json = json.loads(rv.text)
        self.assertIn("message", response_json)
        self.assertEqual(response_json["message"], "Heya, John Smith")
