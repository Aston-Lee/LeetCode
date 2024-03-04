class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
#         k = 2
#         minheap 5 6 ok
        
#         k = 4 
#         minheap 4 5 5 6 ok
        
        heap = []
        for num in nums:
            if len(heap) == k:
                heapq.heappushpop(heap, num)
            else:
                heapq.heappush(heap, num)
        return heapq.heappop(heap)
            