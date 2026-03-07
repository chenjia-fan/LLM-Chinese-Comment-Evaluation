import math

def poly(xs: list, x: float):
    """
    求解点x处系数为xs的多项式。
    返回xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n。
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs是多项式的系数。find_zero返回poly(x)= 0时的解。函数find_zero只返回一个零点，即使有多个零点。此外，函数find_zero只接受具有偶数个系数和最大非零系数的列表xs，因为这样可以保证有一个解。
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # 使用二分法寻找零点
    # 初始搜索区间设为[-100, 100]，因为系数通常不会导致根过大
    left, right = -100.0, 100.0
    epsilon = 1e-10  # 精度要求
    max_iterations = 1000  # 最大迭代次数，防止无限循环
    
    # 计算区间端点的函数值
    f_left = poly(xs, left)
    f_right = poly(xs, right)
    
    # 如果左端点是零点，直接返回
    if abs(f_left) < epsilon:
        return left
    # 如果右端点是零点，直接返回
    if abs(f_right) < epsilon:
        return right
    
    # 确保函数在区间两端异号，这是二分法的前提条件
    # 如果同号，调整区间直到异号
    while f_left * f_right > 0:
        left *= 2
        right *= 2
        f_left = poly(xs, left)
        f_right = poly(xs, right)
    
    # 开始二分法迭代
    for _ in range(max_iterations):
        mid = (left + right) / 2
        f_mid = poly(xs, mid)
        
        # 如果中点函数值足够小，认为是零点
        if abs(f_mid) < epsilon:
            return mid
        
        # 根据中点函数值与区间端点函数值的符号关系，缩小区间
        if f_left * f_mid < 0:
            right = mid
            f_right = f_mid
        else:
            left = mid
            f_left = f_mid
    
    # 达到最大迭代次数，返回最后一次的中点
    return (left + right) / 2