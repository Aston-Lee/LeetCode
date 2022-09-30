class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp mem / bottom up
        mem = [[False]*n]*m
        mem[0][0] = 0
        
        ## top down will encountered maximum recursion error and its not dp (no mem)
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    mem[i][j] = 1
                else:
                    mem[i][j] = mem[i-1][j] + mem[i][j-1]
                    
        return mem[m-1][n-1]
                    
        
            
        
        