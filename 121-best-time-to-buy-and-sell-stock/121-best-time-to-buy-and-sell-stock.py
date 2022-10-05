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

        # @2 pointer
        l, r = 0, 1
        maxP = 0
        while r<len(prices):
            if prices[l] < prices[r]:
                maxP = max( maxP, prices[r] - prices[l] )
            else:
                l = r
            r += 1 
        return maxP
                