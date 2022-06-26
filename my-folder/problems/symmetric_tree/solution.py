# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, lnode, rnode):
        if lnode is None and rnode is None:
            return True
        if lnode is None or rnode is None or lnode.val != rnode.val:
            return False
        return self._isSymmetric(lnode.left, rnode.right) and self._isSymmetric(lnode.right, rnode.left)
                    