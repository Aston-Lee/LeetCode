class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        
        if len(self.minheap) == len(self.maxheap):
            if len(self.minheap) == 0:
                heapq.heappush(self.minheap, num)
            elif num > self.minheap[0]:
                heapq.heappush(self.minheap, num)
            else: ## num <= minheap[0]
                heapq.heappush(self.maxheap, -num)
        
        elif len(self.minheap) > len(self.maxheap):
            if self.minheap[0] < num:
                tmp = heapq.heappushpop(self.minheap, num)
                heapq.heappush(self.maxheap, -tmp)
            else:
                heapq.heappush(self.maxheap, -num)
        
        else: ## len(minheap) < len(maxheap)
            if num > self.minheap[0]:
                heapq.heappush(self.minheap, num)
            else:
                tmp = heapq.heappushpop(self.maxheap, -num)
                heapq.heappush(self.minheap, -tmp)
                
        
    
    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + -self.maxheap[0]) / 2
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return -self.maxheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# minheap  1 2 3 4
# maxheap  1 2 3

# 1234 -1 -2 -3  -5

# -1 -2 -3 1 2 3 4
