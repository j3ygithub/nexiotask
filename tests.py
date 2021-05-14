import json
import unittest

import requests

from scripts.create_fake_users import create_fake_users
from scripts.db_create_all import db_create_all
from scripts.db_drop_all import db_drop_all
from settings import app, HOST, PORT


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"


class TestUserApi(unittest.TestCase):
    def setUp(self):
        db_drop_all()
        db_create_all()
        create_fake_users()
        self.app = app
        self.app.run()
        self.BASE_URL = f"http://{HOST}:{PORT}"
        self.session = requests.session()

    def test_user_list(self):
        path = "/users"
        url = self.BASE_URL + path
        response = self.session.get(url)
        self.assertIsInstance(response.json(), list)

    def test_user_create(self):
        path = "/users"
        url = self.BASE_URL + path
        data = {
            "name": "Jackson",
            "job_title": "PM",
            "communicate_information": json.dumps({
                "email": "jackson@gmail.com",
                "mobile": "09xx-xxx-xxx",
            }),
        }
        response = self.session.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), data)

    def test_user_update(self):
        path = "/users/1"
        url = self.BASE_URL + path
        data = {
            "name": "Jackson",
            "job_title": "PM",
            "communicate_information": json.dumps({
                "email": "jackson@gmail.com",
                "mobile": "09xx-xxx-xxx",
            }),
        }
        response = self.session.put(url, data)
        self.assertEqual(response.status_code, 200)

    def test_user_delete(self):
        path = "/users/1"
        url = self.BASE_URL + path
        response = self.session.delete(url)
        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main()
