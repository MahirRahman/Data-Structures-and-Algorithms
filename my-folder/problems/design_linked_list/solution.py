class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class MyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        head = self.head
        if head is None:
            return -1
        for _ in range(index):
            head = head.next
        return head.val

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        head = self.head
        if not head:
            self.head = Node(val)
        else:
            while head.next:
                head = head.next
            head.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return None
        head = self.head
        if index == 0:
            self.head = Node(val, self.head)
        else:
            for _ in range(index - 1):
                head = head.next
            head.next = Node(val, head.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None
        head = self.head
        if head:
            if index == 0:
                self.head = head.next
            else:
                for _ in range(index - 1):
                        head = head.next
                head.next = head.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)