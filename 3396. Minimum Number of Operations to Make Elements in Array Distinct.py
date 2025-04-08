# You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:

# Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
# Note that an empty array is considered to have distinct elements. Return the minimum number of operations needed to make the elements in the array distinct.
def minimumOperations(self, nums: List[int]) -> int:
        def isdis(nums):
            if nums==[]:
                return True
            k=set(nums)
            for i in k:
                if nums.count(i)>1:
                    return False
            return True
        if(isdis(nums)):
            return 0
        res=0
        while(not isdis(nums)):
            if len(nums)<=3:
                nums=[]
            else:
                nums=nums[3:]
            res+=1
        return res