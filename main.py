from parsing_bytes import get_data_from_payload


if __name__ == "__main__":
    payload = "10FA0E00"

    try:
        parsed_data = get_data_from_payload(payload)
        print(parsed_data)
    except ValueError as v:
        print(f"You should check payload values. Payload: {payload}")
        raise v
    except TypeError as t:
        print("Something is going really wrong."
              f"Payload type: {type(payload)}. How is this possible?")
        raise t
    except Exception as e:
        print(f"Unexpected error: {type(e)}")
        raise e
