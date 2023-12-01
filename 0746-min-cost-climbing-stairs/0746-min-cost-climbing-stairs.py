class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
#         [10, 15, 20, float('inf')]
#         dp(3) = min(dp(1)+cost[1], dp(2)+cost[2])
#         dp(1) return 0
    
#         dp(2) = min(dp(0)+cost[0], dp(1)+cost[1]) 
#         dp(0) return 0
    
    
        n = len(cost)
        
        @cache
        def dp(i):
            if i == 0 or i == 1:
                return 0
            return min(dp(i-2)+cost[i-2], dp(i-1)+cost[i-1])
        
        return dp(n)