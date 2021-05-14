import json
import unittest

from apps import create_app

app = create_app("testing")


class TestUserApi(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = app.test_client()
        self.BASE_URL = "http://127.0.0.1:5000"

    def test_user_list(self):
        path = "/users"
        url = self.BASE_URL + path
        response = self.client.get(url)
        self.assertIsInstance(response.json, list)

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
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, data)

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
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)

    def test_user_delete(self):
        path = "/users/1"
        url = self.BASE_URL + path
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main()
