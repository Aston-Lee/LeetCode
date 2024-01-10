class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        use heap find max  ->  minheap
        '''
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]