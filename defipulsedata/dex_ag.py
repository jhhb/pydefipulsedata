from urllib import parse

from .utils import get_request, validate_allowed_params


class DexAg:
    __API_URL_BASE = 'https://data-api.defipulse.com/api/v1/dexag'

    def __init__(self, *, api_key):
        self.base_params = {'api-key': api_key}
        self.api_base_url = self.__API_URL_BASE

    def get_markets(self):
        # https://data-api.defipulse.com/api/v1/dexag/markets
        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/markets?{1}'.format(
            self.api_base_url, encoded_params
        )
        return get_request(api_url)

    def get_token_list_full(self):
        # https://data-api.defipulse.com/api/v1/dexag/token-list-full
        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/token-list-full?{1}'.format(
            self.api_base_url, encoded_params
        )
        return get_request(api_url)

    def get_price(
            self,
            *,
            fromToken,
            toToken,
            dex='all',
            params={}):
        # https://data-api.defipulse.com/api/v1/dexag/price?from=ETH&to=DAI&fromAmount=1&dex=ag

        required_params = {
            'from': fromToken,
            'to': toToken,
            'dex': dex,
        }

        merged_params = {
            **params,
            **required_params,
            **self.base_params}

        allowed_params = {
            'from',
            'to',
            'fromAmount',
            'toAmount',
            'dex',
            'discluded',
            'api-key'
        }

        from_amount, to_amount = params.get(
            'fromAmount'), params.get('toAmount')
        if not (from_amount or to_amount):
            raise ValueError(
                "Either from_amount or to_amount must be specified.")
        if from_amount and to_amount:
            raise ValueError(
                "Only one of from_amount or to_amount may be specified.")

        validate_allowed_params(merged_params, allowed_params)

        encoded_params = parse.urlencode(merged_params)
        api_url = '{0}/price?{1}'.format(
            self.api_base_url, encoded_params)
        return get_request(api_url)
