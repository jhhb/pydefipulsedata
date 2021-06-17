import warnings
from urllib import parse

from .utils import filter_null_keys, get_request, validate_allowed_params


class DefiPulse:
    __API_URL_BASE = 'https://data-api.defipulse.com/api/v1/defipulse/api'

    def __init__(self, *, api_key):
        self.api_base_url = self.__API_URL_BASE
        self.base_params = {'api-key': api_key}

    def get_market_data(self):
        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/MarketData?{1}'.format(self.api_base_url, encoded_params)
        return get_request(api_url)

    def get_history(self, *, params=None):
        allowed_params = {
            'project',
            'period',
            'length',
            'resolution',
            'category',
            'api-key',
        }
        function_params = params or {}

        if 'period' in function_params and 'length' in function_params:
            warnings.warn('API only supports "period" or "length" params exclusively.')

        default_params = {'project': 'all'}
        merged_params = {**default_params, **function_params, **self.base_params}
        validate_allowed_params(merged_params, allowed_params)

        encoded_params = parse.urlencode(merged_params)
        api_url = '{0}/GetHistory?{1}'.format(self.api_base_url, encoded_params)

        return get_request(api_url)

    def get_projects(self):
        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/GetProjects?{1}'.format(self.api_base_url, encoded_params)
        return get_request(api_url)

    def get_lending_tokens(self):
        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/GetLendingTokens?{1}'.format(self.api_base_url, encoded_params)
        return get_request(api_url)

    def get_lending_market_data(self):
        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/LendingMarketData?{1}'.format(self.api_base_url, encoded_params)
        return get_request(api_url)

    def get_lending_projects(self):
        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/GetLendingProjects?{1}'.format(self.api_base_url, encoded_params)

        return get_request(api_url)

    def get_lending_history(self, *, params=None):
        allowed_params = {
            'period',
            'length',
            'resolution',
            'format',
            'api-key',
        }
        function_params = params or {}
        if 'period' in function_params and 'length' in function_params:
            warnings.warn('API only supports "period" or "length" params exclusively.')

        merged_params = {**function_params, **self.base_params}
        validate_allowed_params(merged_params, allowed_params)

        encoded_params = parse.urlencode(merged_params)
        api_url = '{0}/getLendingHistory?{1}'.format(self.api_base_url, encoded_params)
        return get_request(api_url)

    def get_rates(self, *, token, amount=None):
        allowed_params = {'token', 'amount', 'api-key'}
        merged_params = {'token': token, 'amount': amount, **self.base_params}
        filtered_params = filter_null_keys(merged_params)
        validate_allowed_params(filtered_params, allowed_params)

        encoded_params = parse.urlencode(filtered_params)
        api_url = '{0}/GetRates?{1}'.format(self.api_base_url, encoded_params)
        return get_request(api_url)
