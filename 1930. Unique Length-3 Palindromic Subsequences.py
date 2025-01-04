# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

# A palindrome is a string that reads the same forwards and backwards.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
def countPalindromicSubsequence(self, s: str) -> int:
        dp = [0] * 26
        for i in s:
            dp[ord(i) - ord('a')] += 1
        
        dp2 = [0] * 26
        res = set()
        
        for i in range(len(s)):
            t = ord(s[i]) - ord('a')
            dp[t] -= 1
            for j in range(26):
                if dp2[j] > 0 and dp[j] > 0:
                    res.add(26 * t + j)
            dp2[t] += 1
        
        return len(res)