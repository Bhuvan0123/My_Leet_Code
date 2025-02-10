# You are given a string s.

# Your task is to remove all digits by doing this operation repeatedly:

# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.
def clearDigits(self, s: str) -> str:
        st=[]
        for i in range(len(s)):
            if s[i].isnumeric():
                st.pop(-1)
                continue
            else:
                st.append(s[i])
        return "".join(st)