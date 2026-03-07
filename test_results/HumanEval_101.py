import re

def words_string(s):
    # 使用正则表达式匹配一个或多个非逗号、非空白字符
    return re.findall(r'[^,\s]+', s)