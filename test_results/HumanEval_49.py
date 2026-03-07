def modp(n, p):
    if p == 1:
        return 0
    res = 1
    base = 2 % p
    while n > 0:
        if n & 1:
            res = (res * base) % p
        base = (base * base) % p
        n >>= 1
    return res