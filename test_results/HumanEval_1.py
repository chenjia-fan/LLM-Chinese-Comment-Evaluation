from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    # 移除所有空格
    s = paren_string.replace(" ", "")
    
    result = []
    balance = 0
    current_start = 0
    
    for i, char in enumerate(s):
        if char == '(':
            balance += 1
            if balance == 1:  # 新的最外层组开始
                current_start = i
        elif char == ')':
            balance -= 1
            if balance == 0:  # 最外层组结束
                result.append(s[current_start:i+1])
    
    return result