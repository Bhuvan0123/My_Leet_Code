'''
You are given a 0-indexed array heights of positive integers, where heights[i] represents 
the height of the ith building.

If a person is in building i, they can move to any other building j if and only if i < j and
heights[i] < heights[j].

You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice
is in building ai while Bob is in building bi.

Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob 
can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set 
ans[i] to -1.
'''
def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(heights), len(queries)
        res = [-1] * q
        defe = [[] for _ in range(n)]
        pq = []

        for i in range(q):
            a, b = queries[i]
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                res[i] = b
            else:
                defe[b].append((heights[a], i))

        for i in range(n):
            for query in defe[i]:
                heapq.heappush(pq, query)
            while pq and pq[0][0] < heights[i]:
                res[pq[0][1]] = i
                heapq.heappop(pq)
                

        return res