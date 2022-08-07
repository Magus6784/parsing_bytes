from parsing_bytes import get_data_from_payload


if __name__ == "__main__":
    payload = "10FA0E00"

    try:
        parsed_data = get_data_from_payload(payload)
        print(parsed_data)
    except ValueError as v:
        print("You should check payload values.")
        raise v
    except TypeError as t:
        print("Something go really wrong. How can it possible?")
        raise t
    except Exception as e:
        print(f"Unexpected error: {type(e)}")
        raise e
