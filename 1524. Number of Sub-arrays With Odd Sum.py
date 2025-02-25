# Given an array of integers arr, return the number of subarrays with an odd sum.

# Since the answer can be very large, return it modulo 109 + 7.
def numOfSubarrays(self, arr: List[int]) -> int:
        res=0
        presum=0
        for i in arr:
            presum+=i
            res+=presum%2
        res += (len(arr)-res)*res
        return res%(1000000007)