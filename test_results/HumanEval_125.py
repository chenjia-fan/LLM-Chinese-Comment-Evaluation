def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for ch in txt:
            if 'a' <= ch <= 'z' and (ord(ch) - ord('a')) % 2 == 1:
                count += 1
        return count