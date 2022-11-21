class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ## bfs with queue
        
        m , n = len(grid), len(grid[0])
        path = [(0,1), (0,-1), (1,0), (-1,0)]
        
        t = 0
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i , j))
        
        if len(q) == 0:
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return -1
            return 0
        
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                for offset_x, offset_y in path:
                    new_x, new_y = x+offset_x, y+offset_y
                    if 0 <= new_x and 0 <= new_y \
                        and new_x < m and new_y < n \
                        and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        q.append((new_x, new_y))
            t += 1
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return t-1
                
