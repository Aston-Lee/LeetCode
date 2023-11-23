class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        tower = [[0]*(r+1) for r in range(query_row+2)]
        
        tower[0][0] = poured 
        
        for r in range(query_row+1):
            for g in range(r+1):
                # print(r,g,tower[r][g])
                if tower[r][g]>1:
                    remain = tower[r][g]-1
                    tower[r+1][g] += remain/2
                    tower[r+1][g+1] += remain/2
                    
        return min(1, tower[query_row][query_glass])
    
        
                    
                
            