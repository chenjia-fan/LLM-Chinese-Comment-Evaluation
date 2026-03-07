def prime_fib(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    prime_fibs = []
    a, b = 0, 1
    while len(prime_fibs) < n:
        a, b = b, a + b
        if a > 1 and is_prime(a):
            prime_fibs.append(a)
    return prime_fibs[-1]