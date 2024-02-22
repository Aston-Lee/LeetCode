class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        @cache
        def dp(i):
            if i <= -1:
                return 0
            elif i == 0 or i == 1:
                return nums[i]
            return max(dp(i-2), dp(i-3)) + nums[i]
        
        return max(dp(len(nums)-1), dp(len(nums)-2))
            
            
            
                
        
            