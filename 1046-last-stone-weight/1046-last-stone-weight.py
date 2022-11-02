class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ## maxheap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while( len(stones)>=2 ):
            n1 = heapq.heappop(stones)
            n2 = heapq.heappop(stones)
            if n1!=n2:
                heapq.heappush(stones, n1-n2)
                heapq.heapify(stones)
                
        return -stones[0] if stones else 0