class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # [2,7,9,3,1]
        # [2,7,11,10,12]
        
        n = len(nums)   
        if n < 3:
            return max(nums)
        elif n == 3:
            nums[2] += nums[0] 
            return max(nums)
        
        dp = [0]*n
        
        for i in range(n):
            if i == 0 or i == 1:
                dp[i] = nums[i]
                
            elif i == 2:
                dp[i] = dp[0] + nums[2]
            
            else:
                dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
                
        return max(dp)
