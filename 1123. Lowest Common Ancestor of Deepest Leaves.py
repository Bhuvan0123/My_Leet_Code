# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

# Recall that:

# The node of a binary tree is a leaf if and only if it has no children
# The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
# The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node,depth):
            if not node:
                return (None,depth)
            left,ld=dfs(node.left,depth+1)
            right,rd=dfs(node.right,depth+1)
            if ld>rd:
                return (left,ld)
            elif rd>ld:
                return (right,rd)
            else:
                return (node,ld)
        node,a=dfs(root,0)
        return node