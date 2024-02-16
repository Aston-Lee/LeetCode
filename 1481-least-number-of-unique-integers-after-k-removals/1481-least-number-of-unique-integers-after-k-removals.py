class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
#         arr = [4,3,1,1,3,3,2], k = 3
        
#         4: 1
#         2: 1
            
#         1: 2 
#         3: 3
            
#         1 1 2 3 
        
        freq = collections.Counter(arr)
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, val)
            
        while heap:
            curr = heapq.heappop(heap)
            if curr <= k:
                k -= curr
            else: # curr > k
                return len(heap) + 1
            
        return 0
            
        
                 
                
            