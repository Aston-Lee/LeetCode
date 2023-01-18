class MedianFinder:

    def __init__(self):
        self.minheap = [] ##store bigger element
        self.maxheap = [] ##store smaller element
        
    def addNum(self, num: int) -> None:
        if not self.minheap:
            self.minheap.append(num)
        elif num >= self.minheap[0]:
            if len(self.minheap) > len(self.maxheap):
                tmp = heapq.heappushpop(self.minheap, num)
                heapq.heappush(self.maxheap, -tmp)
            elif len(self.minheap) == len(self.maxheap):
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.minheap, num)
                
        elif num < self.minheap[0]:
            if len(self.minheap) > len(self.maxheap):
                heapq.heappush(self.maxheap, -num)
            elif len(self.minheap) == len(self.maxheap):
                tmp = heapq.heappushpop(self.minheap, num)
                heapq.heappush(self.maxheap, -tmp)
            else:
                tmp = heapq.heappushpop(self.maxheap, -num)
                heapq.heappush(self.minheap, -tmp)
        else:
            print("how3")
        
        # print("minheap", self.minheap)
        # print("maxheap", self.maxheap)
        # print("----")
        

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return float(self.minheap[0])
        elif len(self.minheap) < len(self.maxheap):
            return -float(self.maxheap[0])
        else:
            return (float(-self.maxheap[0]) + float(self.minheap[0]))/ 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()