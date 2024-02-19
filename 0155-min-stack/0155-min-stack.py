class MinStack:

    def __init__(self):
        self.stack = []
        self.minrecord = []
        self.smallest = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.smallest = min(self.smallest, val)
        self.minrecord.append(self.smallest)
        # print(val, self.smallest, self.minrecord)

    def pop(self) -> None:
        self.minrecord.pop()
        if self.minrecord:
            self.smallest = self.minrecord[-1]
        else:
            self.smallest = float('inf')  # Reset smallest when stack is empty
        return self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()