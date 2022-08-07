from device_settings import device_settings, device_special_fields


def get_data_from_payload(payload):
    validate_payload(payload)
    # return parsed_data


def validate_payload(payload):
    if len(payload) < 8 or len(payload) > 8:
        raise ValueError(f"payload length != 8. payload: {payload}")
