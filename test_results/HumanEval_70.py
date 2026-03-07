def strange_sort_list(lst):
    sorted_lst = sorted(lst)
    result = []
    left, right = 0, len(sorted_lst) - 1
    while left <= right:
        result.append(sorted_lst[left])
        left += 1
        if left <= right:
            result.append(sorted_lst[right])
            right -= 1
    return result