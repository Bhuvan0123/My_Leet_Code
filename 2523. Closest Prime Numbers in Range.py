# Given two positive integers left and right, find the two integers num1 and num2 such that:

# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].
def closestPrimes(self, left: int, right: int) -> List[int]:
        isprime=[True]*(right+1)
        isprime[0]=isprime[1]=False
        for i in range(2,int(right**0.5)+1):
            if isprime[i]:
                for j in range(i*i,right+1,i):
                    isprime[j]=False
        prime=[]
        for i in range(left,right+1):
            if isprime[i]:
                prime.append(i)
        mini=float('inf')
        res=[-1,-1]
        for i in range(1,len(prime)):
            temp=prime[i]-prime[i-1]
            if temp<mini:
                mini=temp
                res=[prime[i-1],prime[i]]
        return res