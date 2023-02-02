class Solution:
    def numSquares(self, n: int) -> int:
        
        # base 1 2 3 4 
        
        square = [i**2 for i in range(int(math.sqrt(n))+1)]
        
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(n+1):
            for num in square:
                if i < num:
                    break
                dp[i] = min(dp[i], dp[i-num]+1)
        
        return dp[n]
        
        
        