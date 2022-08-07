from device_settings import device_settings, device_extended_fields


def get_data_from_payload(payload: str) -> dict:
    validate_payload(payload)
    binary_payload = convert_payload_to_binary(payload)
    parsed_data = parsing_data(binary_payload)
    return parsed_data


def parsing_data(binary_payload: str) -> dict:
    parsed_data = {}

    for i, set_setting in enumerate(device_settings):
        sett_byte = binary_payload[8 * i:8 + 8 * i][::-1]
        for start_bit, field_setting in set_setting.items():
            size, field_name = field_setting
            value = sett_byte[start_bit:start_bit + size]
            if field_name in device_extended_fields:
                value = device_extended_fields[field_name][str(int(value, 2))]
                parsed_data[field_name] = value
            else:
                parsed_data[field_name] = "0" + value
    return parsed_data


def convert_payload_to_binary(payload: str) -> str:
    try:
        return bin(int(payload, 16))[2:].zfill(32)
    except ValueError:
        raise ValueError("Payload must be hexadecimal.")


def validate_payload(payload: str) -> None:
    """Checking payload length, type and lack of + or -"""
    if type(payload) != str:
        raise TypeError(f"Payload must be string")
    if len(payload) != 8:
        raise ValueError(f"Payload length != 8.")
    if payload[0] in "+-":
        raise ValueError(f"Operator cant be used in payload.")
