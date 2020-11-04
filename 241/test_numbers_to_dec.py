import pytest

from numbers_to_dec import list_to_decimal


# write one or more pytest functions below, they need to start with test_
@pytest.mark.parametrize("value, expected", [
    ([0, 4, 2, 8], 428),
    ([1, 2], 12),
    ([3], 3),
    ([9, 5], 95),
    ([1], 1),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 123456789)
])
def test_list_to_decimal(value, expected):
    assert list_to_decimal(value) == expected


def test_integer():
    assert list_to_decimal([1]) == 1


def test_invalid_decimal_low():
    with pytest.raises(ValueError):
        list_to_decimal([-1])


def test_invalid_decimal_high():
    with pytest.raises(ValueError):
        list_to_decimal([10])


def test_empty_list():
    with pytest.raises(ValueError):
        list_to_decimal([])


def test_bool_typeerror():
    with pytest.raises(TypeError):
        list_to_decimal([True, False, [], "", {}, ()])


def test_missing_arguments():
    with pytest.raises(TypeError):
        list_to_decimal()
