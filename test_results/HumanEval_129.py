def minPath(grid, k):
    n = len(grid)
    # 找到值为1的单元格作为起点
    start = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                start = (i, j)
                break
        if start:
            break
    r, c = start
    path = [1]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for _ in range(k - 1):
        # 收集所有合法邻居
        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                neighbors.append((nr, nc))
        # 选择值最小的邻居
        min_val = float('inf')
        next_pos = None
        for nr, nc in neighbors:
            val = grid[nr][nc]
            if val < min_val:
                min_val = val
                next_pos = (nr, nc)
        r, c = next_pos
        path.append(min_val)
    return path