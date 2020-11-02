import pytest

from numbers_to_dec import list_to_decimal


# write one or more pytest functions below, they need to start with test_
@pytest.mark.parametrize("value, expected", [
    ([0, 4, 2, 8], 428),
    ([1, 2], 12),
    ([3], 3),
])
def test_list_to_decimal(value, expected):
    assert list_to_decimal(value) == expected


def test_list_to_decimal_valueerror():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 12])


def test_list_to_decimal_typeeror():
    with pytest.raises(TypeError):
        list_to_decimal([True, 6])