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
        return self.inOrderTraversal(root, None)[0]
    
    def inOrderTraversal(self, root, prev):
        if root is None:
            return True, prev
        l, prev = self.inOrderTraversal(root.left, prev)
        if prev and prev.val >= root.val:
            return False, prev
        prev = root
        r, prev = self.inOrderTraversal(root.right, prev)
        return l and r, prev
        
        