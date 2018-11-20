from unittest import TestCase

from testharness.rest_api.clients import base


class BaseRestApiClientTests(TestCase):

    def test_init_client_defaults(self):
        client = base.BaseRestApiClient('test.example.com')

        self.assertEqual(client.host_url, 'http://test.example.com:80')
        self.assertEqual(client.response_timeout, 10.0)

    def test_init_client_change_timeout(self):
        client = base.BaseRestApiClient('test.example.com', response_timeout=13.5)

        self.assertEqual(client.host_url, 'http://test.example.com:80')
        self.assertEqual(client.response_timeout, 13.5)

    def test_init_client_ssl(self):
        client = base.BaseRestApiClient('test.secure.example.com', scheme='https', port=443)

        self.assertEqual(client.host_url, 'https://test.secure.example.com:443')
        self.assertEqual(client.response_timeout, 10.0)

    # =========================================================

    def test__add_rest_headers(self):
        client = base.BaseRestApiClient('test.example.com')

        headers = client._add_rest_headers()
        self.assertIn('Content-Type', headers)
        self.assertEqual(headers['Content-Type'], 'application/json')

    def test__add_rest_headers_parameter(self):
        client = base.BaseRestApiClient('test.example.com')

        original_headers = {
            'User-Agent': 'test/0.1',
            'Content-length': 0
        }
        self.assertNotIn('Content-Type', original_headers)

        expected_headers = original_headers.copy()
        expected_headers['Content-Type'] = 'application/json'

        headers = client._add_rest_headers(headers=original_headers)
        self.assertIn('Content-Type', headers)
        self.assertEqual(headers['Content-Type'], 'application/json')
        self.assertEqual(headers, expected_headers)

    # =========================================================

    def test_delete_url(self):
        client = base.BaseRestApiClient('test.example.com')

        expected_url = 'http://test.example.com:80/v1/test/object/1234'

        real_url = client.delete_url('/v1/test/object', 1234)
        self.assertEqual(real_url, expected_url)

    def test_get_url_no_query(self):
        client = base.BaseRestApiClient('test.example.com')

        expected_url = 'http://test.example.com:80/v1/test/object'

        real_url = client.get_url('/v1/test/object')
        self.assertEqual(real_url, expected_url)

    def test_get_url_with_query(self):
        client = base.BaseRestApiClient('test.example.com')

        input_query = {
            'count': 5,
            'name': 'hello world'
        }
        expected_url = 'http://test.example.com:80/v1/test/object?count=5&name=hello+world'

        real_url = client.get_url('/v1/test/object', query=input_query)
        self.assertEqual(real_url, expected_url)

    def test_post_url(self):
        client = base.BaseRestApiClient('test.example.com')

        input_payload = {
            'pass': 'through',
            'in': 'tuple'
        }
        expected_url = 'http://test.example.com:80/v1/test/object'

        (real_url, expected_payload) = client.post_url('/v1/test/object', input_payload)
        self.assertEqual(real_url, expected_url)
        self.assertEqual(input_payload, expected_payload)

    # =========================================================

    def test_delete_not_implemented(self):
        client = base.BaseRestApiClient('test.example.com')

        with self.assertRaisesRegex(NotImplementedError, r'^DELETE Endpoint:'):
            client.delete('/v1/test/object', 'asdf')

    def test_get_not_implemented(self):
        client = base.BaseRestApiClient('test.example.com')

        with self.assertRaisesRegex(NotImplementedError, r'^GET Endpoint:'):
            client.get('/v1/test/object', query={'code': 'asdf'})

    def test_post_not_implemented(self):
        client = base.BaseRestApiClient('test.example.com')

        with self.assertRaisesRegex(NotImplementedError, r'^POST Endpoint:'):
            client.post('/v1/test/object', {'code': 'asdf'})
