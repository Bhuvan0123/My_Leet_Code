# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i1=0
        i2=0
        n=len(s1)
        diff=0
        for i in range(n):
            if s1[i]!=s2[i]:
                diff+=1
                if diff>2:
                    return False
                elif diff==1:
                    i1=i
                else:
                    i2=i
        print(i1,i2)
        return (s1[i1]==s2[i2] and s1[i2]==s2[i1])
#or the another approach
def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff=0
        if Counter(s1)!=Counter(s2):
            return False
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                diff+=1
        return diff==2 or diff==0