class MyQueue:

    def __init__(self):
        self.dq = []
        

    def push(self, x: int) -> None:
        self.dq.append(x)

    def pop(self) -> int:
        tmp = self.dq[0]
        self.dq = self.dq[1:]
        return tmp

    def peek(self) -> int:
        return self.dq[0]

    def empty(self) -> bool:
        return True if not self.dq else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()