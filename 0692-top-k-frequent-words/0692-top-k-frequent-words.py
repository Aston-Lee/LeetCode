class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = collections.Counter(words)
        heap = []
        
        for key, val in freq.items():
            heapq.heappush(heap, (-val, key))
          
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res
        
        # for key, val in freq.items():
            
            