# You are given two 0-indexed integer permutations A and B of length n.

# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

# Return the prefix common array of A and B.

# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = []
        dp = [0] * (n + 1)
        temp = 0
        
        for i in range(n):
            if dp[A[i]] == 0:
                dp[A[i]] = 1
            elif dp[A[i]] == 1:
                temp += 1
            if dp[B[i]] == 0:
                dp[B[i]] = 1
            elif dp[B[i]] == 1:
                temp += 1
            res.append(temp)
        return res