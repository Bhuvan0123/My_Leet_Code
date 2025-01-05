# You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

# Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

# Return the final string after all such shifts to s are applied.
def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * (n + 1)
        for i in shifts:
            start, end, direction = i
            arr[start] += (1 if direction == 1 else -1)
            if end + 1 < n:
                arr[end + 1] -= (1 if direction == 1 else -1)
        curr = 0
        res = list(s)
        for i in range(n):
            curr += arr[i]
            temp = (curr % 26 + 26) % 26
            res[i] = chr((ord(res[i]) - ord('a') + temp) % 26 + ord('a'))

        return ''.join(res)