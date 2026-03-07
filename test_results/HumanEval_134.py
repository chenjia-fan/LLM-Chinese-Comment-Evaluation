def check_if_last_char_is_a_letter(txt):
    # 检查字符串是否为空
    if not txt:
        return False
    
    last_char = txt[-1]
    # 检查最后一个字符是否为字母
    if not last_char.isalpha():
        return False
    
    # 检查最后一个字符是否前面有空格或为字符串开头
    # 也就是检查它是否是一个独立的单词（长度为1的单词）
    if len(txt) == 1:
        return True
    elif txt[-2] == ' ':
        return True
    else:
        return False