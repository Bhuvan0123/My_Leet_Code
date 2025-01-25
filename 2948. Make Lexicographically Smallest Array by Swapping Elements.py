# You are given a 0-indexed array of positive integers nums and a positive integer limit.

# In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

# Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

# An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.
def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n=len(nums)
        arr=sorted([(nums[i],i) for i in range(n)])
        graph=[]
        graph.append(arr[0])
        def func(graph):
            ind=[]
            ele=[]
            for e,i in graph:
                ele.append(e)
                ind.append(i)
            ind.sort()
            for i,e in zip(ind,ele):
                nums[i]=e
        for e,i in arr[1:]:
            if abs(graph[-1][0]-e)<=limit:
                graph.append((e,i))
            else:
                func(graph)
                graph=[(e,i)]
        func(graph)
        return nums