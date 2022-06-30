# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        maxArray = []
        while queue:
            size = len(queue)
            max = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val > max:
                    max = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            maxArray.append(max)
        return maxArray