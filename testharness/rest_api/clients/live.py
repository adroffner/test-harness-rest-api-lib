""" Live REST API Client

The Live HTTP REST Client implementation.
"""

import logging
import requests

from .base import BaseRestApiClient

# log package name.
log = logging.getLogger('.'.join(__name__.split('.')[:-1]))


class RestApiClient(BaseRestApiClient):
    """ Live REST API Client.

    This HTTP client provides a REST API requests implementation.
    """

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
        resp = requests.delete(full_url, headers=self._add_rest_headers(),
                               timeout=self.response_timeout)
        return resp

    def get(self, rest_url, query={}):
        """ GET from REST API Endpoint.

        :param rest_url: a relative URL on the API
        :param query: query string params as dict
        returns: an HTTP response
        """

        full_url = self.get_url(rest_url, query=query)
        resp = requests.get(full_url, headers=self._add_rest_headers(),
                            timeout=self.response_timeout)
        return resp

    def post(self, rest_url, payload_dict):
        """ POST to REST API Endpoint with payload.

        :param rest_url: a relative URL on the API
        :param payload_dict: JSON payload to post
        returns: an HTTP response
        """

        (full_url, payload_dict) = self.post_url(rest_url, payload_dict)
        resp = requests.post(
            full_url,
            json=payload_dict,
            headers=self._add_rest_headers(),
            timeout=self.response_timeout)
        return resp


if __name__ == '__main__':  # pragma: no cover
    log.setLevel(logging.DEBUG)
    log.addHandler(logging.StreamHandler())

    client = RestApiClient('micro.dev.att.com', port=8030)
    sample_rest_url = '/osscwl/servers'

    print('Host URL: ', client.host_url)

    response = client.delete(sample_rest_url, 'ID')
    print('DELETE: "{}" status={}'.format(
        response.content.decode('utf8'), response.status_code))
    print()

    response = client.get(sample_rest_url, {'hello': 'testing world 100%'})
    print('GET: "{}" status={}'.format(
        response.content.decode('utf8'), response.status_code))
    print()

    response = client.post(sample_rest_url, {'hello': 'testing world 100%'})
    print('POST: "{}" status={}'.format(
        response.content.decode('utf8'), response.status_code))
    print()
