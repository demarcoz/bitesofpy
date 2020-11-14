def is_armstrong(n: int) -> bool:
    if n in range(1,10):
        return True
    power = len(str(n))
    result = sum([int(_) ** power for _ in str(n)])
    return result == n
