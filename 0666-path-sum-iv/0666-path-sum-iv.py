class Solution(object):
    def pathSum(self, nums):
        
        self.ans = 0
        PosVal = {}
        for num in nums:
            PosVal[num//10] = num%10
            
        def dfs(pos, pathsum):
            if pos not in PosVal:
                return 
            pathsum += PosVal[pos]
            
            depth, position = divmod(pos, 10)
            left = (depth+1)*10 + 2*position-1 ## note this
            right = left + 1
            
            if left not in PosVal and right not in PosVal:
                self.ans += pathsum
            dfs(left, pathsum)
            dfs(right, pathsum)
                
            
        dfs(nums[0]//10, 0)
        return self.ans
            
            
            
        
        
        
        