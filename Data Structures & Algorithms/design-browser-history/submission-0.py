class LinkNode:

    def __init__(self,val):
        self.next = None
        self.prev = None
        self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = LinkNode(homepage)
        self.tail = self.head

        self.curr = self.head
        

    def visit(self, url: str) -> None:

        node = LinkNode(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = node
        self.tail = node
        

    def back(self, steps: int) -> str:
        
        while steps >= 1 and self.curr.prev:
            self.curr = self.curr.prev
            steps-=1
        
        return self.curr.val

        

    def forward(self, steps: int) -> str:
        
        while steps >= 1 and self.curr.next:
            print(steps)
            self.curr = self.curr.next
            steps-=1
        
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)