# You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

# Return the number of complete connected components of the graph.

# A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

# A connected component is said to be complete if there exists an edge between every pair of its vertices.
def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import deque
        adj=[[] for _  in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=[False]*n
        res=0
        def func(node):
            queue=deque([node])
            visited[node]=True
            temp=[]
            while queue:
                curr=queue.popleft()
                temp.append(curr)
                for i in adj[curr]:
                    if not visited[i]:
                        visited[i]=True
                        queue.append(i)
            return temp
        for i in range(n):
            if not visited[i]:
                temp=func(i)
                k=0
                for j in temp:
                    if len(adj[j])==len(temp)-1:
                        k+=1
                if k==len(temp):
                    res+=1
        return res