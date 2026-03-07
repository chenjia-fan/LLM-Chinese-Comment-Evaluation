def is_multiply_prime(a):
    if a < 2:
        return False
    
    count = 0
    i = 2
    temp = a
    while i * i <= temp:
        while temp % i == 0:
            temp //= i
            count += 1
        i += 1
    
    if temp > 1:
        count += 1
    
    return count == 3