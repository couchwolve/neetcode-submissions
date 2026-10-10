class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.length = 0


    def get(self, i: int) -> int:

        return self.arr[i]


    def set(self, i: int, n: int) -> None:

        self.arr[i] = n

    def pushback(self, n: int) -> None:

        if self.length  == self.capacity:
            self.resize()
        
        self.arr[self.length] = n
        self.length+=1


    def popback(self) -> int:

        temp = self.arr[self.length-1]
        self.length-=1
        return temp
 

    def resize(self) -> None:
        temp = [0] * (2 * self.capacity)

        for i in range(self.length):
            temp[i] = self.arr[i]
        
        self.arr = temp
        self.capacity = 2 * self.capacity


    def getSize(self) -> int:

        return self.length
        
    
    def getCapacity(self) -> int:

        return self.capacity
