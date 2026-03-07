def circular_shift(x, shift):
    s = str(x)
    n = len(s)
    if shift > n:
        return s[::-1]
    shift = shift % n
    if shift == 0:
        return s
    return s[-shift:] + s[:-shift]