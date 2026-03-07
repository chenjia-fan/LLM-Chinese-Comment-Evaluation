def sort_array(array):
    if not array:
        return []
    if len(array) == 1:
        return array[:]
    first_last_sum = array[0] + array[-1]
    if first_last_sum % 2 == 1:
        return sorted(array)
    else:
        return sorted(array, reverse=True)