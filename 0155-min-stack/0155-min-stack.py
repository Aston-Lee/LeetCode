class MinStack:

    def __init__(self):
        self.stack = []
        self.minrecord = []
        self.smallest = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        # self.smallest = min(self.smallest, val)
        # self.minrecord.append(self.smallest)

    def pop(self) -> None:
        # self.minrecord.pop()
        # if self.minrecord:
        #     self.smallest = self.minrecord[-1]
        # else:
        #     self.smallest = 
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # return self.smallest
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()