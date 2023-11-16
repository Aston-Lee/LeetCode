class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        ## brute force 
        # 2^digits to generate all the combination
        
        digits = len(nums)
        
        unique = set()
        
        def dfs(s):
            if len(s) == digits:
                unique.add(s)
            else:
                dfs(s+"0")
                dfs(s+"1")
            return 
        
        dfs("")
        
        for num in nums:
            unique.remove(num)
            
        return list(unique)[0] if unique else None
        
        
        
        
        
        
        
        
        