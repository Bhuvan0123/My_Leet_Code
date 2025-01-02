# You are given a 0-indexed array of strings words and a 2D array of integers queries.

# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        arr = [0] * (n + 1)
        vows = {'a', 'e', 'i', 'o', 'u'}

        for i in range(n):
            arr[i + 1] = arr[i]
            if words[i][0] in vows and words[i][-1] in vows:
                arr[i + 1] += 1

        res = []
        for query in queries:
            res.append(arr[query[1] + 1] - arr[query[0]])

        return res