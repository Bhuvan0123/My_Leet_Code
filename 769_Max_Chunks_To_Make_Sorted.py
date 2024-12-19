'''
19-12-2024
You are given an integer array arr of length n that represents a permutation of the integers
in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and 
individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.
'''

def maxChunksToSorted(self, arr: List[int]) -> int:
        count=0
        diff=0
        for i, x in enumerate(arr):
            diff += x-i
            count += (diff==0)
        return count