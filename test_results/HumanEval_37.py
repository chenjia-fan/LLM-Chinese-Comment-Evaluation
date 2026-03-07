def sort_even(l):
    even_vals = sorted(l[i] for i in range(0, len(l), 2))
    result = []
    even_index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_vals[even_index])
            even_index += 1
        else:
            result.append(l[i])
    return result