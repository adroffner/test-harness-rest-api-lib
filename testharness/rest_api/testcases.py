""" REST API Test Harness for Python unittest

Use these unittest.TestCase subclasses to run REST API tests.
"""

import logging
import unittest

from .client.live import RestApiClient

log = logging.getLogger(__name__)


class LiveRestApiTestCase(unittest.TestCase):
    """ Live REST API Test Case.

    This Test Case provides a QA or Regression testing plan.

    The REST API service is deployed to a known "hostname" already.
    Each test case method should send an HTTP request to a server endpoint
    to validate its health.
    """

    # Change these constants in the subclass to the real server.
    SCHEME = 'http'  # Change to "https" SSL as needed.
    HOST = 'example.com'
    PORT = 80

    @classmethod
    def setUpClass(cls):
        """ prepare HTTP client """
        cls.client = RestApiClient(cls.HOST, port=cls.PORT, scheme=cls.SCHEME)
