def select_words(s, n):
    if not s:
        return []
    vowels = set('aeiouAEIOU')
    result = []
    for word in s.split():
        count = 0
        for ch in word:
            if ch.isalpha() and ch not in vowels:
                count += 1
        if count == n:
            result.append(word)
    return result