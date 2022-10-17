
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        MinHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            MinHeap.append([dist, x, y])
        
        heapq.heapify(MinHeap)
        
        res = []
        while k>0:
            d, x, y = heapq.heappop(MinHeap)
            res.append([x,y])
            k-=1
        
        return res
        