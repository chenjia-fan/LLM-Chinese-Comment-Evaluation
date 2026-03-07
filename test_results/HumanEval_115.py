def max_fill(grid, capacity):
    import math
    total = 0
    for well in grid:
        cnt = 0
        for cell in well:
            if cell == 1:
                cnt += 1
            else:
                total += math.ceil(cnt / capacity) if cnt > 0 else 0
                cnt = 0
        if cnt > 0:
            total += math.ceil(cnt / capacity)
    return total