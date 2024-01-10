class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-n for n in nums]
        heapq.heapify(nums)
        for _ in range(k):
            ans = heappop(nums)
        return -ans
        