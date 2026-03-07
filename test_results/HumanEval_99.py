def closest_integer(value):
    n = float(value)
    if n >= 0:
        return int(n + 0.5) if n % 1 != 0.5 else int(n + 1)
    else:
        return int(n - 0.5) if n % 1 != -0.5 else int(n - 1)