class LinkNode:

    def __init__(self,val,next = None,prev = None):

        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = LinkNode(0)
        self.tail = LinkNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        

    def get(self, index: int) -> int:

        curr = self.head.next

        while curr and index > 0:
            curr = curr.next
            index-=1

        if curr and curr != self.tail and index == 0:
            return curr.val
        return -1
        

    def addAtHead(self, val: int) -> None:

        node = LinkNode(val = val)
        next = self.head.next
        prev = self.head

        node.next = next
        node.prev = prev

        next.prev = node
        prev.next = node


    def addAtTail(self, val: int) -> None:

        node = LinkNode(val)
        prev = self.tail.prev
        next = self.tail

        node.next = next
        node.prev = prev

        prev.next = node
        next.prev = node



    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next

        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0:
            node = LinkNode(val)

            prev = curr.prev
            next = curr

            prev.next = node
            node.prev = prev

            node.next = next
            next.prev = node

        
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next

        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0 and curr != self.tail:

            next = curr.next
            prev = curr.prev

            prev.next = next
            next.prev = prev

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)