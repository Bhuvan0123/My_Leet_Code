# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

# A subarray is a contiguous non-empty sequence of elements within an array.
def countGood(self, nums: List[int], k: int) -> int:
        dic = {}
        res = left = 0
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 0
            k -= dic[nums[i]]
            dic[nums[i]] += 1
            while k <= 0:
                dic[nums[left]] -= 1
                k += dic[nums[left]]
                left += 1
            res += left
        return res