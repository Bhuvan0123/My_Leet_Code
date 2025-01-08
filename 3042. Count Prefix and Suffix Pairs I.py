# You are given a 0-indexed string array words.

# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:

# isPrefixAndSuffix(str1, str2) returns true if str1 is both a 
# prefix
#  and a 
# suffix
#  of str2, and false otherwise.
# For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.

# Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.
def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def func(s1,s2):
            n1=len(s1)
            n2=len(s2)
            if n1>n2:
                return False
            return s2[:n1]==s1 and s2[-n1:]==s1
        res=0
        n=len(words)
        for i in range(n):
            for j in range(i+1,n):
                if func(words[i],words[j]):
                    res+=1
        return res