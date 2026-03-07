def unique_digits(x):
    def has_even_digit(n):
        while n > 0:
            if (n % 10) % 2 == 0:
                return True
            n //= 10
        return False

    result = [num for num in x if not has_even_digit(num)]
    result.sort()
    return result