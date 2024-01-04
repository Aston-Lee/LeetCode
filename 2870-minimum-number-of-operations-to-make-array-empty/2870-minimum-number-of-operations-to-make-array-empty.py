class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        '''
        [2,3,3,2,2,4,2,3,4]
        {2:4, 3:3, 4:2} 
        operation = 4/2 + 3/3 + 2/2
        lets say we have one freq is 6 this should be 3*2 not 2*3
        7 3*1 2*2
        8 3*2 2*1
        9 3*3
        10 3*2 2*2
        
        
        [2,1,2,2,3,3]
        2:2
        
        '''
        
        def function(num):
            if num%3 == 0:
                return num // 3
            elif num%3 == 1:
                return (num//3)-1 + 2
            else: #num%3 == 2
                return num//3 + 1
            
        NumFreq = collections.Counter(nums)
        
        operation = 0
        for key, val in NumFreq.items():
            if val == 1:
                return -1
            operation += function(val)
            # print(key, val, operation)
            
        return operation
                
            