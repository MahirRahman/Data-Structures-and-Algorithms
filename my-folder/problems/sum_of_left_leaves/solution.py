# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.lsum(root, False)
    
    def lsum(self, root, lnode):
        if not root:
            return 0
        if not root.left and not root.right:
                return root.val if lnode else 0
        return self.lsum(root.left, True) + self.lsum(root.right, False)
        
        