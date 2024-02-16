class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        DIR = ((0,1), (0,-1), (1,0), (-1,0))
        
        ## bfs
        m, n = len(mat), len(mat[0])
        
        res = []
        for _ in range(m):
            res.append([0]*n)
        # print(res)
        # res = [[0]*n]
        
        dq = deque()
        
        timer = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dq.append((i,j))
        # print(dq)
        
        visited = set()
        while dq:
            timer += 1
            for _ in range(len(dq)):
                i, j = dq.popleft()
                visited.add((i,j))
                for _x, _y in DIR:
                    ni, nj = i+_x, j+_y
                    if 0 <= ni < m and 0 <= nj < n:
                        if mat[ni][nj] == 1 and (ni, nj) not in visited:
                            # print((ni, nj))
                            dq.append((ni, nj))
                            mat[ni][nj] = 0
                            res[ni][nj] = timer
        
        return res
                        
                        
            
        
        
            
        
        
        
        
        
        
        
        
        