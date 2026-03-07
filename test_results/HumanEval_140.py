def fix_spaces(text):
    result = []
    space_count = 0
    for ch in text:
        if ch == ' ':
            space_count += 1
        else:
            if space_count > 2:
                result.append('-')
            elif space_count > 0:
                result.append('_' * space_count)
            space_count = 0
            result.append(ch)
    if space_count > 2:
        result.append('-')
    elif space_count > 0:
        result.append('_' * space_count)
    return ''.join(result)