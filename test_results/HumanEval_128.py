def prod_signs(arr):
    if not arr:
        return None
    total_abs = 0
    sign_prod = 1
    for num in arr:
        total_abs += abs(num)
        if num > 0:
            sign_prod *= 1
        elif num < 0:
            sign_prod *= -1
        else:  # num == 0
            sign_prod *= 0
    return total_abs * sign_prod