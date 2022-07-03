# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # pre = None
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.preOrderTraversal(root, float('-inf'), float('inf'))
    
    def preOrderTraversal(self, root, min, max):
        if root is None:
            return True
        if root.val >= max or root.val <= min:
            return False
        return self.preOrderTraversal(root.left, min, root.val) and self.preOrderTraversal(root.right, root.val, max)
        