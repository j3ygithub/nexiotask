import unittest

import views
from flask import Flask, url_for
import requests
from flask_testing import TestCase
from settings import HOST, PORT


class TestUserApi(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_user_list(self):
        response = self.client.get(url_for('user_list'))
        print(response)
        data = response.json
        self.assertIsInstance(data, list)

    # def test_user_create(self):
    #     path = '/users'
    #     url = self.BASE_URL + path
    #     data = {
    #         "name": "Jackson",
    #         "job_title": "PM",
    #         "communicate_information": "123",
    #     }
    #     response = self.session.post(url, data)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(response.json(), data)

    # def test_user_update(self):
    #     path = '/users/1'
    #     url = self.BASE_URL + path
    #     data = {
    #         "name": "Jackson",
    #         "job_title": "PM",
    #         "communicate_information": "123",
    #     }
    #     response = self.session.put(url, data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), data)

    # def test_user_delete(self):
    #     path = '/users/1'
    #     url = self.BASE_URL + path
    #     response = self.session.delete(url)
    #     self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()
