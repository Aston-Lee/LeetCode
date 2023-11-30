class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dp(i):
            if i == 0 or i == 1:
                return 1
            return dp(i-1) + dp(i-2)
        
        return dp(n)
        