# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

# A land cell if grid[r][c] = 0, or
# A water cell containing grid[r][c] fish, if grid[r][c] > 0.
# A fisher can start at any water cell (r, c) and can do the following operations any number of times:

# Catch all the fish at cell (r, c), or
# Move to any adjacent water cell.
# Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.
def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n, dirt = len(grid), len(grid[0]), [-1,0,1,0,-1]
        def func(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 0
            res = grid[i][j]
            grid[i][j] = 0
            for k in range(4):
                res += func(i+dirt[k], j+dirt[k+1])
            return res
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, func(i,j))
        return res