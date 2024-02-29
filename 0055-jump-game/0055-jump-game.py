class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        farthest = 0
        
        for i, num in enumerate(nums):
            if farthest >= i:
                farthest = max(farthest, nums[i]+i)  
                
        return farthest >= len(nums)-1                
        
        