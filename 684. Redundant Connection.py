# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        root=list(range(n+1))
        def func(temp):
            if root[temp]!=temp:
                root[temp]=func(root[temp])
            return root[temp]
        for i, j in edges:
            r1=func(i)
            r2=func(j)
            if r1==r2:
                return [i,j]
            root[r2]=r1