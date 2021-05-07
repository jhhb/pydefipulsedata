from .utils import get_request


class EthGasStation:
    __API_URL_BASE = 'https://data-api.defipulse.com/api/v1/egs/api'

    def __init__(self, *, api_key):
        self.api_key = api_key
        self.api_base_url = self.__API_URL_BASE

    def get_gas_price(self):
        "Returns the current recommended fast, standard and safe low gas prices on the Ethereum network, along with the current block and wait times for each 'speed'."

        api_url = '{0}/ethgasAPI.json?api-key={1}'.format(
            self.api_base_url, self.api_key
        )
        return get_request(api_url)

    def get_prediction_table(self):
        "Returns estimated confirmation times for a range of gas prices from the EGS Prediction Page."

        api_url = '{0}/predictTable.json?api-key={1}'.format(
            self.api_base_url, self.api_key
        )
        return get_request(api_url)
