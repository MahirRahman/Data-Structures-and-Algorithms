# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.left or root.right:
            temp = root.left
            root.left = root.right
            root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
        
        
    # def insertNode(self, node, new_val):
    #     if node is None:
    #         return
    #     if node.val >= new_val:
    #         if node.left:
    #             self.insertNode(node.left, new_val)
    #         else:
    #             node.left = TreeNode(new_val)
    #     else:
    #         if node.right:
    #             self.insertNode(node.right, new_val)
    #         else:
    #             node.right = TreeNode(new_val)    
        