# You are given a 0-indexed integer array nums.

# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
def maximumTripletValue(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        left=[0]*n
        right=[0]*n
        for i in range(1,n):
            left[i]=max(left[i-1],nums[i-1])
            right[n-i-1]=max(right[n-i],nums[n-i])
        for j in range(1,n-1):
            res=max(res,(left[j]-nums[j])*right[j])
        return res