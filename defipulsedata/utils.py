import json

import requests


def get_request(url, **kwargs):
    response, exception = None, None
    timeout = kwargs.get('timeout', 30)

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        content = json.loads(response.content.decode('utf-8'))
        return content
    except Exception as e:
        # TODO: Revisit this as we learn more about error handling.
        try:
            content = json.loads(response.content.decode('utf-8'))
            raise ValueError(content)
        except json.decoder.JSONDecodeError:
            pass
        raise e


def validate_allowed_params(actual_params, allowed_params):
    for k in actual_params:
        if k not in allowed_params:
            message = "Received unexpected param: {0}".format(k)
            raise ValueError(message)
