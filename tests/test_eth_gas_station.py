import json
import unittest

import responses

from defipulsedata import EthGasStation


class TestWrapper(unittest.TestCase):

    @responses.activate
    def test_get_gas_price(self):
        expected = json.dumps({})

        responses.add(
            responses.GET,
            'https://data-api.defipulse.com/api/v1/egs/api/ethgasAPI.json?api-key=mock-key',
            json=expected,
            status=200)

        response = EthGasStation(api_key='mock-key').get_gas_price()

        self.assertEqual(response, expected)

    @responses.activate
    def test_get_prediction_table(self):
        expected = json.dumps({})

        responses.add(
            responses.GET,
            'https://data-api.defipulse.com/api/v1/egs/api/predictTable.json?api-key=mock-key',
            json=expected,
            status=200)

        response = EthGasStation(api_key='mock-key').get_prediction_table()

        self.assertEqual(response, expected)
