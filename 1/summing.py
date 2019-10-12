from typing import List

def sum_numbers(numbers:List=None) -> int:
    if numbers == None:
        return sum(range(1, 101))
    elif len(numbers):
        return sum(numbers)
    else:
        return 0
