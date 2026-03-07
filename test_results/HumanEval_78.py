def hex_key(num):
    primes = set('2357BD')
    count = 0
    for ch in num:
        if ch in primes:
            count += 1
    return count