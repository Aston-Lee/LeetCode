class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        '''
        10^5
        
        [1,4,6,8,10]
         i
         
         i = 0, tmp = 24
         base = 0 + 3 + 5 + 7 + 9 = 24
         leftelement = 0
         rightelement = 5
         
         i = 1
         diff 4-1 = 3
         leftelement = 0+1 = 1
         rightelement = 5-1 = 4
         new = 3 + 0 + 2 + 4 + 6 = 15(24+1*3-4*3)
         
         i = 2 
         diff = 6-4 = 2
         leftelement = 1+1=2
         rightelement = 4-1 =3
         new = 5 + 2 + 0 + 2 + 4 = 13(15+2*2-3*2)
         
         i=3 diff=2
         left = 3
         right = 2 
         new = 13+3*2-2*2 = 15
         
         i=4 diff=2
        
        sorted
        
        
        '''
        
        base = 0
        res = []
        for num in nums:
            base += abs(nums[0] - num)
        res.append(base)
        left = 0
        right = len(nums)
        
        
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            left += 1
            right -= 1
            base = base+left*diff-right*diff
            res.append(base)
                     
        return res
                       
        
        
        
        
#         # brute force  TLE
#         res = []
#         resdict = {}
#         for num in nums:
#             if num not in resdict:
#                 tmp = 0
#                 for i in range(len(nums)):
#                     tmp +=  abs(num - nums[i])
#                 res.append(tmp)
#             else:
#                 res.append(resdict[num])
            
#         return res