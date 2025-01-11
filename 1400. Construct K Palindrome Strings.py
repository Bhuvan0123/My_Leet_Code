# Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.
def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        sor=sorted(s)
        count=0
        i=0
        n=len(s)
        while i<n:
            c=sor[i]
            temp=0
            while i<n and sor[i]==c:
                temp+=1
                i+=1
            if temp%2==1:
                count+=1
        return count<=k