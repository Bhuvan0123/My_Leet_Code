# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
def isArraySpecial(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        for i in range(n-1):
            if nums[i]%2==nums[i+1]%2:
                return False
            
        return True