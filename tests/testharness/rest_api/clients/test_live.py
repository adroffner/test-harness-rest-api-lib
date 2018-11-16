from unittest import TestCase, mock

from testharness.rest_api.clients import live


class RestApiClientTests(TestCase):

    def test_delete(self):
        client = live.RestApiClient('test.example.com')

        mock_response = mock.MagicMock()

        with mock.patch('testharness.rest_api.clients.live.requests.delete',
                        return_value=mock_response) as mock_delete:
            response = client.delete('/v1/test/object', 'asdf')

            mock_delete.assert_called_with(
                client.delete_url('/v1/test/object', 'asdf'),
                headers=client._add_rest_headers(),
                timeout=client.response_timeout)
            self.assertEqual(response, mock_response)

    def test_get(self):
        client = live.RestApiClient('test.example.com')

        mock_response = mock.MagicMock()

        with mock.patch('testharness.rest_api.clients.live.requests.get',
                        return_value=mock_response) as mock_get:
            response = client.get('/v1/test/object', query={'code': 'asdf'})

            mock_get.assert_called_with(
                client.get_url('/v1/test/object', query={'code': 'asdf'}),
                headers=client._add_rest_headers(),
                timeout=client.response_timeout)
            self.assertEqual(response, mock_response)

    def test_post(self):
        client = live.RestApiClient('test.example.com')

        mock_response = mock.MagicMock()

        with mock.patch('testharness.rest_api.clients.live.requests.post',
                        return_value=mock_response) as mock_post:
            response = client.post('/v1/test/object', {'code': 'asdf'})

            (full_url, post_payload) = client.post_url('/v1/test/object', {'code': 'asdf'})
            mock_post.assert_called_with(
                full_url,
                json=post_payload,
                headers=client._add_rest_headers(),
                timeout=client.response_timeout)
            self.assertEqual(response, mock_response)
