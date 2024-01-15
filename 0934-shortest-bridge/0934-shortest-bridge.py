class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        '''
        bfs
        [[0,1,0],[0,0,0],[0,0,1]]
        
        dq
        time = 1
        [[1,1,1],[0,1,1],[0,1,1]]
        
        
        ## label which is island 1, which is island 2 
        make the first 1 to 2 and dfs all of its connection
        
        
        
        '''
        m, n = len(grid), len(grid[0])
        changed = False
        DIR = ((1,0), (-1,0), (0,1), (0,-1))
        dq1, dq2 = deque(), deque()
        island1, island2 = set(), set()
        def changeLabel(x, y):
            if not changed: ## change the first island label 1 to 2
                if grid[x][y] != 1:
                    return
                if (x,y) not in island2:
                    island2.add((x,y))
                    dq2.append((x, y))
                    grid[x][y] = 2
                    for _i, _j in DIR:
                        n_x, n_y = x+_i, y+_j
                        if 0 <= n_x < m and 0 <= n_y < n:
                            changeLabel(n_x, n_y)
                        
            else: ## island 1
                if grid[x][y] != 1:
                    return
                if (x,y) not in island1:
                    island1.add((x,y))
                    dq1.append((x,y))
                    for _i, _j in DIR:
                        n_x, n_y = x+_i, y+_j
                        if 0 <= n_x < m and 0 <= n_y < n:
                            changeLabel(n_x, n_y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and changed:
                    changeLabel(i, j)
                    break
                if grid[i][j] == 1 and not changed:
                    changeLabel(i, j)
                    changed = True
                    
        # print(grid)
        # print(dq1)
        # print(dq2)
                    
        flip = 0
        visited = set()
        while dq1 or dq2:
            
            newdq1 = set()
            for _ in range(len(dq1)):
                x, y = dq1.popleft()
                for _i, _j in DIR:
                    n_x, n_y = x+_i, y+_j
                    if 0 <= n_x < m and 0 <= n_y < n:
                        if grid[n_x][n_y] == 0:
                            grid[n_x][n_y] = 1
                            newdq1.add((n_x, n_y))
                        if grid[n_x][n_y] == 2:
                            return flip

            newdq2 = set()
            for _ in range(len(dq2)):
                x, y = dq2.popleft()
                for _i, _j in DIR:
                    n_x, n_y = x+_i, y+_j
                    if 0 <= n_x < m and 0 <= n_y < n:
                        if grid[n_x][n_y] == 0:
                            grid[n_x][n_y] = 2
                            newdq2.add((n_x, n_y))
                        if grid[n_x][n_y] == 1:
                            return flip+1
            
            if newdq1 & newdq2:
                return flip+1
            flip += 2
            
            dq1 = deque(list(newdq1))
            dq2 = deque(list(newdq2))
            
            # print("flip:", flip)
            # print(grid)
            # print(dq1)
            # print(dq2)

            