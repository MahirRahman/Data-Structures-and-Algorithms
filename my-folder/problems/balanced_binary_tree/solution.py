# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self._isBalanced(root) != -1

    def _isBalanced(self, root):
        if root is None:
            return 0
        l = self._isBalanced(root.left)
        if l == -1:
            return -1
        r = self._isBalanced(root.right)
        if r == -1:
            return -1
        if abs(l - r) > 1:
            return -1
        return 1 + max(l, r)