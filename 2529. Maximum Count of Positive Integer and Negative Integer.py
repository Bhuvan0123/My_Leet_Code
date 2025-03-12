# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.
def maximumCount(self, nums: List[int]) -> int:
        neg=0
        zero=0
        n=len(nums)
        for i in nums:
            if i>0:
                break
            elif i==0:
                zero+=1
            else:
                neg+=1
        return max(neg,n-neg-zero)