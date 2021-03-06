from enum import Enum
from itertools import zip_longest


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def is_equal(list1, list2):
    """Returns True if both lists are equal.
    """
    for a, b in zip_longest(list1, list2):
        if a != b:
            return False
    return True


def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match
    """
    if list1 is list2:
        return Equality(4)

    if is_equal(list1, list2):
        return Equality(3)

    sorted1 = sorted(list1)
    sorted2 = sorted(list2)
    if is_equal(sorted1, sorted2):
        return Equality(2)

    deduped1 = list(set(list1))
    deduped2 = list(set(list2))
    if is_equal(deduped1, deduped2):
        return Equality(1)

    return Equality(0)
