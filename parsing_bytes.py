from device_settings import device_settings, device_extended_fields


def get_data_from_payload(payload):
    validate_payload(payload)
    parsed_data = {}
    binary_payload = bin(int(payload, 16))[2:].zfill(32)

    for i, set_setting in enumerate(device_settings):
        sett_byte = binary_payload[8 * i: 8 + 8 * i][::-1]
        for bit, field_setting in set_setting.items():
            size, field_name = field_setting
            value = sett_byte[bit:bit + size]
            if field_name in device_extended_fields:
                value = device_extended_fields[field_name][str(int(value, 2))]
                parsed_data[field_name] = value
            else:
                parsed_data[field_name] = "0" + value

    return parsed_data


def validate_payload(payload):
    if len(payload) < 8 or len(payload) > 8:
        raise ValueError(f"payload length != 8. payload: {payload}")
