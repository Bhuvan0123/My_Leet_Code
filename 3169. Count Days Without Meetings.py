# You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

# Return the count of days when the employee is available for work but no meetings are scheduled.

# Note: The meetings may overlap.
def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res=[]
        for i in meetings:
            if not res or i[0]>res[-1][1]:
                res.append(i)
            else:
                res[-1][1]=max(res[-1][1],i[1])
        count=0
        for s,e in res:
            count+=e-s+1
        return days-count