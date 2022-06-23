# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = pred = ListNode(0, head)
        while head:
            if head.val == val:
                pred.next = head.next
            else:
                pred = head
            head = head.next
        return dummyHead.next