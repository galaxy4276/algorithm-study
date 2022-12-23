class CircularQueue:

    def __init__(self, k: int):
        self.data = [0 for _ in range(k + 1)]
        self.MAX_SIZE = k + 1
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.data[self.rear] = value
            self.rear = (self.rear + 1) % self.MAX_SIZE
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.data[self.front] = 0
            self.front = (self.front + 1) % self.MAX_SIZE
            return True
        return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.rear + self.MAX_SIZE - 1) % self.MAX_SIZE]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1) % self.MAX_SIZE == self.front

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()