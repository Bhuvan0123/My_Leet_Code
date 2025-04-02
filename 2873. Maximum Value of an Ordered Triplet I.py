# You are given a 0-indexed integer array nums.

# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
def maximumTripletValue(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    x=(nums[i]-nums[j])*nums[k]
                    if x>0 and x>res:
                        res=x
        return res