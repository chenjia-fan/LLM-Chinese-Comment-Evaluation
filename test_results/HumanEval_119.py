def match_parens(lst):
    def is_good_concat(first, second):
        count = 0
        for ch in first:
            count += 1 if ch == '(' else -1
            if count < 0:
                return False
        for ch in second:
            count += 1 if ch == '(' else -1
            if count < 0:
                return False
        return count == 0
    
    s1, s2 = lst
    if is_good_concat(s1, s2) or is_good_concat(s2, s1):
        return 'Yes'
    else:
        return 'No'