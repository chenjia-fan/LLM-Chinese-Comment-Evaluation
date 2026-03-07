def largest_prime_factor(n):
    i = 2
    largest = 1
    while i * i <= n:
        while n % i == 0:
            largest = i
            n //= i
        i += 1
    if n > 1:
        largest = n
    return largest