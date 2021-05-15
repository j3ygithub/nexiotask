import json
import unittest

from flask import url_for
from flask_testing import TestCase

from apps import create_app, db
from models import User


class TestUserApi(TestCase):
    def create_app(self):
        app = create_app("testing")
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_list(self):
        url = url_for("user.user_list")
        response = self.client.get(url)
        self.assertIsInstance(response.json, list)

    def test_user_create(self):
        url = url_for("user.user_create")
        payload = {
            "name": "Jackson",
            "job_title": "PM",
            "communicate_information": json.dumps(
                {
                    "email": "jackson@gmail.com",
                    "mobile": "09xx-xxx-xxx",
                }
            ),
        }
        response = self.client.post(url, json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, payload)

    def test_user_create_with_invalid_payload(self):
        url = url_for("user.user_create")
        payload = {
            "name": 123,
            "job_title": "PM",
            "communicate_information": json.dumps(
                {
                    "email": "jackson@gmail.com",
                    "mobile": "09xx-xxx-xxx",
                }
            ),
        }
        response = self.client.post(url, json=payload)
        self.assertEqual(response.status_code, 500)

    def test_user_create_with_incomplete_payload(self):
        url = url_for("user.user_create")
        payload = {
            "name": "Jackson",
        }
        response = self.client.post(url, json=payload)
        self.assertEqual(response.status_code, 500)

    def test_user_create_with_duplicated_name(self):
        url = url_for("user.user_create")
        payload = {
            "name": "Jackson",
            "job_title": "PM",
            "communicate_information": json.dumps(
                {
                    "email": "jackson@gmail.com",
                    "mobile": "09xx-xxx-xxx",
                }
            ),
        }
        response = self.client.post(url, json=payload)
        self.assertEqual(response.status_code, 201)
        response = self.client.post(url, json=payload)
        self.assertEqual(response.status_code, 500)

    def test_user_update(self):
        url = url_for("user.user_create")
        payload = {
            "name": "Jackson",
            "job_title": "PM",
            "communicate_information": json.dumps(
                {
                    "email": "jackson@gmail.com",
                    "mobile": "09xx-xxx-xxx",
                }
            ),
        }
        response = self.client.post(url, json=payload)
        self.assertEqual(response.status_code, 201)
        url = url_for("user.user_update", pk=1)
        payload = {
            "name": "Jackson",
            "job_title": "PM",
            "communicate_information": json.dumps({
                "email": "jackson@yahoo.com.tw",
                "mobile": "09xx-xxx-xxx",
            }),
        }
        response = self.client.put(url, json=payload)
        self.assertEqual(response.status_code, 200)

    def test_user_delete(self):
        url = url_for("user.user_create")
        payload = {
            "name": "Jackson",
            "job_title": "PM",
            "communicate_information": json.dumps(
                {
                    "email": "jackson@gmail.com",
                    "mobile": "09xx-xxx-xxx",
                }
            ),
        }
        response = self.client.post(url, json=payload)
        self.assertEqual(response.status_code, 201)
        url = url_for("user.user_destroy", pk=1)
        payload = {
            "name": "Jackson",
            "job_title": "PM",
            "communicate_information": json.dumps({
                "email": "jackson@yahoo.com.tw",
                "mobile": "09xx-xxx-xxx",
            }),
        }
        response = self.client.delete(url, json=payload)
        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main()
