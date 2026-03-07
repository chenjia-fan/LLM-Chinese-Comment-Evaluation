from typing import List

def remove_duplicates(numbers):
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
    result = []
    for num in numbers:
        if count[num] == 1:
            result.append(num)
    return result