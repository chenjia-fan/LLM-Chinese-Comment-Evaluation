def correct_bracketing(brackets: str):
    balance = 0
    for char in brackets:
        if char == '(':
            balance += 1
        else:  # char == ')'
            balance -= 1
            if balance < 0:
                return False
    return balance == 0