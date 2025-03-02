# You are given two 2D integer arrays nums1 and nums2.

# nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# Each array contains unique ids and is sorted in ascending order by id.

# Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

# Only ids that appear in at least one of the two arrays should be included in the resulting array.
# Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
# Return the resulting array. The returned array must be sorted in ascending order by id.
def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i,j=0,0
        res=[]
        n1,n2=len(nums1),len(nums2)
        while i<n1 and j<n2:
            i1,v1=nums1[i]
            i2,v2=nums2[j]
            if i1<i2:
                res.append([i1,v1])
                i+=1
            elif i2<i1:
                res.append([i2,v2])
                j+=1
            else:
                res.append([i1,v1+v2])
                i+=1
                j+=1
        while i<n1:
            res.append(nums1[i])
            i+=1
        while j<n2:
            res.append(nums2[j])
            j+=1
        return res