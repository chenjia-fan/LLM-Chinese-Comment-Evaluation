def cycpattern_check(a, b):
    n = len(b)
    for i in range(n):
        rotated = b[i:] + b[:i]
        if rotated in a:
            return True
    return False