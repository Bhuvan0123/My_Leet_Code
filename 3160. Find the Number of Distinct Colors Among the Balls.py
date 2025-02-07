# You are given an integer limit and a 2D array queries of size n x 2.

# There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.

# Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

# Note that when answering a query, lack of a color will not be considered as a color.
def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball={}
        color={}
        res=[]
        d=0
        for i, c in queries:
            if i in ball:
                color[ball[i]] -= 1
                if color[ball[i]] == 0:
                    d -= 1
            ball[i] = c
            color[c] = color.get(c, 0) + 1
            if color[c] == 1: d += 1
            res.append(d)
        return res