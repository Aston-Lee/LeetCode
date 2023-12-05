class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ## minheap: heapq.heapify
        ## Time: O(N) Space: O(N)
        minheap = []
        
        
        for point in points:
            length = point[0]**2 + point[1]**2
            minheap.append((length, (point)))
            
        heapq.heapify(minheap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        
        return res
        
        
        ## followup: try the pushpop, maintaining k size array 

        