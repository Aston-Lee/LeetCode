class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        neighbor = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(i, j):
            # print(i, j)
            grid[i][j] = "0"
            for a, b in neighbor:
                if 0 <= i+a < m and 0 <= j+b < n and grid[i+a][j+b] == "1":
                    dfs(i+a, j+b)
            return
        
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island += 1
                    dfs(i, j)
                    
                    
        return island
                    
            