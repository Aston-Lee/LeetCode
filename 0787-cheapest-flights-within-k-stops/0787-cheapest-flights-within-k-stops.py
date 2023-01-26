class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ## bellman ford - shortest path
        prices = [float('inf')] * n
        prices[src] = 0
        
        for i in range(k+1):
            tmpPrices = prices.copy()
            
            for s, d, p in flights:
                if prices[s] == float(inf):
                    continue
                tmpPrices[d] = min(prices[s]+p, tmpPrices[d])
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]