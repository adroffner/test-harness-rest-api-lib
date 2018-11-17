from unittest import TestCase, skipIf

try:
    from flask.testing import FlaskClient

    from testharness.rest_api.clients import flask as flask_clients
    from .server import app
    HAS_FLASK = True
except ImportError:
    app = None
    HAS_FLASK = False
    raise


@skipIf(not HAS_FLASK, 'Flask REST API test require flask')
class FlaskTestingRestApiClientTests(TestCase):
    """ FlaskTestingRestApiClient Tests.

    This code tests the FlaskTestingRestApiClient using a simple REST API in Flask.
    It should prove that the code runs "Flask Testing" with its client.
    """

    def setUp(self):
        self.app = app
        self.client = flask_clients.FlaskTestingRestApiClient(self.app)

    def test_delete(self):
        self.assertEqual(self.app.config.get('TESTING'), True)
        self.assertIsInstance(self.client.test_client, FlaskClient)

        response = self.client.delete('/v1/testing/goodbye', 'you')

        self.assertEqual(response.status_code, 204)

    def test_get(self):
        self.assertEqual(self.app.config.get('TESTING'), True)
        self.assertIsInstance(self.client.test_client, FlaskClient)

        response = self.client.get('/v1/testing/hello')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get('message'), 'hello tester')

    def test_post(self):
        self.assertEqual(self.app.config.get('TESTING'), True)
        self.assertIsInstance(self.client.test_client, FlaskClient)

        expected_json = {'message': 'test in-out'}

        response = self.client.post('/v1/testing/hello', expected_json)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, expected_json)
