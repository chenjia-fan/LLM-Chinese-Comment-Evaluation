def is_palindrome(string: str) -> bool:
    """检查给定的字符串是否是回文。"""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """找到以给定的字符串开头的最短回文。"""
    if not string:
        return ''
    
    # 从末尾开始寻找最长回文后缀
    for i in range(len(string)):
        # 检查从位置i到末尾的子串是否是回文
        if is_palindrome(string[i:]):
            # 将回文前缀前的部分反转并附加到末尾
            return string + string[:i][::-1]
    
    # 理论上不会执行到此处，但为了完整性返回原字符串
    return string