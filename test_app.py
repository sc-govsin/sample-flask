import unittest
from flask import Flask
from flask_testing import TestCase
from app import app


class TestApp(TestCase):
    def create_app(self):
        return app

    def test_hello_world(self):
        response = self.client.get("/")
        self.assert200(response)
        self.assertTemplateUsed("index.html")


if __name__ == "__main__":
    unittest.main()
