class Solution:
    def pathSum(self, nums: List[int]) -> int:
        
        '''
        
        [113,215,221,312,322,332,345]
        11 -> 21, 22
        2*(n-1)+1, 2*(n-1)+2
        
        dict { 
            11: 3
            21: 5
            22: 1
        }
        '''
        
        LocNum = {}
        for num in nums:
            LocNum[num//10] = num%10
          
        self.ans = 0
        def dfs(node, tmp):
            tmp += LocNum[node]
            left = ((node//10)+1)*10 + 2*(node%10-1) + 1
            right = ((node//10)+1)*10 + 2*(node%10-1) + 2
            if left not in LocNum and right not in LocNum:
                self.ans += tmp 
                return 
            if left in LocNum:
                dfs(left, tmp)
            if right in LocNum:
                dfs(right, tmp)
            return 
        
        dfs(11, 0)
        
        return self.ans 
            
            
        