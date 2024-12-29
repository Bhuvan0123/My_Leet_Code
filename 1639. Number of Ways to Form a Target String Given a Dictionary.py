# You are given a list of strings of the same length words and a string target.

# Your task is to form target using the given words under the following rules:

# target should be formed from left to right.
# To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
# Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
# Repeat the process until you form the string target.
# Notice that you can use multiple characters from the same string in words provided the conditions above are met.

# Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.



def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7
        n = len(words)
        m = len(words[0])
        arr = [[0] * 26 for _ in range(m)]
        for i in words:
            for j in range(m):
                arr[j][ord(i[j]) - ord('a')] += 1

        dp = [[-1] * len(target) for _ in range(m)]

        def func(i: int, j: int) -> int:
            if j == len(target):
                return 1  
            if i == len(arr):
                return 0  
            if dp[i][j] != -1:
                return dp[i][j]  

            count = func(i + 1, j) 
            count %= mod
            count += (arr[i][ord(target[j]) - ord('a')] * func(i + 1, j + 1)) % mod
            count %= mod
            dp[i][j] = count
            return dp[i][j]

        return func(0, 0)
