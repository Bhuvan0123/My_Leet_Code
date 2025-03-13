# You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

# Each queries[i] represents the following action on nums:

# Decrement the value at each index in the range [li, ri] in nums by at most vali.
# The amount by which each value is decremented can be chosen independently for each index.
# A Zero Array is an array with all its elements equal to 0.

# Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.
def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        
        def func(k):
            diff = [0] * (n + 1)
            for i in range(k):
                left, right, val = queries[i]
                diff[left] += val
                diff[right + 1] -= val
            curr = 0
            for i in range(n):
                curr += diff[i]
                if curr < nums[i]:
                    return False
            return True
        if all(x == 0 for x in nums):
            return 0
        l, r = 1, len(queries)
        if not func(r):
            return -1
        
        while l < r:
            mid = l + (r - l) // 2
            
            if func(mid):
                r = mid
            else:
                l = mid + 1
        
        return l