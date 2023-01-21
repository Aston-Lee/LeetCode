class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        seen = set()
        minheap = [(0,0)] #(pathcost, node to connect) -> node is a index of point
        
        cost = 0
        
        while minheap:
            if len(seen) == len(points):
                return cost
            
            pathcost, newnode = heapq.heappop(minheap) 
            if newnode in seen:
                continue
            cost += pathcost
            seen.add(newnode)
            for i in range(len(points)):
                if i not in seen:
                    tmpcost = abs( points[i][0] - points[newnode][0]) + abs( points[i][1] - points[newnode][1])
                    heapq.heappush(minheap, ( tmpcost,i) )
                    
        return cost
                    
                    
#         seen: 0, 1, 3 ,4, 2
#         minheap: [(13,2), (10,2), (14,2) ]
#         cost: 0 + 4 + 3 + 4 + 9
            
#             (9,2),