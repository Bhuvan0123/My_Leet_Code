# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.
def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dic = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        hash_map = {}

        def func():
            visit = {}
            area = []
            def dfs(i, j):
                nonlocal area
                visit[(i, j)] = True
                area.append((i, j))
                for dx, dy in dic:
                    ni, nj = i + dx, j + dy
                    if ni >= 0 and ni < n and nj >= 0 and nj < m and (ni, nj) not in visit and grid[ni][nj] == 1:
                        dfs(ni, nj)
            
            res = 0
            for i in range(n):
                for j in range(m):
                    if (i, j) not in visit and grid[i][j] == 1:
                        area = []
                        dfs(i, j)
                        for indx in area:
                            hash_map[indx] = (len(area), (i, j))
                        res = max(res, len(area))
            return res
            
        
        res = func()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    area = 1
                    entry = []
                    for dx, dy in dic:
                        ni, nj = i + dx, j + dy
                        if ni >= 0 and ni < n and nj >= 0 and nj < m and grid[ni][nj] == 1:
                            if hash_map[(ni, nj)][1] not in entry:
                                area += hash_map[(ni, nj)][0]
                                entry.append(hash_map[(ni, nj)][1])

                    res = max(res, area)
        return res
