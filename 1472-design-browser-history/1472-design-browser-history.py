class BrowserHistory:

    def __init__(self, homepage: str):
        self.queue = [homepage]
        self.pointer = 0
        self.maxpointer = 0

    def visit(self, url: str) -> None:
        if self.pointer == self.maxpointer:
            self.pointer += 1
            if len(self.queue) == self.pointer:
                self.queue.append(url)
            else:
                self.queue[self.pointer] = url
        else:
            self.pointer += 1
            self.queue[self.pointer] = url
        
        self.maxpointer = self.pointer
        # print(self.pointer, self.maxpointer)
        # return self.queue[self.pointer]
        return url
        
    
    def back(self, steps: int) -> str:
        self.pointer -= steps
        if self.pointer < 0:
            self.pointer = 0
        # print("back", steps, "to", self.pointer, "curr max:", self.maxpointer)
        return self.queue[self.pointer]
        

    def forward(self, steps: int) -> str:
        self.pointer += steps
        if self.pointer > self.maxpointer:
            self.pointer = self.maxpointer
        # print("forward", steps, "to", self.pointer,"curr max", self.maxpointer)
        return self.queue[self.pointer]
    

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)