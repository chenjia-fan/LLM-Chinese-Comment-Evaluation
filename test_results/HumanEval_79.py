def decimal_to_binary(decimal):
    # 将十进制整数转换为二进制字符串，去掉'0b'前缀
    binary_str = bin(decimal)[2:] if decimal != 0 else '0'
    # 在二进制字符串前后加上'db'
    return f"db{binary_str}db"