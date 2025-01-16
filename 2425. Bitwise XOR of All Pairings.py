# You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

# Return the bitwise XOR of all integers in nums3.
def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1,n2=len(nums1),len(nums2)
        x1,x2=0,0
        if n1%2!=0:
            for i in nums2:
                x2^=i
        if n2%2==1:
            for i in nums1:
                x1^=i
        return x1^x2