def encrypt(s):
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            base = ord('a')
            shifted = (ord(char) - base + 2 * 2) % 26
            result.append(chr(base + shifted))
        elif 'A' <= char <= 'Z':
            base = ord('A')
            shifted = (ord(char) - base + 2 * 2) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)
    return ''.join(result)