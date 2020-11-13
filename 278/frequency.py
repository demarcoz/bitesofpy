from collections import Counter


def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    count = sorted(Counter(numbers).items(), key=lambda x: x[1])
    minor, major = count[0][0], count[-1][0]
    return major, minor