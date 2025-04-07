# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        n=len(nums)
        if total%2!=0:
            return False
        tar=total//2
        dp=[False]*(tar+1)
        dp[0]=True
        for i in nums:
            for j in range(tar,i-1,-1):
                dp[j]=dp[j] or dp[j-i]
        return dp[tar]