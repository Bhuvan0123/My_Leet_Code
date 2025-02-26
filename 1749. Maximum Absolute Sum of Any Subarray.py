# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.
 
def maxAbsoluteSum(self, nums: List[int]) -> int:
        sum=0
        minsum=0
        maxsum=0
        for i in nums:
            sum+=i
            if sum<minsum:
                minsum=sum
            if sum>maxsum:
                maxsum=sum
        return abs(maxsum-minsum)