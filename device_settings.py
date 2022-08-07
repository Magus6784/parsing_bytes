# Format settings - array [sett_byte1 as dict {bit: [size, 'field_name']}, sett_byte2, sett_byte3, sett_byte4]
device_settings = [
    {0: [3, "field1"], 3: [1, "field2"], 4: [1, "field3"], 5: [3, "field4"]},
    {
        0: [1, "field5"],
        1: [1, "field6"],
        2: [1, "field7"],
        3: [3, "field8"],
    },
    {0: [1, "field9"], 5: [1, "field10"]},
    {},
]

field1 = {
    "0": "Low",
    "1": "reserved",
    "2": "reserved",
    "3": "reserved",
    "4": "Medium",
    "5": "reserved",
    "6": "reserved",
    "7": "High",
}
field4 = {
    "0": "00",
    "1": "10",
    "2": "20",
    "3": "30",
    "4": "40",
    "5": "50",
    "6": "60",
    "7": "70",
}
field8 = {
    "0": "Very Low",
    "1": "reserved",
    "2": "Low",
    "3": "reserved",
    "4": "Medium",
    "5": "High",
    "6": "reserved",
    "7": "Very High",
}

device_extended_fields = {
    "field1": field1,
    "field4": field4,
    "field8": field8,
}
