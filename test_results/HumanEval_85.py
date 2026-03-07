def add(lst):
    total = 0
    for i, num in enumerate(lst):
        if i % 2 == 1 and num % 2 == 0:
            total += num
    return total