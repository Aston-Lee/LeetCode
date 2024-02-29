class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def dfs(string, left, right):
            if len(string) == 2*n:
                res.append(string)
                
            if left > right:
                return
                
            if left > 0:
                dfs(string+'(', left-1, right)
                
            if right > 0:
                dfs(string+')', left, right-1)
                
            return
        
        
        dfs("", n, n)
        
        return res