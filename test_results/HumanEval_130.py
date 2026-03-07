def tri(n):
    result = []
    for i in range(n + 1):
        if i == 1:
            result.append(3)
        elif i % 2 == 0:
            result.append(1 + i // 2)
        else:  # i 是奇数且大于1
            next_val = 1 + (i + 1) // 2
            result.append(result[i - 1] + result[i - 2] + next_val)
    return result