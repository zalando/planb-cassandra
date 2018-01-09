import pytest

from planb.common import environment_as_dict, decode_user_data


def test_environment_as_dict():
    raw_list = ["key=value", "base64=dGVzdA=="]
    expected = {'key': 'value', 'base64': 'dGVzdA=='}
    assert environment_as_dict(raw_list) == expected


def test_decode_user_data():
    expected = {'test': 'Hello!'}
    assert decode_user_data("dGVzdDogSGVsbG8hCg==") == expected