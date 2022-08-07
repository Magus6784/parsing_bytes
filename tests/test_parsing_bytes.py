import pytest
from parsing_bytes import get_data_from_payload


@pytest.mark.parametrize(
    "payload,expected_error",
    [
        pytest.param("", ValueError,
                     id="Should return ValueError for empty payload"),
        pytest.param("FA", ValueError,
                     id="Should return ValueError for 1 set payload"),
        pytest.param("FA01", ValueError,
                     id="Should return ValueError for 2 set payload"),
        pytest.param("10FA0A", ValueError,
                     id="Should return ValueError for 3 set payload"),
        pytest.param("10FA0FA", ValueError,
                     id="Should return ValueError for 7 length payload"),
        pytest.param("10FA010FA0", ValueError,
                     id="Should return ValueError for big payload"),
    ]
)
def test_payload_length_must_be_8(
    payload,
    expected_error
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
            id="Should return correct data"),
    ]
)
def test_correct_parsing_payload(
    payload,
    parsed_data
):
    assert get_data_from_payload(payload) == parsed_data

# test_data = [
#     (
#         "10FA0E00",
#         {
#             "field1": "Low",
#             "field2": "00",
#             "field3": "01",
#             "field4": "00",
#             "field5": "00",
#             "field6": "01",
#             "field7": "00",
#             "field8": "Very High",
#             "field9": "00",
#             "field10": "00",
#         },
#     ),
# ]
