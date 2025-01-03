# You are given a 0-indexed integer array nums of length n.

# nums contains a valid split at index i if the following are true:

# The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
# There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.
def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        sumnums=sum(nums)
        index=0
        res=0
        for i in range(n-1):
            index+=nums[i]
            res+=(2*index>=sumnums)
        return res