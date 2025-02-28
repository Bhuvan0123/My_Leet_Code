# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

# A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.
def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m=len(str1)
        n=len(str2)
        dp=[[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        i,j=m,n
        res=""
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                res+=str1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:
                res+=str1[i-1]
                i-=1
            else:
                res+=str2[j-1]
                j-=1
        while i>0:
            res+=str1[i-1]
            i-=1
        while j>0:
            res+=str2[j-1]
            j-=1
        return res[::-1]