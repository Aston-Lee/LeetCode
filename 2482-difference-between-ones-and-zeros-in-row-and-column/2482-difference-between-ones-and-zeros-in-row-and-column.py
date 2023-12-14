import numpy as np
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0 
        2 + 1 - (3-2) - (3-1)
        2* (2+1) - 6
        
        2 + 3 - 1 - 0 = 4 
        
        2*(2 + 3) - 6 = 4
        
        2*(1+1) - 6 = -2
        '''
        
#         [[0,1,1],[1,0,1],[0,0,1]]
#         [2,2,1] = row 
        
#         [[0,1,1],[1,0,1],[0,0,1]]
        
        
        row = []
        for ls in grid:
            row.append(sum(ls))
            
        col  = []
        t_grid = np.transpose(grid)
        for ls in t_grid:
            col.append(sum(ls))
            
#         print(row, col)
        m, n = len(grid), len(grid[0])
            
        for i in range(len(row)):
            for j in range(len(col)):
                grid[i][j] = 2*(row[i]+col[j]) - (m+n)
                
        return grid
            

        
        