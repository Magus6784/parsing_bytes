import pytest
from parsing_bytes import get_data_from_payload


@pytest.mark.parametrize(
    "payload,expected_error",
    [
        pytest.param(
            "", ValueError,
            id="Should raise ValueError for empty payload"),
        pytest.param(
            "10FA010FA0", ValueError,
            id="Should raise ValueError for big payload"
        ),
        pytest.param(
            "10FA0A",
            ValueError,
            id="Should raise ValueError for length payload less than 8",
        ),
        pytest.param(
            "G2FA0FA3",
            ValueError,
            id="Should raise ValueError for not hexadecimal data",
        ),
        pytest.param(
            ["10FA0E00"], TypeError,
            id="Should raise TypeError for not string"
        ),
        pytest.param(
            "-0FA0E00",
            ValueError,
            id="Should raise ValueError for not expected symbols",
        ),
    ],
)
def test_should_raise_error_when_payload_incorrect(
    payload: str,
    expected_error,
):
    with pytest.raises(expected_error):
        get_data_from_payload(payload)


@pytest.mark.parametrize(
    "payload,parsed_data",
    [
        pytest.param(
            "10FA0E00",
            {
                "field1": "Low",
                "field2": "00",
                "field3": "01",
                "field4": "00",
                "field5": "00",
                "field6": "01",
                "field7": "00",
                "field8": "Very High",
                "field9": "00",
                "field10": "00",
            },
            id="Should return correct data for correct payload",
        ),
        pytest.param(
            "C90D2100",
            {
                "field1": "Medium",
                "field2": "01",
                "field3": "00",
                "field4": "30",
                "field5": "01",
                "field6": "00",
                "field7": "01",
                "field8": "Medium",
                "field9": "01",
                "field10": "01",
            },
            id="Should return correct data for non zero extended fields",
        ),
        pytest.param(
            "00000000",
            {
                "field1": "Low",
                "field2": "00",
                "field3": "00",
                "field4": "00",
                "field5": "00",
                "field6": "00",
                "field7": "00",
                "field8": "Very Low",
                "field9": "00",
                "field10": "00",
            },
            id="Should return correct data for minimum payload",
        ),
        pytest.param(
            "FFFFFFFF",
            {
                "field1": "High",
                "field2": "01",
                "field3": "01",
                "field4": "70",
                "field5": "01",
                "field6": "01",
                "field7": "01",
                "field8": "Very High",
                "field9": "01",
                "field10": "01",
            },
            id="Should return correct data for maximum payload",
        ),
    ],
)
def test_correct_parsing_payload(
    payload: str,
    parsed_data: dict,
):
    assert get_data_from_payload(payload) == parsed_data
