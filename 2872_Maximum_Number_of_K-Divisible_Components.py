'''
There is an undirected tree with n nodes labeled from 0 to n - 1.
You are given the integer n and a 2D integer array edges of length n - 1, where 
edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are also given a 0-indexed integer array values of length n, where values[i] 
is the value associated with the ith node, and an integer k.

A valid split of the tree is obtained by removing any set of edges, possibly empty, 
from the tree such that the resulting components all have values that are divisible by k,
where the value of a connected component is the sum of the values of its nodes.

Return the maximum number of components in any valid split.
'''

def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.ans = 0
        def dfs(root, parent):
            s = values[root]
            for child in graph[root]:
                if child != parent:
                    s += dfs(child, root)
            if s%k == 0:
                self.ans += 1
                return 0
            return s

        dfs(0, -1)
        return self.ans