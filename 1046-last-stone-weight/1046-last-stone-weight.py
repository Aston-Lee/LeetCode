class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ## smallest or largest -> minheap maxheap
        
        ## maxheap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while( len(stones)>1 ):
            ## regular pop will fail since it does not pop the smalleset 
            n1 = heapq.heappop(stones) 
            ## heappop pop the smallest
            n2 = heapq.heappop(stones)
            if n1!=n2:
                heapq.heappush(stones, n1-n2)
                
        return -stones[0] if stones else 0
