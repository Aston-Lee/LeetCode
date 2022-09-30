class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        # dp bottom
        mem = [0]*len(cost)
        mem[0] = cost[0]
        if len(cost) > 1:
            mem[1] = cost[1]
        

        for i in range(2, len(cost)):
            mem[i] = min(mem[i-1], mem[i-2]) + cost[i]
        
        return min(mem[-1], mem[-2])