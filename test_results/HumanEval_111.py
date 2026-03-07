def histogram(test):
    from collections import Counter
    if not test:
        return {}
    letters = test.split()
    counts = Counter(letters)
    max_count = max(counts.values()) if counts else 0
    return {k: v for k, v in counts.items() if v == max_count}