class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # n^2 will TLE
        # try nlogn
        # try using heap
        
        
        # intervals [[1,4],[2,4],[3,6],[4,4]]
        # queries [2,3,4,5]
        # minHeap [(3,4), (4,4), (4,6)]
        # i 3
        
#         intervals.sort()
#         minHeap = []
#         res = {}
#         i = 0
        
#         for q in sorted(queries):
#             while i<len(queries) and intervals[i][0] <= q:
#                 l, r = intervals[i][0], intervals[i][1]
#                 heapq.heappush(minHeap, (r-l+1, r))
#                 i+=1
            
#             while minHeap and minHeap[0][1] < q:
#                 heapq.heappop(minHeap)
#             res[q] = minHeap[0][0] if minHeap else -1
#         return [res[q] for q in queries]
    
    
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
        