# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.

# Return the number of good triplets.
def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res=0
        n=len(arr)
        for i in range(0,n-2):
            for k in range(i+2,n):
                if abs(arr[i]-arr[k])>c:
                    continue
                for j in range(i+1,k):
                    if((abs(arr[i]-arr[j])<=a) and (abs(arr[j]-arr[k])<=b)):
                        res+=1
                    
        return res