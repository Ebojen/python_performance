from control_flatten import control_flatten
from dry_flatten import dry_flatten
from one_thing_flatten import one_thing_flatten


FUNCS = [control_flatten, dry_flatten, one_thing_flatten]

def test_should_properly_flatten_string_data():
    data = "a"
    expected = [{"root": "a"}]

    for func in FUNCS:
        result = func(data)

        assert expected == result


def test_should_properly_flatten_number_data():
    data = 4
    expected = [{"root": 4}]

    for func in FUNCS:
        result = func(data)

        assert expected == result


def test_should_properly_flatten_bool_data():
    data = False
    expected = [{"root": False}]

    for func in FUNCS:
        result = func(data)

        assert expected == result


def test_should_properly_flatten_a_flat_dict():
    data = {"key1": "string_value", "key2": 3.1415, "key3": True}
    expected = [{"root_key1": "string_value", "root_key2": 3.1415, "root_key3": True}]

    result = control_flatten(data)

    assert expected == result


def test_should_properly_flatten_nested_dict():
    data = {
        "key1": "root_value",
        "key2": {
            "key3": "one_layer_deep",
            "key4": {"key5": "two_layers_deep", "key6": {"key7": "three_layers_deep"}},
        },
    }
    expected = [
        {
            "root_key1": "root_value",
            "root_key2_key3": "one_layer_deep",
            "root_key2_key4_key5": "two_layers_deep",
            "root_key2_key4_key6_key7": "three_layers_deep",
        }
    ]

    for func in FUNCS:
        result = func(data)

        assert expected == result


def test_should_properly_flatten_a_list_of_primitives():
    data = ["string", 2.71828, False, None]
    expected = [
        {"root_0": "string"},
        {"root_1": 2.71828},
        {"root_2": False},
        {"root_3": None},
    ]

    for func in FUNCS:
        result = func(data)

        assert expected == result


def test_should_properly_flatten_a_list_of_flat_dicts():
    data = [
        {"key1": 0.0, "key2": 1.0},
        {"key1": 0.1, "key2": 1.1},
        {"key1": 0.2, "key2": 1.2},
        {"key1": 0.3, "key2": 1.3},
    ]
    expected = [
        {"root_0_key1": 0.0, "root_0_key2": 1.0},
        {"root_1_key1": 0.1, "root_1_key2": 1.1},
        {"root_2_key1": 0.2, "root_2_key2": 1.2},
        {"root_3_key1": 0.3, "root_3_key2": 1.3},
    ]

    for func in FUNCS:
        result = func(data)

        assert expected == result


def test_should_properly_flatten_a_dict_with_a_list_value():
    data = {
        "key1": "root_value",
        "key2": [{"key2.1": 0}, {"key2.1": 1}],
    }
    expected = [
        {"root_key1": "root_value", "root_key2_0_key2.1": 0},
        {"root_key1": "root_value", "root_key2_1_key2.1": 1},
    ]

    for func in FUNCS:
        result = func(data)

        assert expected == result


def test_should_properly_flatten_a_dict_with_multiple_list_values():
    data = {
        "key1": "root_value",
        "key2": [{"key2.1": 0}, {"key2.1": 1}],
        "key3": [
            {"key3.1": "a", "key3.2": "b"},
            {"key3.1": "c", "key3.2": "d"},
            {"key3.1": "e", "key3.2": "f"},
        ],
    }
    expected = [
        {
            "root_key1": "root_value",
            "root_key2_0_key2.1": 0,
            "root_key3_0_key3.1": "a",
            "root_key3_0_key3.2": "b",
        },
        {
            "root_key1": "root_value",
            "root_key2_0_key2.1": 0,
            "root_key3_1_key3.1": "c",
            "root_key3_1_key3.2": "d",
        },
        {
            "root_key1": "root_value",
            "root_key2_0_key2.1": 0,
            "root_key3_2_key3.1": "e",
            "root_key3_2_key3.2": "f",
        },
        {
            "root_key1": "root_value",
            "root_key2_1_key2.1": 1,
            "root_key3_0_key3.1": "a",
            "root_key3_0_key3.2": "b",
        },
        {
            "root_key1": "root_value",
            "root_key2_1_key2.1": 1,
            "root_key3_1_key3.1": "c",
            "root_key3_1_key3.2": "d",
        },
        {
            "root_key1": "root_value",
            "root_key2_1_key2.1": 1,
            "root_key3_2_key3.1": "e",
            "root_key3_2_key3.2": "f",
        },
    ]

    for func in FUNCS:
        result = func(data)

        assert expected == result
