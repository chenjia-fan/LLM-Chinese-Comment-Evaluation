def count_nums(arr):
    def digit_sum(num):
        if num == 0:
            return 0
        # 获取数字的每一位（包括符号位）
        s = str(num)
        if s[0] == '-':
            # 负数：第一位带负号
            total = -int(s[1])  # 第一个数字带负号
            for ch in s[2:]:
                total += int(ch)
            return total
        else:
            # 正数
            total = 0
            for ch in s:
                total += int(ch)
            return total
    
    count = 0
    for num in arr:
        if digit_sum(num) > 0:
            count += 1
    return count