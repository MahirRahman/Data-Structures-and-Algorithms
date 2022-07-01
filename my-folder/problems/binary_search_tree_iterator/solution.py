# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.res = self.helper(root)
        self.pointer = -1
        
    def helper(self, root):
        res = []
        stk = []
        node = root
        while node or stk:
            pre = None
            while node:
                stk.append(node)
                node = node.left
            node = stk.pop()
            res.append(node)
            node = node.right
        return res

    def next(self) -> int:
        self.pointer += 1
        return self.res[self.pointer].val

    def hasNext(self) -> bool:
        if self.pointer + 1 >= len(self.res):
            return False
        return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()