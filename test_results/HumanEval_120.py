def maximum(arr, k):
    sorted_arr = sorted(arr)
    return sorted_arr[len(sorted_arr)-k:]