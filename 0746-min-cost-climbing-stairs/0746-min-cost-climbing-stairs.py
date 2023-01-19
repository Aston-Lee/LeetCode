class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        dp = [0]*(len(cost)+1)
        
        for i in range(1,len(cost)+1):
            if i <= 2:
                dp[i] = min(dp[i-2]+cost[i-1], dp[i-1]+cost[i-1])
            else:
                dp[i] = min(dp[i-2]+cost[i-1], dp[i-1]+cost[i-1])
        
        return min(dp[-1], dp[-2])