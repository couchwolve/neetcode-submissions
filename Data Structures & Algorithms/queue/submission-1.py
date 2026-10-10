class Node:

    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):

        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:

        if self.head.next == self.tail:
            return True
        return False
        

    def append(self, value: int) -> None:
        node = Node(value)
        next = self.tail
        prev = self.tail.prev

        node.next = next
        node.prev = prev
        node.prev.next = node

        self.tail.prev = node
        

    def appendleft(self, value: int) -> None:
        node = Node(value)
        next = self.head.next
        prev = self.head

        node.next = next
        node.prev = prev
        node.next.prev = node

        self.head.next = node


    def pop(self) -> int:

        if self.isEmpty():
            return -1
        
        value = self.tail.prev
        self.tail.prev = value.prev
        value.prev.next = self.tail
        return value.val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        value = self.head.next

        self.head.next = value.next
        value.next.prev = self.head

        return value.val
        
