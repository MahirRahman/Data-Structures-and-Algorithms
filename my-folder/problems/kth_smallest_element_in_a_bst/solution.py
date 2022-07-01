# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        node = root
        i = 1
        while node or s:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            # print(node.val)
            if k == i:
                return node.val
            i += 1
            node = node.right
            