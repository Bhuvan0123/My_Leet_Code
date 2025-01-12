# A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

# It is ().
# It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
# It can be written as (A), where A is a valid parentheses string.
# You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

# If locked[i] is '1', you cannot change s[i].
# But if locked[i] is '0', you can change s[i] to either '(' or ')'.
# Return true if you can make s a valid parentheses string. Otherwise, return false.
def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        ocount = 0
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                ocount += 1
            else:
                ocount -= 1
            if ocount < 0:
                return False
        ccount = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                ccount += 1
            else:
                ccount -= 1
            if ccount < 0:
                return False
        return True