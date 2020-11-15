from typing import List


def minimum_number(digits: List[int]) -> int:
    if len(digits) == 0:
        return 0
    return int("".join(sorted([str(_) for _ in set(digits)])))
