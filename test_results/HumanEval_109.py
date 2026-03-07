def move_one_ball(arr):
    n = len(arr)
    if n <= 1:
        return True
    count = 0
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            count += 1
    return count == 1