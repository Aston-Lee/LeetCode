class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        maxarea, area = 0, 0
        
        def dfs(i, j):
            grid[i][j] = 0
            nonlocal area
            area += 1
            for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                if 0<=i+dx<m and 0<=j+dy<n and grid[i+dx][j+dy] == 1:
                    dfs(i+dx, j+dy)
            return
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i,j)
                    maxarea = max(maxarea, area)
                    
        return maxarea
                
        
