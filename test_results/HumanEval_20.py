from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers_sorted = sorted(numbers)
    min_diff = float('inf')
    result = (0, 0)
    
    for i in range(len(numbers_sorted) - 1):
        diff = numbers_sorted[i+1] - numbers_sorted[i]
        if diff < min_diff:
            min_diff = diff
            result = (numbers_sorted[i], numbers_sorted[i+1])
    
    return result