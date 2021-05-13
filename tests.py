import unittest
import requests


class TestUserApi(unittest.TestCase):
    def setUp(self):
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
        }
        response = self.session.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), data)


if __name__ == '__main__':
    unittest.main()
