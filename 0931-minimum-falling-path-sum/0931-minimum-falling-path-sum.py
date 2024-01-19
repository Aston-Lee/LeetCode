class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
#         [[2,1,3],[6,5,4],[7,8,9]]
#         [[2,1,3],[8,8,7],[15,16,17]]
        
        
        m, n = len(matrix), len(matrix[0])
        i = 1
        while i != m:
            for j in range(n):
                if j == 0:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j+1]) + matrix[i][j]
                elif j == n-1:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j]) + matrix[i][j]
                else:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1]) + matrix[i][j]
            
            i += 1
            
        return min(matrix[-1])