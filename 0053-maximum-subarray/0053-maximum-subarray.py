class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        counter = 0
        maximum = -float('inf')
        while(r!=len(nums)):
            counter += nums[r]
            maximum = max(counter, maximum)
            r += 1
            if counter < 0:
                counter = 0
            
        return maximum