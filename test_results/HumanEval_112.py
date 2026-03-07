def reverse_delete(s, c):
    # 删除 s 中所有出现在 c 中的字符
    result_str = ''.join(ch for ch in s if ch not in c)
    # 检查结果字符串是否为回文
    is_palindrome = result_str == result_str[::-1]
    return (result_str, is_palindrome)