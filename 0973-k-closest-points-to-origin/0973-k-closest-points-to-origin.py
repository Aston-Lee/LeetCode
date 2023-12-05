import heapq

class Solution:
    def kClosest(self, points, k):
        minheap = []
        for point in points:
            length = point[0]**2 + point[1]**2
            if len(minheap) < k:
                heapq.heappush(minheap, (-length, point))
            elif length < -minheap[0][0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap, (-length, point))

        return [heapq.heappop(minheap)[1] for _ in range(k)]