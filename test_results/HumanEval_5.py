from typing import List

def intersperse(numbers: List, delimeter) -> List:
    if not numbers:
        return []
    
    result = []
    for num in numbers[:-1]:
        result.append(num)
        result.append(delimeter)
    result.append(numbers[-1])
    return result