# An element x of an integer array arr of length m is dominant if more than half the elements of arr have a value of x.

# You are given a 0-indexed integer array nums of length n with one dominant element.

# You can split nums at an index i into two arrays nums[0, ..., i] and nums[i + 1, ..., n - 1], but the split is only valid if:

# 0 <= i < n - 1
# nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.
# Here, nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j, both ends being inclusive. Particularly, if j < i then nums[i, ..., j] denotes an empty subarray.

# Return the minimum index of a valid split. If no valid split exists, return -1.
def minimumIndex(self, nums: List[int]) -> int:
        from collections import Counter

        freq = Counter(nums)
        n = len(nums)
        d, count = 0, 0

        for num, c in freq.items():
            if c > n // 2:
                d, count = num, c
                break

        left_count = 0
        for i in range(n - 1):
            if nums[i] == d:
                left_count += 1
            left_size = i + 1
            right_size = n - left_size
            right_count = count - left_count

            if left_count > left_size // 2 and right_count > right_size // 2:
                return i
        return -1