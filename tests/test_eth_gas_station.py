import unittest

import responses

from defipulsedata import EthGasStation


class TestWrapper(unittest.TestCase):
    @responses.activate
    def test_get_gas_price(self):
        expected_url = 'https://data-api.defipulse.com/api/v1/egs/api/ethgasAPI.json?api-key=mock-key'

        responses.add(responses.GET, expected_url, json='{}', status=200)
        EthGasStation(api_key='mock-key').get_gas_price()
        self.assertEqual(responses.calls[0].request.url, expected_url)

    @responses.activate
    def test_get_prediction_table(self):
        expected_url = 'https://data-api.defipulse.com/api/v1/egs/api/predictTable.json?api-key=mock-key'

        responses.add(responses.GET, expected_url, json='{}', status=200)
        EthGasStation(api_key='mock-key').get_prediction_table()
        self.assertEqual(responses.calls[0].request.url, expected_url)
