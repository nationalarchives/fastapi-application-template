import unittest

from fastapi.testclient import TestClient

from app import create_app


class HealthcheckBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("config.Test")
        self.client = TestClient(self.app)
        self.domain = "http://localhost:83"

    def test_healthcheck_live(self):
        rv = self.client.get("/healthcheck/live/")
        self.assertEqual(rv.status_code, 200)
        self.assertIn("ok", rv.text)

    # TODO
    # def test_trailing_slash_redirects(self):
    #     rv = self.client.get("/healthcheck/live")
    #     self.assertEqual(rv.status_code, 307)
    #     self.assertEqual(rv.location, f"{self.domain}/healthcheck/live/")
