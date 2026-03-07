def sort_third(l):
    indices = [i for i in range(len(l)) if i % 3 == 0]
    values = [l[i] for i in indices]
    values.sort()
    result = l[:]
    for idx, val in zip(indices, values):
        result[idx] = val
    return result