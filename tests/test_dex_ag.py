# TODO: Write the other method, and test by hand. Then commit. also add
# the other fixture.

import unittest

import responses

from defipulsedata import DexAg


class TestWrapper(unittest.TestCase):
    @responses.activate
    def test_get_markets(self):
        expected_url = (
            'https://data-api.defipulse.com/api/v1/dexag/markets?api-key=mock-key'
        )

        responses.add(responses.GET, expected_url, json='{}', status=200)
        DexAg(api_key='mock-key').get_markets()
        self.assertEqual(responses.calls[0].request.url, expected_url)

    @responses.activate
    def test_get_token_list_full(self):
        expected_url = 'https://data-api.defipulse.com/api/v1/dexag/token-list-full?api-key=mock-key'

        responses.add(responses.GET, expected_url, json='{}', status=200)
        DexAg(api_key='mock-key').get_token_list_full()
        self.assertEqual(responses.calls[0].request.url, expected_url)


class GetPriceTestWrapper(unittest.TestCase):
    @responses.activate
    def test_denomination_in_to_token(self):
        expected_url = 'https://data-api.defipulse.com/api/v1/dexag/price?toAmount=1&from=ETH&to=DAI&dex=all&api-key=mock-key'
        responses.add(responses.GET, expected_url, json='{}', status=200)
        DexAg(api_key='mock-key').get_price(
            fromToken='ETH', toToken='DAI', params={'toAmount': 1}
        )
        self.assertEqual(
            responses.calls[0].request.url,
            expected_url,
            'it serializes toAmount in the query params',
        )

    @responses.activate
    def test_denomination_in_from_token(self):
        expected_url = 'https://data-api.defipulse.com/api/v1/dexag/price?fromAmount=1&from=ETH&to=DAI&dex=all&api-key=mock-key'
        responses.add(responses.GET, expected_url, json='{}', status=200)
        DexAg(api_key='mock-key').get_price(
            fromToken='ETH', toToken='DAI', params={'fromAmount': 1}
        )
        self.assertEqual(
            responses.calls[0].request.url,
            expected_url,
            'it serializes fromAmount in the query params.',
        )

    @responses.activate
    def test_all_params(self):
        expected_url = 'https://data-api.defipulse.com/api/v1/dexag/price?discluded=uniswap%2Csushiswap&fromAmount=1&from=ETH&to=DAI&dex=all&api-key=mock-key'
        responses.add(responses.GET, expected_url, json='{}', status=200)
        params = {'discluded': 'uniswap,sushiswap', 'fromAmount': 1}
        DexAg(api_key='mock-key').get_price(
            fromToken='ETH', toToken='DAI', params=params
        )
        self.assertEqual(
            responses.calls[0].request.url,
            expected_url,
            'it includes the params keys and values in the URL',
        )

    @responses.activate
    def test_param_overrides(self):
        expected_url = 'https://data-api.defipulse.com/api/v1/dexag/price?fromAmount=1&dex=all&api-key=mock-key&discluded=override-discluded&from=ETH&to=DAI'
        responses.add(responses.GET, expected_url, json='{}', status=200)

        all_query_params = {
            'fromAmount': 1,
            'dex': 'override-dex',
            'api-key': 'override-key',
            'discluded': 'override-discluded',
        }
        DexAg(api_key='mock-key').get_price(
            fromToken='ETH',
            toToken='DAI',
            params={**all_query_params, 'from': 'from-override', 'to': 'to-override'},
        )
        self.assertEqual(
            responses.calls[0].request.url,
            expected_url,
            'specifying from and to in the params hash has no effect on the generated URL',
        )

    def test_invalid_param_combinations(self):
        client = DexAg(api_key='mock_key')
        args = {
            'fromToken': 'ETH',
            'toToken': 'DAI',
            'params': {
                'fromAmount': 100,
                'toAmount': 200,
            },
        }

        self.assertRaisesRegex(
            ValueError,
            "Only one of from_amount or to_amount may be specified.",
            client.get_price,
            **args,
        )

        self.assertRaisesRegex(
            ValueError,
            "Either from_amount or to_amount must be specified.",
            client.get_price,
            fromToken='ETH',
            toToken='DAI',
        )

        self.assertRaisesRegex(
            ValueError,
            "Received unexpected param: unknown-key",
            client.get_price,
            fromToken='ETH',
            toToken='DAI',
            params={'unknown-key': 'val', 'fromAmount': '1'},
        )
