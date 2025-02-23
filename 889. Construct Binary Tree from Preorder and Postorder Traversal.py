# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

# If there exist multiple answers, you can return any of them.
def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def func():
            node=TreeNode(postorder.pop())
            if node.val!=preorder[-1]:
                node.right=func()
            if node.val!=preorder[-1]:
                node.left=func()
            preorder.pop()
            return node
        return func()