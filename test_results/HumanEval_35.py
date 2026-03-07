def max_element(l: list):
    if not l:
        return None
    max_val = l[0]
    for item in l[1:]:
        if item > max_val:
            max_val = item
    return max_val