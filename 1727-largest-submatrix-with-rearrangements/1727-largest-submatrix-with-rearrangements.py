class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
#          [[0,0,1],[1,1,1],[1,0,1]]
            
#          [[0,0,1],[1,1,2],[2,1,3]]
#          [[1,0,0],[2,1,1],[3,2,1]]
        
        m, n = len(matrix), len(matrix[0])
        res = 0
        
        for i in range(m-1):
            for j in range(n):
                if matrix[i+1][j] != 0:
                    matrix[i+1][j] += matrix[i][j]
                
            matrix[i] = sorted(matrix[i], reverse = True )
        
        matrix[-1] = sorted(matrix[-1], reverse = True )
            
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    res = max(matrix[i][j] * (j+1), res) 
                    
        return res
        
            
        