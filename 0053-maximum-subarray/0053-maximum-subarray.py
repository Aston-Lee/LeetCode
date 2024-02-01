class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        tmp, maxsum = nums[0], nums[0]
        for num in nums[1:]:
            
            if tmp < 0:
                tmp = 0
            tmp += num
            maxsum = max(maxsum, tmp)
        return maxsum if maxsum != -float('inf') else nums[0]
            