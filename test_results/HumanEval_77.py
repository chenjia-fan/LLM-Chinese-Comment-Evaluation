def iscube(a):
    # 处理0的情况
    if a == 0:
        return True
    
    # 计算立方根并四舍五入到最近的整数
    root = round(abs(a) ** (1/3))
    
    # 检查原数和负数的立方
    if root ** 3 == abs(a):
        # 根据a的符号检查对应的立方
        if a > 0:
            return True
        else:
            # 对于负数，检查负的立方根
            return (-root) ** 3 == a
    return False