# You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

# (startx, starty): The bottom-left corner of the rectangle.
# (endx, endy): The top-right corner of the rectangle.
# Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

# Each of the three resulting sections formed by the cuts contains at least one rectangle.
# Every rectangle belongs to exactly one section.
# Return true if such cuts can be made; otherwise, return false.
def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def func(arr):
            arr.sort()
            res=0
            maxi=arr[0][1]
            for s,e in arr:
                if maxi<=s:
                    res+=1
                maxi=max(maxi,e)
            return res>=2
        xi=[[i[0],i[2]] for i in rectangles]
        yi=[[i[1],i[3]] for i in rectangles]
        return func(xi) or func(yi)