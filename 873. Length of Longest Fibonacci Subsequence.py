# A sequence x1, x2, ..., xn is Fibonacci-like if:

# n >= 3
# xi + xi+1 == xi+2 for all i + 2 <= n
# Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

# A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n=len(arr)
        dp=[[0]*n for i in range(n)]
        maxlen=0
        for i in range(2,n):
            start=0
            end=i-1
            while start<end:
                pair=arr[start]+arr[end]
                if pair>arr[i]:
                    end-=1
                elif pair<arr[i]:
                    start+=1
                else:
                    dp[end][i]=dp[start][end]+1
                    maxlen=max(maxlen,dp[end][i])
                    end-=1
                    start+=1
        return maxlen+2 if maxlen>0  else 0