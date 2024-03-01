class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [-1]*self.k
        self.addidx = 0
        self.removeidx = 0  
              

    def enQueue(self, value: int) -> bool:
        if self.queue[self.addidx % self.k] == -1:
            self.queue[self.addidx % self.k] = value
            self.addidx += 1
            return True
        return False
        

    def deQueue(self) -> bool:
        if self.queue[self.removeidx % self.k] != -1:
            self.queue[self.removeidx % self.k] = -1
            self.removeidx += 1
            return True
        return False
        

    def Front(self) -> int:
        return self.queue[self.removeidx % self.k]
        
    def Rear(self) -> int:
        return self.queue[(self.addidx - 1) % self.k] if self.addidx > 0 else -1

    def isEmpty(self) -> bool:
        return self.queue[self.removeidx % self.k] == -1

    def isFull(self) -> bool:
        return self.queue[self.addidx % self.k] != -1
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(self.k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
