import unittest
import responses

from defipulsedata import utils

global EMPTY_BLOB
# TODO: JB - Check on the actual return type.
EMPTY_BLOB = '{}'


class TestWrapper(unittest.TestCase):

    @responses.activate
    def test_get_request(self):
        expected_url = 'https://data-api.defipulse.com/api/v1/egs/api/ethgasAPI.json?api-key=mock-key'

        responses.add(responses.GET, expected_url,
                      json=EMPTY_BLOB, status=500)
        self.assertRaises(ValueError, utils.get_request, expected_url)

        responses.reset()
        responses.add(responses.GET, expected_url,
                      json=EMPTY_BLOB, status=400)
        self.assertRaises(ValueError, utils.get_request, expected_url)

        responses.reset()
        responses.add(responses.GET, expected_url,
                      EMPTY_BLOB, status=200)
        utils.get_request(expected_url)
        self.assertEqual(responses.calls[0].request.url, expected_url)

    @responses.activate
    def test_validate_allowed_params(self):
        empty_params = {}
        params = {'foo': 'bar'}

        self.assertRaises(
            ValueError,
            utils.validate_allowed_params,
            params,
            empty_params)

        self.assertEqual(
            utils.validate_allowed_params(
                empty_params,
                params),
            None,
            'it handles empty hash input')

        self.assertEqual(
            utils.validate_allowed_params(
                empty_params,
                None),
            None,
            'it handles None input')
