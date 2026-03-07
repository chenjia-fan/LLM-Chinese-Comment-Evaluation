def simplify(x, n):
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    numerator = x_num * n_num
    denominator = x_den * n_den
    return numerator % denominator == 0