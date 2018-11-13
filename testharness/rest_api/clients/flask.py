""" Flask Testing REST API Client

The Flask Testing HTTP REST Client implemetation.
"""

import logging

from .base import BaseRestApiClient

# log package name.
log = logging.getLogger('.'.join(__name__.split('.')[:-1]))


class FlaskTestingRestApiClient(BaseRestApiClient):
    """ Flask Testing REST API Client.

    This HTTP client binds a Flask app to a REST API requests implemetation.
    """

    def __init__(self, flask_app):
        """ Init RestApiClient.

        :param flask.App flask_app: Flask application object to make test client
        :param float response_timeout: wait timeout for a response (in seconds)
        """

        super().__init__('flask.example.com')

        self.app = flask_app
        self.app.config['TESTING'] = True
        self.test_client = self.app.test_client()

    def _set_host_url(self, scheme, hostname, port):
        """ Set Host URL.

        Blank string to use only relative testing URLs.
        """

        return ''

    # =================================================
    # REST API: HTTP Methods
    # =================================================

    def delete(self, rest_url, object_key):
        """ DELETE from REST API Endpoint.

        :param rest_url: a relative URL on the API
        :param object_key: a key or id to delete the object
        returns: an HTTP response
        """

        full_url = self.delete_url(rest_url, object_key)
        return self.test_client.delete(full_url)

    def get(self, rest_url, query={}):
        """ GET from REST API Endpoint.

        :param rest_url: a relative URL on the API
        :param query: query string params as dict
        returns: an HTTP response
        """

        full_url = self.get_url(rest_url, query=query)
        return self.test_client.get(full_url, headers=self._add_rest_headers())

    def post(self, rest_url, payload_dict):
        """ POST to REST API Endpoint with payload.

        :param rest_url: a relative URL on the API
        :param payload_dict: JSON payload to post
        returns: an HTTP response
        """

        full_url = self.post_url(rest_url, payload_dict)
        return self.test_client.post(full_url, data=payload_dict,
                                     headers=self._add_rest_headers())


if __name__ == '__main__':  # pragma: no cover
    from unittest import mock

    log.setLevel(logging.DEBUG)
    log.addHandler(logging.StreamHandler())

    # Mock the flask application object.
    mock_app = mock.MagicMock()
    mock_app.config = {}
    mock_app.test_client.return_value = mock.MagicMock(side_effect=['one', 'two', 'three'])

    client = FlaskTestingRestApiClient(mock_app)
    sample_rest_url = '/v1/sample/object'

    print('Host URL: ', client.host_url)

    response = client.delete(sample_rest_url, 'ID')
    print('DELETE: "{}"'.format(response.data))
    print()

    response = client.get(sample_rest_url, {'hello': 'testing world 100%'})
    print('GET: "{}"'.format(response.data))
    print()

    response = client.post(sample_rest_url, {'hello': 'testing world 100%'})
    print('POST: "{}"'.format(response.data))
    print()
