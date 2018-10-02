import sys
sys.path.append('../')
from flask import Flask
from flask_testing import LiveServerTestCase
from app import main_app as app
import requests
import unittest

class BaseTest(LiveServerTestCase):

    def create_app(self):
        app.config['TESTING'] = True

        app.config['LIVESERVER_PORT'] = 9999
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_server_is_up_and_running(self):
        response = requests.get(url=self.get_server_url())
        self.assertEqual(response.status_code, 200)
