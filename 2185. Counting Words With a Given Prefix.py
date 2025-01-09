# You are given an array of strings words and a string pref.

# Return the number of strings in words that contain pref as a prefix.

# A prefix of a string s is any leading contiguous substring of s.
def prefixCount(self, words: List[str], pref: str) -> int:
        res=0
        for i in words:
            if i.startswith(pref):
                res+=1
        return res