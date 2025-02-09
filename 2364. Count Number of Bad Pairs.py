# You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

# Return the total number of bad pairs in nums.

def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        dic={}
        res=0
        for i,val in enumerate(nums):
            k=val-i
            res+=dic.get(k,0)
            dic[k]=dic.get(k,0)+1
        return (n*(n-1))//2 - res