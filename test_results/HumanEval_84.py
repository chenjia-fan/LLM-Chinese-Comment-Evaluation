def solve(N):
    # 计算N的各位数字之和
    digit_sum = sum(int(d) for d in str(N))
    # 转换为二进制字符串，并去掉'0b'前缀
    return bin(digit_sum)[2:]