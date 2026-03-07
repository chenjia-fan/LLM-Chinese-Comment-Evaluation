def is_nested(string):
    state = 0
    for ch in string:
        if state == 0:
            if ch == '[':
                state = 1
        elif state == 1:
            if ch == '[':
                state = 2
        elif state == 2:
            if ch == ']':
                state = 3
        elif state == 3:
            if ch == ']':
                return True
    return False