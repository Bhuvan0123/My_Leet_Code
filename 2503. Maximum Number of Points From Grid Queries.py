# You are given an m x n integer matrix grid and an array queries of size k.

# Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

# If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
# Otherwise, you do not get any points, and you end this process.
# After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

# Return the resulting array answer.
def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        from queue import PriorityQueue
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        sortq = sorted([(val, idx) for idx, val in enumerate(queries)])
        res = [0] * len(queries)
        
        heap = PriorityQueue()
        visited = [[False] * cols for _ in range(rows)]
        
        heap.put((grid[0][0], 0, 0))
        visited[0][0] = True
        points = 0
        
        for query_val, query_idx in sortq:
            while not heap.empty() and heap.queue[0][0] < query_val:
                _, row, col = heap.get()
                points += 1
                
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        not visited[nr][nc]):
                        heap.put((grid[nr][nc], nr, nc))
                        visited[nr][nc] = True
            
            res[query_idx] = points
        
        return res