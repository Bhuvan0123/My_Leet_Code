# You are given three integers start, finish, and limit. You are also given a 0-indexed string s representing a positive integer.

# A positive integer x is called powerful if it ends with s (in other words, s is a suffix of x) and each digit in x is at most limit.

# Return the total number of powerful integers in the range [start..finish].

# A string x is a suffix of a string y if and only if x is a substring of y that starts from some index (including 0) in y and extends to the index y.length - 1. For example, 25 is a suffix of 5125 whereas 512 is not.
def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def func(num: int) -> int:
            numstr = str(num)
            suffix_len = len(s)
            prefix_len = len(numstr) - suffix_len

            if prefix_len < 0:
                return 0

            dp = [[0] * 2 for _ in range(prefix_len + 1)]

            dp[prefix_len][0] = 1
            suffix_from_num = numstr[prefix_len:]
            dp[prefix_len][1] = int(suffix_from_num) >= int(s)

            for i in range(prefix_len - 1, -1, -1):
                digit = int(numstr[i])
                dp[i][0] = (limit + 1) * dp[i + 1][0]
                if digit <= limit:
                    dp[i][1] = digit * dp[i + 1][0] + dp[i + 1][1]
                else:
                    dp[i][1] = (limit + 1) * dp[i + 1][0]

            return dp[0][1]

        return func(finish) - func(start - 1)