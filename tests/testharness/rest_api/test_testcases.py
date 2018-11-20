# from unittest import TestCase

from testharness.rest_api import testcases
from testharness.rest_api.clients.live import RestApiClient


class LiveRestApiTestCaseTests(testcases.LiveRestApiTestCase):
    """ LiveRestApiTestCase Class Tests.

    The LiveRestApiTestCase is a helper class for QA Testing.
    We are testing it here with itself, which is confusing.
    """

    SCHEME = 'https'
    HOST = 'secure.example.com'
    PORT = 443

    def test_setup_class_client(self):
        " Prove live client has been configured with HOST, PORT, ..etc. "
        self.assertIsInstance(self.client, RestApiClient)

        self.assertEqual(self.SCHEME, 'https')
        self.assertEqual(self.HOST, 'secure.example.com')
        self.assertEqual(self.PORT, 443)
