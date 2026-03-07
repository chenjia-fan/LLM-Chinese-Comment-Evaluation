def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    
    max_prime = None
    for num in lst:
        if is_prime(num):
            if max_prime is None or num > max_prime:
                max_prime = num
    
    if max_prime is None:
        return 0
    
    digit_sum = 0
    while max_prime > 0:
        digit_sum += max_prime % 10
        max_prime //= 10
    return digit_sum