def even_odd_count(num):
    num_str = str(abs(num))
    even = sum(1 for d in num_str if int(d) % 2 == 0)
    odd = len(num_str) - even
    return (even, odd)