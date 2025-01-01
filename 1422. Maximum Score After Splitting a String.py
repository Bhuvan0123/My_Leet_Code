# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
def maxScore(self, s: str) -> int:
        res=0
        n=len(s)
        for i in range(1,n):
            k=(s[:i].count("0"))+(s[i:].count("1"))
            print(s[:i],s[i:])
            print(k)
            res=max(k,res)
        return res