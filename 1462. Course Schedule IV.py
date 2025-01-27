# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

# Return a boolean array answer, where answer[j] is the answer to the jth query.
def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        dp = [0] * numCourses
        for p in prerequisites:
            adj[p[0]].append(p[1])
            dp[p[1]] += 1
        queue = deque()
        for i in range(numCourses):
            if dp[i] == 0:
                queue.append(i)
        mp = defaultdict(set)
        while queue:
            curr = queue.popleft()
            for next_course in adj[curr]:
                mp[next_course].add(curr)
                mp[next_course].update(mp[curr])
                dp[next_course] -= 1
                if dp[next_course] == 0:
                    queue.append(next_course)
        
        return [q[0] in mp[q[1]] for q in queries]