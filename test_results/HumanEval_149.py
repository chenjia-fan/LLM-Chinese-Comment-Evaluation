def sorted_list_sum(lst):
    filtered = [s for s in lst if len(s) % 2 == 0]
    return sorted(filtered, key=lambda s: (len(s), s))