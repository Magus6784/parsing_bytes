from device_settings import device_settings, device_special_fields


def get_data_from_payload(payload):
    try:
        if len(payload) < 8 or len(payload) > 8:
            raise ValueError
    except ValueError as v:
        v.args = ""
        return ValueError()
    # return parsed_data
