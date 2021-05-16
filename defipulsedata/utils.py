import json

import requests


# TODO: JB - Revisit this as we learn more about error handling.
def get_request(url, **kwargs):
    timeout = kwargs.get('timeout', 30)

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        content = json.loads(response.content.decode('utf-8'))
        return content
    except (json.decoder.JSONDecodeError, requests.HTTPError) as e:
        raise e
    except Exception as e:
        message = "Unexpected exception type: {type}".format(type=e.__class__.__name__)
        raise Exception(message) from e


def validate_allowed_params(actual_params, allowed_params):
    for k in actual_params:
        if k not in allowed_params:
            message = "Received unexpected param: {0}".format(k)
            raise ValueError(message)


def filter_null_keys(_dict):
    return {k: v for k, v in _dict.items() if v is not None}
