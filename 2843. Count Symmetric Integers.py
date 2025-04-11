# You are given two positive integers low and high.

# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

# Return the number of symmetric integers in the range [low, high].
def countSymmetricIntegers(self, low: int, high: int) -> int:
        def issymetric(x):
            n=len(str(x))
            if n%2==1:
                return 0
            temp=list(map(int,list(str(x))))
            return sum(temp[:n//2])==sum(temp[n//2:])
        res=0
        for i in range(low,high+1):
            if issymetric(i):
                res+=1
        return res