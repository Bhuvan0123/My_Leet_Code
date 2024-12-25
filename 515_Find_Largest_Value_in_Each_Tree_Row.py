'''
Given the root of a binary tree, return an array of the largest value in 
each row of the tree (0-indexed).
'''
def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(root,level):
            if(root):
                val=root.val
                if(len(res)==level):
                    res.append(val)
                else:
                    res[level]=max(res[level],val)
                dfs(root.left,level+1)
                dfs(root.right,level+1)
        dfs(root,0)
        return res