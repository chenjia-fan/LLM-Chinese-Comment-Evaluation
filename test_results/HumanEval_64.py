def vowels_count(s):
    if not s:
        return 0
    s_lower = s.lower()
    count = 0
    for ch in s_lower:
        if ch in 'aeiou':
            count += 1
    if s_lower[-1] == 'y':
        count += 1
    return count