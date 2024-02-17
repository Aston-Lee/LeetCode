class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        quota = []
        
        for i in range(len(heights)-1):
            
            toClimb = heights[i+1] - heights[i]
            
            if toClimb <= 0:
                continue
            
            heapq.heappush(quota, toClimb)
            # print(i, quota, bricks, ladders)
            
            if len(quota) <= ladders:
                continue
                
            climb = heapq.heappop(quota)
            
            bricks -= climb
            # print("bricks", bricks)
            if bricks < 0:
                return i
            
        return len(heights)-1
        
#         # @bfs dq MLE
#         dq = deque([(bricks, ladders)])
#         i = -1
#         while i<len(heights) and dq:
#             i += 1
#             if i == len(heights)-1:
#                 break
#             if heights[i+1] <= heights[i]:
#                 continue
#             else:
#                 for _ in range(len(dq)):
#                     bricks, ladders = dq.popleft()
#                     if bricks - (heights[i+1] - heights[i]) >= 0:
#                         dq.append( (bricks - (heights[i+1] - heights[i]), ladders ))
#                     if ladders-1 >= 0:
#                         dq.append( (bricks, ladders-1 ))
        
#         return i


#         # @bfs tuple set MLE
#         pairSet = set()
#         pairSet.add(tuple((bricks, ladders)))
#         i = -1
#         while i<len(heights) and pairSet:
#             i += 1
#             if i == len(heights)-1:
#                 break
#             if heights[i+1] <= heights[i]:
#                 continue
#             else:
#                 dq = deque(pairSet)
#                 tmp = set()
#                 for _ in range(len(dq)):
#                     bricks, ladders = dq.popleft()
#                     if bricks - (heights[i+1] - heights[i]) >= 0:
#                         tmp.add( tuple((bricks - (heights[i+1] - heights[i]), ladders )))
#                     if ladders-1 >= 0:
#                         tmp.add( tuple((bricks, ladders-1 )))
#                 pairSet = tmp
        
#         return i
            
        
        
        
        
        
        
        