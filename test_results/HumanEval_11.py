from typing import List

def string_xor(a: str, b: str) -> str:
    # 确保两个字符串长度相同
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length")
    
    # 逐位进行异或操作
    result_chars = []
    for i in range(len(a)):
        if a[i] == b[i]:
            result_chars.append('0')
        else:
            result_chars.append('1')
    
    return ''.join(result_chars)