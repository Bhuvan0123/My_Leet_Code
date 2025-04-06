# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.
def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp=[[i] for i in nums]
        n=len(nums)
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(dp[j])+1>len(dp[i]):
                    dp[i]=dp[j]+[nums[i]]
        return max(dp,key=len)