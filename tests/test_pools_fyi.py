import unittest

import responses

from defipulsedata import PoolsFyi


class TestWrapper(unittest.TestCase):
    @responses.activate
    def test_get_exchanges(self):
        url_without_params = 'https://data-api.defipulse.com/api/v1/blocklytics/pools/v1/exchanges?api-key=mock-key'
        responses.add(responses.GET, url_without_params, json='{}', status=200)
        PoolsFyi(api_key='mock-key').get_exchanges()
        self.assertEqual(responses.calls[0].request.url, url_without_params)

        responses.reset()
        url_with_params = 'https://data-api.defipulse.com/api/v1/blocklytics/pools/v1/exchanges?tags=stable&platform=bancor&direction=asc&orderBy=platform&offset=1&limit=200&api-key=mock-key'
        all_params = {
            'tags': 'stable',
            'platform': 'bancor',
            'direction': 'asc',
            'orderBy': 'platform',
            'offset': 1,
            'limit': 200,
        }
        responses.add(responses.GET, url_with_params, json='{}', status=200)
        PoolsFyi(api_key='mock-key').get_exchanges(params=all_params)
        self.assertEqual(
            responses.calls[0].request.url,
            url_with_params,
            'it correctly serializes the query params',
        )

    @responses.activate
    def test_get_returns(self):
        address = '0x0000000000000000000000000000000000000000'
        expected_url = 'https://data-api.defipulse.com/api/v1/blocklytics/pools/v1/returns/0x0000000000000000000000000000000000000000?api-key=mock-key'

        responses.add(responses.GET, expected_url, json='{}', status=200)
        PoolsFyi(api_key='mock-key').get_returns(address=address)
        self.assertEqual(responses.calls[0].request.url, expected_url)

    @responses.activate
    def test_get_liquidity(self):
        address = '0x0000000000000000000000000000000000000000'
        expected_url = 'https://data-api.defipulse.com/api/v1/blocklytics/pools/v0/liquidity/0x0000000000000000000000000000000000000000?api-key=mock-key'

        responses.add(responses.GET, expected_url, json='{}', status=200)
        PoolsFyi(api_key='mock-key').get_liquidity(address=address)
        self.assertEqual(responses.calls[0].request.url, expected_url)

    @responses.activate
    def test_get_exchange(self):
        address = '0x0000000000000000000000000000000000000000'
        expected_url = 'https://data-api.defipulse.com/api/v1/blocklytics/pools/v1/exchange/0x0000000000000000000000000000000000000000?api-key=mock-key'

        responses.add(responses.GET, expected_url, json='{}', status=200)
        PoolsFyi(api_key='mock-key').get_exchange(address=address)
        self.assertEqual(responses.calls[0].request.url, expected_url)

    @responses.activate
    def test_get_trades(self):
        address = '0x0000000000000000000000000000000000000000'
        url_without_params = 'https://data-api.defipulse.com/api/v1/blocklytics/pools/v1/trades/0x0000000000000000000000000000000000000000?api-key=mock-key'

        responses.add(responses.GET, url_without_params, json='{}', status=200)
        PoolsFyi(api_key='mock-key').get_trades(address=address)
        self.assertEqual(responses.calls[0].request.url, url_without_params)

        responses.reset()
        url_with_all_params = 'https://data-api.defipulse.com/api/v1/blocklytics/pools/v1/trades/0x0000000000000000000000000000000000000000?from=2020-10-21&to=2020-10-31&platform=bancor&direction=asc&orderBy=platform&offset=1&limit=200&api-key=mock-key'
        responses.add(responses.GET, url_with_all_params, json='{}', status=200)

        all_params = {
            'from': '2020-10-21',
            'to': '2020-10-31',
            'platform': 'bancor',
            'direction': 'asc',
            'orderBy': 'platform',
            'offset': 1,
            'limit': 200,
        }
        PoolsFyi(api_key='mock-key').get_trades(address=address, params=all_params)
        self.assertEqual(responses.calls[0].request.url, url_with_all_params)
