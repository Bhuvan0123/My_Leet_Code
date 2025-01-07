# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

# A substring is a contiguous sequence of characters within a string
def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        n=len(words)
        for i in range(n):
            for j in range(n):
                if i!=j and words[i] in words[j]:
                    res.append(words[i])
        return list(set(res))