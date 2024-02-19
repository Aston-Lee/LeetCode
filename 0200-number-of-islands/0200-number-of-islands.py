class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        DIR = ((0,1), (0,-1), (1,0), (-1,0))
        
        m, n = len(grid), len(grid[0])
        
        def dfs(i,j):
            grid[i][j] = "0"
            for _x, _y in DIR:
                ni, nj = i+_x, j+_y
                if 0<=ni<m and 0<=nj<n:
                    if grid[ni][nj] == "1":
                        dfs(ni,nj)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)
        
        return ans
                    
        