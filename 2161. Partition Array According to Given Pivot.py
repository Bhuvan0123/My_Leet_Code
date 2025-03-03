# You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

# Every element less than pivot appears before every element greater than pivot.
# Every element equal to pivot appears in between the elements less than and greater than pivot.
# The relative order of the elements less than pivot and the elements greater than pivot is maintained.
# More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
# Return nums after the rearrangement.
def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        res = [0] * n
        left = 0
        right = n - 1
        i=0
        j=n-1
        while i<n:
            if(nums[i]<pivot):
                res[left]=nums[i]
                left+=1
            if nums[j]>pivot:
                res[right]=nums[j]
                right-=1
            i+=1
            j-=1
        while left<=right:
            res[left]=pivot
            left+=1
        return res
        
        
            
        return res