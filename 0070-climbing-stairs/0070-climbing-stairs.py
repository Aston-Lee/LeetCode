class Solution:
    def climbStairs(self, n: int) -> int:
        
        # @cache
        mem = {}
        def dp(i):
            if i == 0 or i == 1:
                return 1
            if i in mem:
                return mem[i]
            ans = dp(i-1) + dp(i-2)
            mem[i] = ans
            return ans
        
        return dp(n)
        