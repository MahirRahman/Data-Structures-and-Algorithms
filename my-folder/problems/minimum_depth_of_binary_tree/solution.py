# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
    def helper(self, root, depth):
        if root is None:
            return depth
        depth += 1
        if not root.left:
            return self.helper(root.right, depth)
        elif not root.right:
            return self.helper(root.left, depth)
        else:
            return min(self.helper(root.left, depth), self.helper(root.right, depth))