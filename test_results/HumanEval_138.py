def is_equal_to_sum_even(n):
    # 四个正偶数之和至少是 2+2+2+2 = 8，并且必须是偶数
    return n >= 8 and n % 2 == 0