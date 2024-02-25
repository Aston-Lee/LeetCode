class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        DIR = [(0,1), (0,-1), (1,0), (-1,0)]
        
        m, n = len(grid), len(grid[0])
        dq = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    dq.append((i,j))
                    visited.add((i,j))
                    break
        
        steps = 0
        while dq:
            steps += 1
            # print(steps, dq)
            for _ in range(len(dq)):
                i, j = dq.popleft()
                for _x, _y in DIR:
                    ni, nj = i+_x, j+_y
                    if 0<=ni<m and 0<=nj<n:
                        if grid[ni][nj] == 'O' and (ni,nj) not in visited:
                            dq.append((ni,nj))
                            visited.add((ni,nj))
                        elif grid[ni][nj] == '#':
                            return steps
                        
        return -1