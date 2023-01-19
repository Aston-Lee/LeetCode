class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0]*(len(nums)+1)
        
        for i in range(len(nums)+1):
            if i<3:
                dp[i] = nums[i-1]
            elif i == 3:
                dp[i] = max(dp[1] + nums[2], dp[2])
            else:
                dp[i] = max(dp[i-2], dp[i-3]) + nums[i-1]
        
        return max(dp[-1], dp[-2])