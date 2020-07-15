def raise_exception_if_not_ok(response):
    if response.ok:
        return

    raise Exception(get_response_error_message(response))


def get_response_error_message(response):
    error_msg = f'received {response.status_code}'
    resp_json = response.json()
    err_type = resp_json.get('type', '')
    message = resp_json.get('message', '')
    if err_type:
        error_msg += f" : {err_type}"

    if message:
        error_msg += f" : {message}"

    return error_msg
