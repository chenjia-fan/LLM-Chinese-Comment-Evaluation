def is_sorted(lst):
    if not lst:
        return True
    seen = {}
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
        seen[lst[i-1]] = seen.get(lst[i-1], 0) + 1
        if seen[lst[i-1]] > 2:
            return False
    seen[lst[-1]] = seen.get(lst[-1], 0) + 1
    if seen[lst[-1]] > 2:
        return False
    return True