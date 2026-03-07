import re

def is_bored(S):
    count = 0
    sentences = re.split(r'[.!?]', S)
    for sentence in sentences:
        stripped = sentence.strip()
        if stripped.startswith('I'):
            count += 1
    return count