import unittest

import responses

from defipulsedata import DefiPulse


EMPTY_BLOB = {}


class TestWrapper(unittest.TestCase):
    @responses.activate
    def test_simple_endpoints(self):
        client = DefiPulse(api_key='mock-key')

        simple_endpoint_urls = [
            (
                client.get_market_data,
                'https://data-api.defipulse.com/api/v1/defipulse/api/MarketData?api-key=mock-key',
            ),
            (
                client.get_projects,
                'https://data-api.defipulse.com/api/v1/defipulse/api/GetProjects?api-key=mock-key',
            ),
            (
                client.get_lending_tokens,
                'https://data-api.defipulse.com/api/v1/defipulse/api/GetLendingTokens?api-key=mock-key',
            ),
            (
                client.get_lending_market_data,
                'https://data-api.defipulse.com/api/v1/defipulse/api/LendingMarketData?api-key=mock-key',
            ),
            (
                client.get_lending_projects,
                'https://data-api.defipulse.com/api/v1/defipulse/api/GetLendingProjects?api-key=mock-key',
            ),
        ]

        for fn, url in simple_endpoint_urls:
            responses.reset()
            responses.add(responses.GET, url, json=EMPTY_BLOB, status=200)
            fn()
            self.assertEqual(responses.calls[0].request.url, url)

    @responses.activate
    def test_get_history(self):
        # TODO: JB - This should also test and implement usage of exclusive params
        client = DefiPulse(api_key='mock-key')

        url = 'https://data-api.defipulse.com/api/v1/defipulse/api/GetHistory?api-key=mock-key'
        responses.add(responses.GET, url, json=EMPTY_BLOB, status=200)
        client.get_history()
        self.assertEqual(responses.calls[0].request.url, url)

    @responses.activate
    def test_get_lending_history(self):
        # TODO: JB - This should also test and implement usage of exclusive params
        client = DefiPulse(api_key='mock-key')

        url = 'https://data-api.defipulse.com/api/v1/defipulse/api/getLendingHistory?api-key=mock-key'
        responses.add(responses.GET, url, json=EMPTY_BLOB, status=200)
        client.get_lending_history()
        self.assertEqual(
            responses.calls[0].request.url,
            url,
        )

    @responses.activate
    def test_get_rates(self):
        client = DefiPulse(api_key='mock-key')

        url_without_amount = 'https://data-api.defipulse.com/api/v1/defipulse/api/GetRates?token=DAI&api-key=mock-key'
        responses.add(responses.GET, url_without_amount, json=EMPTY_BLOB, status=200)
        client.get_rates(token='DAI')
        self.assertEqual(
            responses.calls[0].request.url,
            url_without_amount,
            'it does not include amount as a query param',
        )

        responses.reset()
        url_with_amount = 'https://data-api.defipulse.com/api/v1/defipulse/api/GetRates?token=DAI&amount=100&api-key=mock-key'
        responses.add(responses.GET, url_with_amount, json=EMPTY_BLOB, status=200)
        client.get_rates(token='DAI', amount=100)
        self.assertEqual(
            responses.calls[0].request.url,
            url_with_amount,
            'it includes the amount as a query param',
        )
