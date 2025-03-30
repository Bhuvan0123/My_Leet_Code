# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.
def partitionLabels(self, s: str) -> List[int]:
        last = {}
        
        for i, char in enumerate(s):
            last[char] = i
        
        res = []
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            end = max(end, last[char])
            
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        
        return res