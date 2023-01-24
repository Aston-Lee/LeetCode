class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        maxheap = []
        
        ## brute heap 
        n = len(matrix)
        for lst in matrix:
            for num in lst:
                if len(maxheap) < k:
                    heapq.heappush(maxheap, -num)
                else:
                    heapq.heappushpop(maxheap, -num)
                # print(maxheap)
        return -maxheap[0]
                    
        