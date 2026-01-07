import unittest

from fastapi.testclient import TestClient

from app import create_app


class HealthcheckBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("config.Test")
        self.client = TestClient(self.app)
        self.domain = "http://localhost:83"

    def test_build_endpoint(self):
        rv = self.client.get("/build/")
        self.assertEqual(rv.status_code, 200)
        self.assertIn("containerImage", rv.json())
        self.assertIn("buildVersion", rv.json())
