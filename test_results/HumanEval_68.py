def pluck(arr):
    if not arr:
        return []
    min_even = None
    min_index = -1
    for i, val in enumerate(arr):
        if val % 2 == 0:
            if min_even is None or val < min_even or (val == min_even and i < min_index):
                min_even = val
                min_index = i
    if min_even is None:
        return []
    return [min_even, min_index]