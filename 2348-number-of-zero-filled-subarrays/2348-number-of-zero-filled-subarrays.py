class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
#         pos = []
#         for i, num in enumerate(nums):
#             if num == 0:
#                 pos.append(i)
                
#         if len(pos) == 0:
#             return 0
        
#         res = 0
#         gap = 0
        
#         while gap < len(pos):
            
#             for i in range(len(pos)-gap):
#                 if pos[i+gap] - pos[i] == gap:
#                     res += 1                 
#             gap += 1
        
#         return res 
        
        res = 0
        currLen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                currLen += 1
            else:
                print(i, currLen)
                if currLen != 0:
                    for p in range(currLen+1):
                        res += p 
                    currLen = 0
                    
        if currLen != 0:
            for p in range(currLen+1):
                res += p 
            currLen = 0

        return res