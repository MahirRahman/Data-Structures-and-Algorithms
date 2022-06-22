# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy = pred = ListNode(0, curr)
        while curr and curr.next:
            pred.next = curr.next
            curr.next = curr.next.next
            pred.next.next = curr
            pred, curr = curr, curr.next
        return dummy.next