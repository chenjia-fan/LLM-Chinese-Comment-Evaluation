def largest_divisor(n: int) -> int:
    if n <= 1:
        return 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            return n // i
        i += 1
    return 1