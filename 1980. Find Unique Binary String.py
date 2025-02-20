# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.
def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        res='0'*n
        if res not in nums:
            return res
        res=list(res)
        for i in range(n):
            res[i]='1'
            if "".join(res) not in nums:
                return "".join(res)
            res[i]='0'
        return "".join(res)