# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        res=[0]*(n*n+1)
        for i in grid:
            for j in i:
                res[j]+=1
        a=0
        b=0
        for i in range(len(res)):
            if res[i]>=2:
                a=i
            elif res[i]==0:
                b=i
        return [a,b]