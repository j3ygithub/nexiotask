import json

from flask_testing import TestCase

from apps import create_app, db


class TestUserApi(TestCase):

    def create_app(self):
        return create_app("testing")

    def setUp(self):
        db.create_all()
        self.BASE_URL = "http://127.0.0.1:5000"

    def test_user_list(self):
        path = "/users"
        url = self.BASE_URL + path
        response = self.client.get(url)
        self.assertIsInstance(response.json, list)

    def test_user_create(self):
        path = "/users"
        url = self.BASE_URL + path
        payload = {
            "name": "Jackson",
            "job_title": "PM",
            "communicate_information": json.dumps({
                "email": "jackson@gmail.com",
                "mobile": "09xx-xxx-xxx",
            }),
        }
        response = self.client.post(url, json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, payload)

    # def test_user_update(self):
    #     path = "/users/1"
    #     url = self.BASE_URL + path
    #     payload = {
    #         "name": "Jackson",
    #         "job_title": "PM",
    #         "communicate_information": json.dumps({
    #             "email": "jackson@gmail.com",
    #             "mobile": "09xx-xxx-xxx",
    #         }),
    #     }
    #     response = self.client.put(url, json=payload)
    #     self.assertEqual(response.status_code, 200)

    # def test_user_delete(self):
    #     path = "/users/1"
    #     url = self.BASE_URL + path
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, 204)

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == "__main__":
    unittest.main()
