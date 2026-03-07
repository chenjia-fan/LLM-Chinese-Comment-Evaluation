def encode(message):
    result = []
    vowel_map = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
                 'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
    
    for char in message:
        if char.isalpha():
            swapped = char.swapcase()
            if swapped in vowel_map:
                result.append(vowel_map[swapped])
            else:
                result.append(swapped)
        else:
            result.append(char)
    
    return ''.join(result)