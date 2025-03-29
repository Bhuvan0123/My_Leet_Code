# You are given an array nums of n positive integers and an integer k.

# Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:

# Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
# Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
# Multiply your score by x.
# Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.

# The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.

# Return the maximum possible score after applying at most k operations.

# Since the answer may be large, return it modulo 109 + 7.
def maximumScore(self, nums: List[int], k: int) -> int:
        def primeFactors(n):
            i = 2
            ans = set()
            while i * i <= n:
                while n % i == 0:
                    ans.add(i)
                    n //= i
                i += 1
            if n > 1:
                ans.add(n)
            return len(ans)
        mod = 10**9 + 7
        arr = [(i, primeFactors(x), x) for i, x in enumerate(nums)]
        n = len(nums)

        left = [-1] * n
        right = [n] * n
        stk = []
        for i, f, x in arr:
            while stk and stk[-1][0] < f:
                stk.pop()
            if stk:
                left[i] = stk[-1][1]
            stk.append((f, i))

        stk = []
        for i, f, x in arr[::-1]:
            while stk and stk[-1][0] <= f:
                stk.pop()
            if stk:
                right[i] = stk[-1][1]
            stk.append((f, i))

        arr.sort(key=lambda x: -x[2])
        ans = 1
        for i, f, x in arr:
            l, r = left[i], right[i]
            cnt = (i - l) * (r - i)
            if cnt <= k:
                ans = ans * pow(x, cnt, mod) % mod
                k -= cnt
            else:
                ans = ans * pow(x, k, mod) % mod
                break
        return ans