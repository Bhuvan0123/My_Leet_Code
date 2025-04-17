# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
def countPairs(self, nums: List[int], k: int) -> int:
        res=0
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if(nums[i]==nums[j] and (i*j)%k==0):
                    res+=1
        return res