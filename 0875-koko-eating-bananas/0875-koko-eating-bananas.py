class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        l, r = 1 ,max(piles)
        minK = float('inf')
        while l<=r:
            amount = (l+r)//2
            currh = 0
            for p in piles:
                currh += math.ceil(p/amount)
            
            if currh > h:
                l = amount+1
            else:
                minK = min(minK, amount)
                r = amount-1
                
        return minK