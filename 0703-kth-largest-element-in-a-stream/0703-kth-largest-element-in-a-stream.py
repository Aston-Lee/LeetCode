class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = []
        for n in self.nums:
            if len(self.heap) == k:
                heapq.heappushpop(self.heap, n)    
            else:
                heapq.heappush(self.heap, n)
        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k: 
            heapq.heappush(self.heap, val)
        elif self.heap and val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
    

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)