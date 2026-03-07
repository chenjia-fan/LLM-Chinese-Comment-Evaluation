def solve(s):
    # 检查字符串是否包含字母
    has_letter = any(c.isalpha() for c in s)
    
    if has_letter:
        # 对每个字符进行大小写转换或保持不变
        result = []
        for c in s:
            if c.isalpha():
                if c.islower():
                    result.append(c.upper())
                else:
                    result.append(c.lower())
            else:
                result.append(c)
        return ''.join(result)
    else:
        # 反转字符串
        return s[::-1]