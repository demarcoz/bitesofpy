VOWELS = "aeiou"
PYTHON = "python"


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return all([_.lower() in VOWELS for _ in input_str])


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return any([_.lower() in PYTHON for _ in input_str])


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return any([_.isdigit() for _ in input_str])
