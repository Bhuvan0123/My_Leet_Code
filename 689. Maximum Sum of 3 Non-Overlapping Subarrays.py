# Given an integer array nums and an integer k, find three non-overlapping subarrays 
# of length k with maximum sum and return them.

# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.
def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sum1 = sum(nums[:k])
        sum2 = sum(nums[k:2*k])
        sum3 = sum(nums[2*k:3*k])

        max1 = sum1
        max12 = sum1 + sum2
        maxall = sum1 + sum2 + sum3

        index1 = 0
        index12 = 0
        index21 = k
        ans = [0, k, 2 * k]

        for i in range(1, n - 3 * k + 1):
            sum1 = sum1 - nums[i - 1] + nums[i + k - 1]
            sum2 = sum2 - nums[i + k - 1] + nums[i + 2 * k - 1]
            sum3 = sum3 - nums[i + 2 * k - 1] + nums[i + 3 * k - 1]

            if sum1 > max1:
                max1 = sum1
                index1 = i

            if max1 + sum2 > max12:
                max12 = max1 + sum2
                index12 = index1
                index21 = i + k

            if max12 + sum3 > maxall:
                maxall = max12 + sum3
                ans = [index12, index21, i + 2 * k]

        return ans