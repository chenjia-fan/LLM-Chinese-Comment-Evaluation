from typing import List

def sort_numbers(numbers):
    # 建立单词到数字的映射
    word_to_num = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    # 建立数字到单词的映射
    num_to_word = {v: k for k, v in word_to_num.items()}
    
    # 分割字符串
    words = numbers.split()
    
    # 转换为数字列表并排序
    nums = [word_to_num[w] for w in words]
    nums.sort()
    
    # 转换回单词并连接
    result = ' '.join(num_to_word[n] for n in nums)
    
    return result