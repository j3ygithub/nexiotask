import unittest
import requests
from settings import HOST, PORT


class TestUserApi(unittest.TestCase):
    def setUp(self):
        self.BASE_URL = f'http://{HOST}:{PORT}'
        self.session = requests.session()

    def test_user_list(self):
        path = '/users'
        url = self.BASE_URL + path
        response = self.session.get(url)
        data = response.json()
        self.assertIsInstance(data, list)

    def test_user_create(self):
        path = '/users'
        url = self.BASE_URL + path
        data = {
            "name": "Jackson",
            "job_title": "PM",
            "communicate_information": "123",
        }
        response = self.session.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), data)

    def test_user_delete(self):
        path = '/users/1'
        url = self.BASE_URL + path
        response = self.session.delete(url)
        self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()
