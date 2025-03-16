# You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

# You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

# Return the minimum time taken to repair all the cars.

# Note: All the mechanics can repair the cars simultaneously.
def repairCars(self, ranks: List[int], cars: int) -> int:
        def func(mid):
            res=0
            for i in ranks:
                res+=int((mid//i)**0.5)
                if res>=cars:
                    return True
            return False
        left=1
        right=min(ranks)*cars*cars
        while left<right:
            mid=(left+right)//2
            if func(mid):
                right=mid
            else:
                left=mid+1
        return left