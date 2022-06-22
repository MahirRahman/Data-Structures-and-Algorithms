# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(0, head)
        count = 0
        while head:
            head = head.next
            count += 1
        head = dummyHead
        for i in range(count - n):
            head = head.next
        head.next = head.next.next
        return dummyHead.next
            
            
            