class Solution:
    def rob(self, nums: List[int]) -> int:
        
#         0123
#         dp3 = max(dp1, dp0) + nums[3]
        
#         01234
#         dp4 = max(dp2, dp1) + nums[4]
#         dp3 = max(dp1, dp0) + nums[3]
        
        n = len(nums)
        if n < 3:
            return max(nums[:n])
    
        dp = [0]*len(nums)
        
        for i in range(len(nums)):
            if i == 0 or i == 1:
                dp[i] = nums[i]
            elif i == 2:
                dp[i] = dp[i-2] + nums[i]
            else:
                dp[i] = max(dp[i-3], dp[i-2]) + nums[i]
                
        return max(dp[-1], dp[-2])