class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0] * (n+1)
        base = 1
        
        for i in range(1, n+1):
            if base * 2 == i:
                base = i
            dp[i] = 1 + dp[ i-base ]
            
        return dp