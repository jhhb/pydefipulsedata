from urllib import parse

from .utils import get_request, validate_allowed_params


class PoolsFyi:
    __API_URL_BASE = 'https://data-api.defipulse.com/api/v1/blocklytics/pools'

    def __init__(self, *, api_key):
        self.api_base_url = self.__API_URL_BASE
        self.base_params = {'api-key': api_key}

    def get_exchanges(self, *, params=None):
        # Example URL:
        # https://data-api.defipulse.com/api/v1/blocklytics/pools/v1/exchanges
        allowed_params = {
            'tags',
            'platform',
            'direction',
            'orderBy',
            'offset',
            'limit',
            'api-key',
        }
        function_params = params or {}
        merged_params = {**function_params, **self.base_params}

        validate_allowed_params(merged_params, allowed_params)

        encoded_params = parse.urlencode(merged_params)
        api_url = '{0}/v1/exchanges?{1}'.format(self.api_base_url, encoded_params)
        return get_request(api_url)

    def get_returns(self, *, address):
        # Example URL for UNI-V2 ETH/GRT:
        # https://data-api.defipulse.com/api/v1/blocklytics/pools/v1/returns/0x2e81ec0b8b4022fac83a21b2f2b4b8f5ed744d70

        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/v1/returns/{1}?{2}'.format(
            self.api_base_url, address, encoded_params
        )
        return get_request(api_url)

    def get_liquidity(self, *, address):
        # Returns the owners of liquidity on the AMM
        # Example URL: https://data-api.defipulse.com/api/v1/blocklytics/pools/v0/liquidity/0x2e81ec0b8b4022fac83a21b2f2b4b8f5ed744d70/owners

        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/v0/liquidity/{1}?{2}'.format(
            self.api_base_url, address, encoded_params
        )
        return get_request(api_url)

    def get_exchange(self, *, address):
        # Example URL:
        # https://data-api.defipulse.com/api/v1/blocklytics/pools/v1/exchange/0x2e81ec0b8b4022fac83a21b2f2b4b8f5ed744d70

        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/v1/exchange/{1}?{2}'.format(
            self.api_base_url, address, encoded_params
        )
        return get_request(api_url)

    def get_trades(self, *, address, params=None):
        allowed_params = {
            'platform',
            'direction',
            'orderBy',
            'offset',
            'limit',
            'to',
            'from',
            'api-key',
        }
        function_params = params or {}
        merged_params = {**function_params, **self.base_params}

        validate_allowed_params(merged_params, allowed_params)

        encoded_params = parse.urlencode(merged_params)
        api_url = '{0}/v1/trades/{1}?{2}'.format(
            self.api_base_url, address, encoded_params
        )
        return get_request(api_url)
