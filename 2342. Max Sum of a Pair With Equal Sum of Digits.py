# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.
def maximumSum(self, nums: List[int]) -> int:
        dp = [-1] * 82 
        res = -1
        for i in nums:
            dsum = sum(int(d) for d in str(i))
            if dp[dsum] != -1:
                res = max(res, i + dp[dsum])
            dp[dsum] = max(dp[dsum], i)
        return res