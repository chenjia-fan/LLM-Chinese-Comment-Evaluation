def decode_cyclic(s: str):
    """
    输入encode_cyclic函数编码的字符串，返回解码后的字符串。
    """
    # 将字符串拆分为组，每个组的长度为3
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # 在每个组中反向循环元素，除非该组的元素少于3个
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)