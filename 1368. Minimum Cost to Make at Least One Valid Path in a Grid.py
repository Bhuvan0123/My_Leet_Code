# Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

# 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
# 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
# 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
# 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
# Notice that there could be some signs on the cells of the grid that point outside the grid.

# You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

# You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

# Return the minimum cost to make the grid have at least one valid path.
def minCost(self, grid: List[List[int]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dq = deque([(0, 0)])
        dist[0][0] = 0
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        
        while dq:
            x, y = dq.popleft()
            curDir = grid[x][y] - 1
            for dir in range(4):
                nx, ny = x + dx[dir], y + dy[dir]
                if 0 <= nx < m and 0 <= ny < n:
                    cost = dist[x][y] + (0 if dir == curDir else 1)
                    if cost < dist[nx][ny]:
                        dist[nx][ny] = cost
                        if dir == curDir:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))
        
        return dist[m - 1][n - 1]