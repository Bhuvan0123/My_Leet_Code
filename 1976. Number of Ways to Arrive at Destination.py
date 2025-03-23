# You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

# You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

# Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.
def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
            
        distance = [float('inf')] * n
        res = [0] * n
        
        distance[0] = 0
        res[0] = 1
        
        pq = [(0, 0)]
        
        MOD = 10**9 + 7
        
        # Dijkstra's algorithm
        while pq:
            d, node = heapq.heappop(pq)
            
            if d > distance[node]:
                continue
                
            for neighbor, time in graph[node]:
                if distance[node] + time < distance[neighbor]:
                    distance[neighbor] = distance[node] + time
                    res[neighbor] = res[node]
                    heapq.heappush(pq, (distance[neighbor], neighbor))
                elif distance[node] + time == distance[neighbor]:
                    res[neighbor] = (res[neighbor] + res[node]) % MOD
        
        return res[n-1]