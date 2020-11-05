import pytest

from workouts import print_workout_days


@pytest.mark.parametrize("value, expected", [
    ("body", "Mon, Tue, Thu, Fri\n"),
    ("lower", "Tue, Fri\n"),
    ("upper", "Mon, Tue\n"),
    ("cardio", "Wed\n"),
    ("", "Mon, Tue, Wed, Thu, Fri\n"),
    ("none", "No matching workout\n"),
])
def test_print_workout_days(capsys, input, output):
    print_workout_days(input)
    capture = capsys.readouterr()
    assert capture.out == output


def test_typeerror():
    with pytest.raises(TypeError):
        print_workout_days()


def test_attributeerror():
    with pytest.raises(AttributeError):
        print_workout_days(1)
