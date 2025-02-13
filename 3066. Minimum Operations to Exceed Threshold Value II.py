# You are given a 0-indexed integer array nums, and an integer k.

# In one operation, you will:

# Take the two smallest integers x and y in nums.
# Remove x and y from nums.
# Add min(x, y) * 2 + max(x, y) anywhere in the array.
# Note that you can only apply the described operation if nums contains at least two elements.

# Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
def minOperations(self, nums: List[int], k: int) -> int:
        res=0
        arr=nums
        heapq.heapify(arr)
        n=len(nums)
        for i in range(n):
            x=heapq.heappop(arr)
            if x<k:
                res+=1
                y=heapq.heappop(arr)
                val=(y*2)+x
                if x<y:
                    val=(x*2)+y
                heapq.heappush(arr,val)
            else:
                break
        return res