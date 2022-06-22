# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode(0)  
        while l1 and l2:
            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                head = head.next
                l1 = l1.next 
            elif l2.val < l1.val:
                head.next = ListNode(l2.val)
                head = head.next
                l2 = l2.next
            else: 
                head.next = ListNode(l1.val)
                head.next.next = ListNode(l2.val) 
                l1 = l1.next
                l2 = l2.next
                head = head.next.next
        while l1:
            head.next = ListNode(l1.val)
            head = head.next
            l1 = l1.next
        while l2:
            head.next = ListNode(l2.val)
            head = head.next
            l2 = l2.next
        return dummy.next