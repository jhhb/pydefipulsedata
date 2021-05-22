from urllib import parse

from .utils import get_request


class EthGasStation:
    __API_URL_BASE = 'https://data-api.defipulse.com/api/v1/egs/api'

    def __init__(self, *, api_key):
        self.api_base_url = self.__API_URL_BASE
        self.base_params = {'api-key': api_key}

    def get_gas_price(self):
        "Returns the current recommended fast, standard and safe low gas prices on the Ethereum network, along with the current block and wait times for each 'speed'."

        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/ethgasAPI.json?{1}'.format(self.api_base_url, encoded_params)
        return get_request(api_url)

    def get_prediction_table(self):
        "Returns estimated confirmation times for a range of gas prices from the EGS Prediction Page."

        encoded_params = parse.urlencode(self.base_params)
        api_url = '{0}/predictTable.json?{1}'.format(self.api_base_url, encoded_params)
        return get_request(api_url)
