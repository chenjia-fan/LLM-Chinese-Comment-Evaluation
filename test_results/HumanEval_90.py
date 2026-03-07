def next_smallest(lst):
    if len(lst) < 2:
        return None
    
    # 找到最小元素
    min_val = min(lst)
    
    # 找到比最小元素大的所有元素中的最小值
    second_min = None
    for num in lst:
        if num > min_val:
            if second_min is None or num < second_min:
                second_min = num
    
    return second_min