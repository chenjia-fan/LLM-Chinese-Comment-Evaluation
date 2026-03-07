from typing import List

def factorize(n: int) -> List[int]:
    result = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            result.append(divisor)
            n //= divisor
        divisor += 1
    return result