import unittest

import responses

from defipulsedata import RekTo


EMPTY_DICT = {}


class TestWrapper(unittest.TestCase):
    @responses.activate
    def test_get_events(self):
        expected_url = (
            'https://data-api.defipulse.com/api/v1/rekto/api/events?api-key=mock-key'
        )
        client = RekTo(api_key='mock-key')
        responses.add(responses.GET, expected_url, json=EMPTY_DICT, status=200)

        client.get_events()
        self.assertEqual(responses.calls[0].request.url, expected_url)

    @responses.activate
    def test_get_top_10(self):
        expected_url = (
            'https://data-api.defipulse.com/api/v1/rekto/api/top10?api-key=mock-key'
        )
        client = RekTo(api_key='mock-key')
        responses.add(responses.GET, expected_url, json=EMPTY_DICT, status=200)

        client.get_top_10()
        self.assertEqual(responses.calls[0].request.url, expected_url)

    @responses.activate
    def test_get_total_damage(self):
        expected_url = 'https://data-api.defipulse.com/api/v1/rekto/api/total-damage?api-key=mock-key'
        client = RekTo(api_key='mock-key')
        responses.add(responses.GET, expected_url, json=EMPTY_DICT, status=200)

        client.get_total_damage()
        self.assertEqual(responses.calls[0].request.url, expected_url)
