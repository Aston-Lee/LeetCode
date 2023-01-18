class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if not self.minheap or num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
            
        if len(self.minheap) > len(self.maxheap) + 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        elif len(self.maxheap) > len(self.minheap):
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

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