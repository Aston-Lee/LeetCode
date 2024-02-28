class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        heap = []
        
        for num in arr:
            if len(heap) < k:
                heapq.heappush(heap, [-abs(num-x), -num])
            else:
                heapq.heappushpop(heap, [-abs(num-x), -num])
                
        # print(heap)
        
        res = []
        for _, num in heap:
            res.append(-num)

        return sorted(res)