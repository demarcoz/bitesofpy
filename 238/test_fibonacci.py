import pytest

from fibonacci import fib


# write one or more pytest functions below, they need to start with test_
@pytest.mark.parametrize("value, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
])
def test_get_fibonacci(value, expected):
    assert fib(value) == expected


def test_valueerror():
    with pytest.raises(ValueError):
        fib(-5)

def test_typeeror():
    with pytest.raises(TypeError):
        fib("test")
