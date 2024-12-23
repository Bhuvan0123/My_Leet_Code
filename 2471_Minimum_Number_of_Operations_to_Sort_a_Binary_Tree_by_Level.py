'''
You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each 
level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.
'''
def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def func(arr):
            n = len(arr)
            index = [(val, i) for i, val in enumerate(arr)]
            index.sort()
            visited = [False] * n
            swaps = 0

            for i in range(n):
                if visited[i] or index[i][1] == i:
                    continue

                cycle_size = 0
                x = i

                while not visited[x]:
                    visited[x] = True
                    x = index[x][1]
                    cycle_size += 1

                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps

        queue = deque([root])
        res = 0

        while queue:
            level = len(queue)
            curr = []

            for _ in range(level):
                node = queue.popleft()
                curr.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res += func(curr)

        return res