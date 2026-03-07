def choose_num(x, y):
    if x > y:
        return -1
    # 确保从较大数开始向下寻找偶数
    start = max(x, y)
    end = min(x, y)
    # 如果start是奇数，减1变成偶数（但必须>=end）
    if start % 2 == 1:
        start -= 1
    # 检查是否在范围内
    if start >= end:
        return start
    else:
        return -1