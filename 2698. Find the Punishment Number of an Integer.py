# Given a positive integer n, return the punishment number of n.

# The punishment number of n is defined as the sum of the squares of all integers i such that:

# 1 <= i <= n
# The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.
def punishmentNumber(self, n: int) -> int:
        def func(k,tar):
            if k==tar:
                return True
            if k==0:
                return tar==0
            for i in (10,100,1000):
                if func(k//i,tar-(k%i)):
                    return True
            return False
        res=0
        for i in range(1,n+1):
            if func(i*i,i):
                res+=i*i
        return res