# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pred = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = pred
            pred = curr
        n = head
        while pred:
            if (n.val != pred.val):
                return False
            n = n.next
            pred = pred.next
        return True