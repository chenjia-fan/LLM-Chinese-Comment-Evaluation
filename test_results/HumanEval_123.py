def get_odd_collatz(n):
    odd_numbers = set()
    current = n
    while True:
        if current % 2 == 1:
            odd_numbers.add(current)
        if current == 1:
            break
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
    return sorted(list(odd_numbers))