# You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

# A uni-value grid is a grid where all the elements of it are equal.

# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr=[]
        for i in grid:
            for j in i:
                arr.append(j)
        arr.sort()
        diff=[abs(i-arr[0])%x for i in arr]
        if any(d!=0 for d in diff):
            return -1
        med=arr[len(arr)//2]
        return sum(abs(i-med)//x for i in arr)