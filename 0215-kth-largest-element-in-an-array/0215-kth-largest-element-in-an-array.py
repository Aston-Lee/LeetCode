class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-n for n in nums]
        heapq.heapify(nums)
        
        res = 0
        while(k>0):
            res = heappop(nums)
            k-=1
            
        return -res