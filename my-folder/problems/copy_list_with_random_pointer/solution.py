"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # First duplicate the nodes
        n = head
        while n:
            n.next = Node(n.val, n.next)
            n = n.next.next

        # Mark the randoms
        n = head
        while n:
            if n.random:
                n.next.random = n.random.next
            n = n.next.next

        #separate the lists
        n = head
        sentinel = Node(0)
        copy = sentinel
        while n:
            copy.next = n.next
            n.next = n.next.next
            copy = copy.next
            n = n.next
        return sentinel.next