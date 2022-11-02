class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nk = len(nums) - k +1
        
        heapq.heapify(nums)
        
        while(nk):
            res = heapq.heappop(nums)
            nk -= 1
        
        return res