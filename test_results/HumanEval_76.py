def is_simple_power(x, n):
    if x == 1:
        return True
    if n == 1:
        return False
    if n == 0:
        return x == 0
    power = 1
    while power < x:
        power *= n
        if power == x:
            return True
    return False