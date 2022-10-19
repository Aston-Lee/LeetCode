class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        lowest = max(piles)
        while(l<=r):
            mid = (l+r) // 2
            curr_h = 0
            curr_h = sum( math.ceil(float(p)/float(mid)) for p in piles )
            if curr_h > h:
                l = mid + 1
            else:
                lowest = min(lowest, mid)
                r = mid - 1
                
        return lowest
                
        
        
            
        
        