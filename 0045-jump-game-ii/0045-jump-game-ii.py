class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l, r = 0, 0 
        maxJump = 0
        
        while maxJump < len(nums)-1:
            for i in range(l, r+1):
                maxJump = max(maxJump, i+nums[i])
            r = maxJump
            l += 1
        
        return l
            
            
        
         