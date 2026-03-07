def get_max_triples(n):
    # 计算模3余2的个数
    count0 = (n + 1) // 3
    # 其余为模3余0或1的个数
    count1 = n - count0
    # 计算组合数 C(x,3)
    def comb(x):
        if x < 3:
            return 0
        return x * (x - 1) * (x - 2) // 6
    return comb(count0) + comb(count1)