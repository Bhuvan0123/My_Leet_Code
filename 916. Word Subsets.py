# You are given two string arrays words1 and words2.

# A string b is a subset of string a if every letter in b occurs in a including multiplicity.

# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.

# Return an array of all the universal strings in words1. You may return the answer in any order.
def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = Counter()
        for i in words2:
            cur = Counter(i)
            for c in cur:
                counter[c] = max(counter[c], cur[c])
        
        res = []
        for i in words1:
            cur = Counter(i)
            if all(cur[ch] >= counter[ch] for ch in counter):
                res.append(i)
        
        return res