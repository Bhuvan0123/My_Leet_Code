# You are given a string word and a non-negative integer k.

# Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.
def countOfSubstrings(self, word: str, k: int) -> int:
        def func(word,k):
            n=len(word)
            res=0
            cons=0
            left=0
            vm={}
            for right in range(n):
                if word[right] in "aeiou":
                    vm[word[right]]=vm.get(word[right],0)+1
                else:
                    cons+=1
                while len(vm)==5 and cons>=k:
                    res+=n-right
                    if word[left] in "aeiou":
                        vm[word[left]]-=1
                        if vm[word[left]]==0:
                            del vm[word[left]]
                    else:
                        cons-=1
                    left+=1
            return res
        return func(word,k)-func(word,k+1)