# You are given an array nums consisting of positive integers.

# We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

# Return the length of the longest nice subarray.

# A subarray is a contiguous part of an array.

# Note that subarrays of length 1 are always considered nice.
def longestNiceSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        elif n==1:
            return 1
        res=0
        used=0
        left=0
        for right in range(n):
            while (used & nums[right])!=0:
                used^=nums[left]
                left+=1
            used|=nums[right]
            res=max(res,right-left+1)
        return res