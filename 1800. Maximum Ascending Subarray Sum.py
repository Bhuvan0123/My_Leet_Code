# Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

# A subarray is defined as a contiguous sequence of numbers in an array.

# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.
def maxAscendingSum(self, nums: List[int]) -> int:
        ind=nums[0]
        res=nums[0]
        n=len(nums)
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                ind+=nums[i]
            else:
                ind=nums[i]
            res=max(res,ind)
        return res