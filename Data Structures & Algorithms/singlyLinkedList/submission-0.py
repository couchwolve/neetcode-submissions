class Node:

    def __init__(self,val = -1,next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    
    def get(self, index: int) -> int:

        i = 0
        curr = self.head.next
        
        while curr :
            if i == index:
                return curr.val
            curr = curr.next
            i+=1

        return -1


    def insertHead(self, val: int) -> None:

        next_node = Node()
        next_node.val = val
        next_node.next = self.head.next

        self.head.next = next_node

        if not next_node.next:
            self.tail = next_node
        

    def insertTail(self, val: int) -> None:

        next_node = Node()
        next_node.val = val
        next_node.next = None

        
        self.tail.next = next_node
        self.tail = next_node
        

    def remove(self, index: int) -> bool:

        curr = self.head
        i = 0
        while curr and i < index:
            i += 1
            curr = curr.next
        
        if curr and curr.next:

            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

            return True

        return False

        


    def getValues(self) -> List[int]:

        ans = []
        curr = self.head.next

        while curr:

            ans.append(curr.val)
            curr = curr.next
        
        return ans
        
