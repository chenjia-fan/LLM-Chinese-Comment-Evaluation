def find_max(words):
    max_unique = -1
    result = None
    for word in words:
        unique_count = len(set(word))
        if unique_count > max_unique:
            max_unique = unique_count
            result = word
        elif unique_count == max_unique:
            if result is None or word < result:
                result = word
    return result