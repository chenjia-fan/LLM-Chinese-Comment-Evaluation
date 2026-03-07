def compare_one(a, b):
    def to_float(val):
        if isinstance(val, (int, float)):
            return float(val)
        elif isinstance(val, str):
            # 将逗号替换为点，以支持不同的小数点表示
            return float(val.replace(',', '.'))
        else:
            # 根据问题描述，输入只会是整数、浮点数或字符串
            raise TypeError("Unsupported type for comparison")

    num_a = to_float(a)
    num_b = to_float(b)

    if num_a > num_b:
        return a
    elif num_a < num_b:
        return b
    else:
        return None