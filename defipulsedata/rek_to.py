from urllib import parse

from .utils import get_request


class RekTo:
    __API_URL_BASE = 'https://data-api.defipulse.com/api/v1/rekto/api'

    def __init__(self, *, api_key):
        self.api_base_url = self.__API_URL_BASE
        self.base_params = {'api-key': api_key}

    def get_events(self):
        # https://data-api.defipulse.com/api/v1/rekto/api/events
        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/events?{1}'.format(self.api_base_url, encoded_params)
        return get_request(api_url)

    def get_top_10(self):
        # https://data-api.defipulse.com/api/v1/rekto/api/top10
        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/top10?{1}'.format(self.api_base_url, encoded_params)
        return get_request(api_url)

    def get_total_damage(self):
        # https://data-api.defipulse.com/api/v1/rekto/api/total-damage
        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/total-damage?{1}'.format(self.api_base_url, encoded_params)
        return get_request(api_url)
