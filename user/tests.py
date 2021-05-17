import json
import unittest

from flask import url_for
from flask_testing import TestCase

from app import create_app, db
from core import status_codes


class UserViewTestCase(TestCase):
    """Test the views of user APP"""

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
        self.assertEqual(response.status_code, status_codes.CREATED)
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
        self.assertEqual(response.status_code, status_codes.BAD_REQUEST)

    def test_user_create_with_incomplete_payload(self):
        url = url_for("user.user_create")
        payload = {
            "name": "Jackson",
        }
        response = self.client.post(url, json=payload)
        self.assertEqual(response.status_code, status_codes.BAD_REQUEST)

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
        self.assertEqual(response.status_code, status_codes.CREATED)
        response = self.client.post(url, json=payload)
        self.assertEqual(response.status_code, status_codes.BAD_REQUEST)

    def test_user_retrieve(self):
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
        self.assertEqual(response.status_code, status_codes.CREATED)
        url = url_for("user.user_retrieve", pk=1)
        response = self.client.get(url, json=payload)
        self.assertEqual(response.status_code, status_codes.OK)
        expected_payload = dict(**payload, id=1)
        self.assertEqual(response.json, expected_payload)

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
        self.assertEqual(response.status_code, status_codes.CREATED)
        url = url_for("user.user_update", pk=1)
        payload = {
            "name": "Jackson",
            "job_title": "PM",
            "communicate_information": json.dumps(
                {
                    "email": "jackson@yahoo.com.tw",
                    "mobile": "09xx-xxx-xxx",
                }
            ),
        }
        response = self.client.put(url, json=payload)
        self.assertEqual(response.status_code, status_codes.OK)

    def test_user_update_with_invalid_payload(self):
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
        self.assertEqual(response.status_code, status_codes.CREATED)
        url = url_for("user.user_update", pk=1)
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
        response = self.client.put(url, json=payload)
        self.assertEqual(response.status_code, status_codes.BAD_REQUEST)

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
        self.assertEqual(response.status_code, status_codes.CREATED)
        url = url_for("user.user_destroy", pk=1)
        payload = {
            "name": "Jackson",
            "job_title": "PM",
            "communicate_information": json.dumps(
                {
                    "email": "jackson@yahoo.com.tw",
                    "mobile": "09xx-xxx-xxx",
                }
            ),
        }
        response = self.client.delete(url, json=payload)
        self.assertEqual(response.status_code, status_codes.NO_CONTENT)


if __name__ == "__main__":
    unittest.main()
