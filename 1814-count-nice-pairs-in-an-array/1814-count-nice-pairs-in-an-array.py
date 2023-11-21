class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        '''
        a + rev(b) = b + rev(a)
        a - rev(a) = b - rev(b)
        
        [42,11,1,97]
        -18 0 0 -18        
        ''' 
        MOD = 10**9 + 7
        def rev(s):
            s = str(s)
            tmp = ""
            for i in range(len(s)-1, -1, -1):
                tmp+=s[i]
            return int(tmp)
        
        minus = []
        for num in nums:
            minus.append(num - rev(num))
        
        count = {}
        res = 0
        for num in minus:
            if num in count:
                res += count[num] % MOD
                count[num] += 1
            else:
                count[num] = 1
                
        return res % MOD
                
#         [13,10,35,24,76]
        
#         -18 9 -18 -18 9
        
                    
                    
        
        
        
        
        
#         '''
#         brute force TLE
#         '''
#         MOD = 10**9 + 7
#         def rev(s):
#             s = str(s)
#             tmp = ""
#             for i in range(len(s)-1, -1, -1):
#                 tmp+=s[i]
#             return int(tmp)
        
#         reverse = []
#         for num in nums:
#             reverse.append(rev(num))
        
#         res = 0
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + reverse[j] == nums[j] + reverse[i]:
#                     res += 1
#         return res % MOD
        
            
            
            