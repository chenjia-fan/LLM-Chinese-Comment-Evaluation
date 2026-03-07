def int_to_mini_roman(number):
    # 映射表：值和对应的罗马数字（小写），按值降序排列
    value_map = [
        (1000, 'm'),
        (900, 'cm'),
        (500, 'd'),
        (400, 'cd'),
        (100, 'c'),
        (90, 'xc'),
        (50, 'l'),
        (40, 'xl'),
        (10, 'x'),
        (9, 'ix'),
        (5, 'v'),
        (4, 'iv'),
        (1, 'i')
    ]
    
    result = ''
    for value, roman in value_map:
        while number >= value:
            result += roman
            number -= value
    return result