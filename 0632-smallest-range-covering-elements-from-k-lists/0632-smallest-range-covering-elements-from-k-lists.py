class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        minx, miny = 0, float('inf')
        max_val = float('-inf')
        nextListPos = [0] * len(nums)
        flag = True
        
        min_heap = []
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i))
            max_val = max(max_val, nums[i][0])
        
        while flag:
            min_val, whichList = heapq.heappop(min_heap)
            
            if miny - minx > max_val - min_val:
                minx, miny = min_val, max_val
            
            # print(nextListPos)
            nextListPos[whichList] += 1
            # print(nextListPos)
            if nextListPos[whichList] == len(nums[whichList]):
                flag = False
                break
            
            # print(nums[whichList][nextListPos[whichList]], whichList)
            heapq.heappush(min_heap, (nums[whichList][nextListPos[whichList]], whichList))
            max_val = max(max_val, nums[whichList][nextListPos[whichList]])
        return [minx, miny]
        
        
        
#         k = len(nums)
#         currCoveringDiff = float('inf')
#         currCovering = []
        
#         pointer = defaultdict(int)
#         for i in range(k): 
#             pointer[i] = 0 #position in each list 
            
#         postdict = defaultdict(int)
#         while True:
#             smallest = float('inf')
#             smallest_list_pos = None
#             for i in range(k):
#                 if nums[i][pointer[i]] <= smallest:
#                     smallest_list_pos.append(i)
#                     smallest.append(nums[i][pointer[i]])

#             if len(smallest_list_pos) == k:
#                 return [nums[smallest_list_pos][pointer[smallest_list_pos]], nums[smallest_list_pos][pointer[smallest_list_pos]]]
            
#             #update the correalted value
#             for j in smallest_list_pos:
#                 pointer[j] += 1
#                 seen.add(j)
#                 currMax = max(currMax, nums[j][pointer[j]])
#                 currMin = min(currMin, nums[j][pointer[j]])
                
#             if len(seen) == k and currMax-currMin < currCoveringDiff :
#                 currCovering = [currMin, currMax]
#                 currCoveringDiff = currMin - currMax
                