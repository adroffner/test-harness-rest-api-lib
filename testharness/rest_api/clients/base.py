""" Base REST API Client

The HTTP REST Client interface.
"""

import logging

from urllib.parse import urlencode

# log package name.
log = logging.getLogger('.'.join(__name__.split('.')[:-1]))


class BaseRestApiClient(object):
    """ Base REST API Client.

    This HTTP client describes a REST API requests interface.
    """

    def __init__(self, hostname, port=80, scheme='http', response_timeout=10.0):
        """ Init RestApiClient.

        :param str hostname: server hostname
        :param int port: server port number
        :param str scheme: URL scheme is "http" unless set to "https" for SSL
        :param float response_timeout: wait timeout for a response (in seconds)
        """

        self.host_url = self._set_host_url(scheme, hostname, port)
        self.response_timeout = response_timeout

    def _set_host_url(self, scheme, hostname, port):
        """ Set Host URL.

        Compose the host URL base for the REST API site.

        Example:
            "http://example.com:80"
        """

        host_url = '{}://{}:{}'.format(scheme, hostname, port)
        return host_url

    def _get_full_url(self, rest_url, extra_path=[]):
        """ Get Full URL.

        Compose full URL for the relative rest_url and extra_path.

        :param rest_url: REST API relative URL
        :param extra_path: a list of extra path terms
        :returns: a full URL
        """

        url_list = [self.host_url, rest_url]
        url_list.extend(extra_path)
        full_url = ''.join(url_list)
        return full_url

    def _add_rest_headers(self, headers={}):
        headers['Content-Type'] = 'application/json'
        return headers

    # =================================================
    # Compose URLs.
    # =================================================

    def delete_url(self, rest_url, object_key):
        """ DELETE URL.

        :param rest_url: a relative URL on the API
        :param object_key: a key or id to delete the object
        :returns: DELETE endpoint URL
        """

        full_url = self._get_full_url(rest_url, extra_path=['/', repr(object_key)])
        log.debug('Client DELETE {}'.format(full_url))

        return full_url

    def get_url(self, rest_url, query={}):
        """ GET URL with Query String.

        :param rest_url: a relative URL on the API
        :param query: query string params as dict
        :returns: GET endpoint URL
        """

        full_url = self._get_full_url(rest_url)
        if isinstance(query, dict) and query:
            query_string = urlencode(query)
            full_url = '?'.join([full_url, query_string])
        log.debug('Client GET {}'.format(full_url))

        return full_url

    def post_url(self, rest_url, payload_dict):
        """ POST URL with Input Payload.

        :param rest_url: a relative URL on the API
        :param payload_dict: JSON payload to post
        :returns: POST endpoint tuple (url, payload)
        """

        full_url = self._get_full_url(rest_url)
        log.debug('Client POST {} payload={}'.format(full_url, payload_dict))

        return (full_url, payload_dict)

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
        raise NotImplementedError('DELETE Endpoint: {}'.format(full_url))

    def get(self, rest_url, query={}):
        """ GET from REST API Endpoint.

        :param rest_url: a relative URL on the API
        :param query: query string params as dict
        returns: an HTTP response
        """

        full_url = self.get_url(rest_url, query=query)
        raise NotImplementedError('GET Endpoint: {}'.format(full_url))

    def post(self, rest_url, payload_dict):
        """ POST to REST API Endpoint with payload.

        :param rest_url: a relative URL on the API
        :param payload_dict: JSON payload to post
        returns: an HTTP response
        """

        full_url = self.post_url(rest_url, payload_dict)
        raise NotImplementedError('POST Endpoint: {} payload={}'.format(full_url, payload_dict))


if __name__ == '__main__':  # pragma: no cover
    log.setLevel(logging.DEBUG)
    log.addHandler(logging.StreamHandler())

    client = BaseRestApiClient('test.example.com')
    sample_rest_url = '/v1/sample/object'

    print('Host URL: ', client.host_url)

    try:
        client.delete(sample_rest_url, 'ID')
    except NotImplementedError as e:
        print(str(e))
        print()

    try:
        client.get(sample_rest_url, {'hello': 'testing world 100%'})
    except NotImplementedError as e:
        print(str(e))
        print()

    try:
        client.post(sample_rest_url, {'hello': 'testing world 100%'})
    except NotImplementedError as e:
        print(str(e))
        print()
