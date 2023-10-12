class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        currmin, currmax = prices[0], prices[0]
        maxprofit = 0
        for p in prices:
            if p < currmin:
                maxprofit = max(maxprofit, currmax-currmin)
                currmin, currmax = p, p
            else:
                currmax = max(currmax, p)
        maxprofit = max(maxprofit, currmax-currmin)
        return maxprofit
        
        
        
            
            
            
            
        
        
        
        
        
        
        
        
                