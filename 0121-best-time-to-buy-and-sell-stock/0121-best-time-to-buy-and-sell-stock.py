class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # @leftmost rightmost -> is used for rain, not day trade
        
#         # two pointer?
#         least = 1000000  # by not using max() its so much faster 
#         value = 0
#         maxvalue =0
        
#         for i in prices:
#             if least > i:
#                 least = i
#                 value = 0
#             else:
#                 value = i - least
#                 if maxvalue < value:
#                     maxvalue = value
                    
#         return maxvalue

        # # @2 pointer Time:O(n) Space:O(1)
        # l, r = 0, 1
        # maxP = 0
        # while r<len(prices):
        #     if prices[l] < prices[r]:
        #         maxP = max( maxP, prices[r] - prices[l] )
        #     else:
        #         l = r
        #     r += 1 
        # return maxP
        
        currmin, currmax = float('inf'), -float('inf')
        maxprofit = 0
        for p in prices:
            if p < currmin and currmin != float('inf'):
                if currmax != -float('inf'):
                    maxprofit = max(maxprofit, currmax - currmin)
                currmin = p
                currmax = -float('inf')
            else:
                currmin = min(currmin, p)
                currmax = max(currmax, p)
        
        maxprofit = max(maxprofit, currmax - currmin)
        return maxprofit
            
            
            
            
            
        
        
        
        
        
        
        
        
                