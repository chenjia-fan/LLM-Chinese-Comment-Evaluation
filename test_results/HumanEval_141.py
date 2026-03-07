def file_name_check(file_name):
    # 检查点的数量
    if file_name.count('.') != 1:
        return 'No'
    
    # 分割文件名
    name_part, ext_part = file_name.split('.', 1)
    
    # 检查名称部分非空且以字母开头
    if not name_part or not name_part[0].isalpha():
        return 'No'
    
    # 检查扩展名是否在允许列表中
    if ext_part not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # 检查数字数量是否不超过3个
    digit_count = sum(1 for char in file_name if char.isdigit())
    if digit_count > 3:
        return 'No'
    
    return 'Yes'