# Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

# Append the character '0' zero times.
# Append the character '1' one times.
# This can be performed any number of times.

# A good string is a string constructed by the above process having a length between low and high (inclusive).

# Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.
def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod=10**9+7
        dp=[0]*(high+1)
        dp[0]=1
        for i in range(1,high+1):
            res=1
            if i>=zero:
                res+=dp[i-zero]
            if i>=one:
                res+=dp[i-one]
            dp[i]=res%mod
        return (dp[high]-dp[low-1]+mod)%mod