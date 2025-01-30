# You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

# You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

# Divide the nodes of the graph into m groups (1-indexed) such that:

# Each node in the graph belongs to exactly one group.
# For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
# Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i - 1].append(j - 1)
            graph[j - 1].append(i - 1)
        dic = defaultdict(int)
        for i in range(n):
            q = deque([i])
            dist = [0] * n
            dist[i] = maxi = 1
            root = i
            while q:
                a = q.popleft()
                root = min(root, a)
                for b in graph[a]:
                    if dist[b] == 0:
                        dist[b] = dist[a] + 1
                        maxi = max(maxi, dist[b])
                        q.append(b)
                    elif abs(dist[b] - dist[a]) != 1:
                        return -1
            dic[root] = max(dic[root], maxi)
        return sum(dic.values())