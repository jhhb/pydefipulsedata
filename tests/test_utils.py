import unittest
import responses

from defipulsedata import utils


class TestWrapper(unittest.TestCase):

    @responses.activate
    def test_get_request(self):
        json = {}
        url = 'https://data-api.defipulse.com/api/v1/egs/api/ethgasAPI.json?api-key=mock-key'

        responses.add(responses.GET, url,
                      json=json, status=500)
        self.assertRaises(ValueError, utils.get_request, url)
        responses.reset()

        responses.add(responses.GET, url,
                      json=json, status=400)
        self.assertRaises(ValueError, utils.get_request, url)
        responses.reset()

        responses.add(responses.GET, url,
                      json=json, status=200)
        self.assertEqual(utils.get_request(url), json, 'it works!')

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
