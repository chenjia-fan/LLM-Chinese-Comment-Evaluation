def digits(n):
    product = 1
    has_odd = False
    for digit in str(n):
        d = int(digit)
        if d % 2 == 1:
            has_odd = True
            product *= d
    if has_odd:
        return product
    else:
        return 0