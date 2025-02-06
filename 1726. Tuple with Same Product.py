# Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.
def tupleSameProduct(self, nums: List[int]) -> int:
        n=len(nums)
        dic=defaultdict(int)
        for i in range(n):
            for j in range(i+1,n):
                p=nums[i]*nums[j]
                dic[p]+=1
        res=0
        for i in dic.values():
            if i>=2:
                res+=i*(i-1)//2
        return res*8