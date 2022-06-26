# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self._pruneTree(root)
        if root.left is None and root.right is None:
            if root.val == 0:
                return None
        return root
    
    def _pruneTree(self, root):
        if not root:
            return False
        if self._pruneTree(root.left):
            root.left = None
        if self._pruneTree(root.right):
            root.right = None
        if not root.left and not root.right:
            if root.val == 0:
                return True
        return False