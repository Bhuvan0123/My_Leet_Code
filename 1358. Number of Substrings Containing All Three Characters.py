# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.
def numberOfSubstrings(self, s: str) -> int:
        res=0
        right=0
        abc=[-1,-1,-1]
        n=len(s)
        while right<n:
            abc[ord(s[right])-ord('a')]=right
            res+=min(abc)+1
            right+=1
        return res