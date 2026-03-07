import re

def anti_shuffle(s):
    parts = re.findall(r'\S+|\s+', s)
    result_parts = []
    for part in parts:
        if part.isspace():
            result_parts.append(part)
        else:
            sorted_part = ''.join(sorted(part))
            result_parts.append(sorted_part)
    return ''.join(result_parts)