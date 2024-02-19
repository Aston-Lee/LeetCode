class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        DIR = [(0,1),(0,-1),(1,0),(-1,0)]
        
        m, n = len(grid), len(grid[0])
        
        
        dq = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dq.append((i,j))
                    visited.add((i,j))
        
        time = -1
        while dq:
            time += 1
            for _ in range(len(dq)):
                i, j = dq.popleft()
                for _x, _y in DIR:
                    ni, nj = i+_x, j+_y
                    if 0<=ni<m and 0<=nj<n:
                        if grid[ni][nj] == 1 and (ni, nj) not in visited:
                            grid[ni][nj] = 2
                            dq.append((ni,nj))
                            visited.add((ni,nj))
                            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                
        return time if time != -1 else 0
        
                        
        