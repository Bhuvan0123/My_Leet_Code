# Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.
def trapRainWater(self, heightMap: List[List[int]]) -> int:
        import heapq
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []

        for i in range(m):
            for j in [0, n - 1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in [0, m - 1]:
                if not visited[i][j]:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0

        while heap:
            height, x, y = heapq.heappop(heap)

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    res += max(0, height - heightMap[nx][ny])
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True

        return res