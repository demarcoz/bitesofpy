def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if isinstance(value, int) or isinstance(value, float):
        if fmt.lower() == "cm":
            ret = value * 2.54
        elif fmt.lower() == "in":
            ret = value * 0.393700787
        else:
            raise ValueError
        return round(ret, 4)
    else:
        raise TypeError