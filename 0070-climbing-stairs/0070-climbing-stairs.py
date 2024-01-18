class Solution:
    def climbStairs(self, n: int) -> int:
        
#         dp(2) = dp(1) + dp(0)
        
#         dp(3) = dp(2) + dp(1)
        
#         dp(0) = 1
#         dp(1) = 1
#         dp(2) = 2
        
        @cache
        def dp(n):
            if n == 0 or n == 1:
                return 1
            else:
                return dp(n-1) + dp(n-2)
            
        return dp(n)