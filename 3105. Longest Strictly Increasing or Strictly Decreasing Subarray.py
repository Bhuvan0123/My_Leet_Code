# You are given an array of integers nums. Return the length of the longest 
# subarray
#  of nums which is either 
# strictly increasing
#  or 
# strictly decreasing
# .
def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        elif n==1:
            return 1
        res=1
        inc=1
        dec=1
        for i in range(n-1):
            if nums[i]<nums[i+1]:
                inc+=1
                dec=1
            elif nums[i]>nums[i+1]:
                dec+=1
                inc=1
            else:
                inc=dec=1
            res=max(res,inc,dec)
        return res